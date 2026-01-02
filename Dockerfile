# Multi-stage Dockerfile for AgriSuper-App
# Stage 1: Base image with dependencies
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    postgresql-client \
    libpq-dev \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy requirements
COPY requirements.txt requirements-production.txt ./

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements-production.txt

# ===================================
# Stage 2: Development
# ===================================
FROM base as development

# Install development tools
RUN pip install pytest pytest-cov black flake8 pylint ipython

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Run development server
CMD ["python", "app.py"]

# ===================================
# Stage 3: Production
# ===================================
FROM base as production

# Create non-root user
RUN useradd -m -u 1000 agrisuper && \
    mkdir -p /app/data /app/logs /app/uploads && \
    chown -R agrisuper:agrisuper /app

# Copy application code
COPY --chown=agrisuper:agrisuper . .

# Switch to non-root user
USER agrisuper

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Expose port
EXPOSE 5000

# Run production server with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--timeout", "120", "--log-level", "info", "app:app"]
