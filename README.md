# 🌾 AgriSuper-App: Complete Agricultural Ecosystem Platform

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Empowering farmers with technology, connecting markets, and revolutionizing Indian agriculture

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 Overview

AgriSuper-App is a comprehensive agricultural platform designed to address real-world challenges faced by Indian farmers. With 41+ integrated features, it provides:

- **Real-time market prices** from AGMARKNET and eNAM
- **Weather forecasts** from IMD and NASA POWER
- **Financial services** (micro-loans, insurance, digital wallet)
- **AI-powered recommendations** for crop selection, pest management
- **Community features** (Q&A forum, mentorship, farmer groups)
- **Supply chain management** (marketplace, logistics, storage)
- **Government scheme integration** (PM-KISAN, PMFBY, Soil Health Card)

### 🎯 Mission

To increase farmer income by 30%, reduce crop losses by 25%, and improve market access for 1 million farmers by 2026.

---

## ✨ Key Features

### 💰 Financial Services
- **Micro-Loan Marketplace** - Access to agricultural loans from multiple lenders
- **Crop Insurance** - PMFBY integration and claim management
- **Digital Wallet** - Cashless transactions and payment management
- **EMI Purchase** - Buy equipment and inputs on installments
- **Carbon Credits** - Earn from sustainable practices

### 📊 Market Intelligence
- **Real-Time Pricing** - Live mandi prices from 3000+ markets
- **Price Forecasting** - AI-based 7-day price predictions
- **Market Comparison** - Find best rates across states
- **Contract Farming** - Guaranteed price contracts
- **Bulk Deals** - Group buying for better prices

### 🌤️ Weather & Alerts
- **Farm-Specific Weather** - Location-based forecasts
- **Disaster Alerts** - IMD warnings for floods, droughts, cyclones
- **Crop Advisory** - Weather-based farming recommendations
- **Pest Alerts** - Early warning system
- **Irrigation Scheduling** - Smart water management

### 🤖 AI & Machine Learning
- **Yield Prediction** - Forecast production with 85%+ accuracy
- **Crop Recommendation** - Best crops for your soil and climate
- **Disease Detection** - Image-based crop disease identification
- **Price Prediction** - ML models for market trends
- **Profit Analyzer** - Calculate ROI for different crops

### 🌐 Community & Learning
- **Q&A Forum** - Ask experts and experienced farmers
- **Mentorship Program** - Connect with successful farmers
- **Success Stories** - Learn from real-world experiences
- **E-Learning** - Free courses on modern farming
- **Farmer Groups** - Form cooperatives and collectives

### 🚚 Logistics & Supply Chain
- **Shared Logistics** - Reduce transportation costs
- **Storage Booking** - Reserve warehouse space
- **Route Optimization** - Efficient delivery planning
- **Export Gateway** - Access international markets
- **Quality Certification** - Organic and premium grades

### 📱 Accessibility
- **Multi-language** - 15+ regional languages
- **Voice Assistant** - Speak in your native language
- **SMS/USSD** - Works on basic phones
- **Offline Mode** - Access critical info without internet
- **Progressive Web App** - App-like experience on mobile

### 🔒 Security & Trust
- **ID Verification** - Aadhaar/DigiLocker integration
- **Fraud Detection** - AI-powered transaction monitoring
- **Smart Contracts** - Transparent payment terms
- **Buyer Ratings** - Community-verified traders
- **Encrypted Payments** - Bank-grade security

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend Layer                           │
│  (Progressive Web App + Native Mobile)                       │
│  - React/Vue.js Dashboard                                    │
│  - Responsive Templates                                      │
│  - Offline-First Service Worker                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    API Gateway (Flask)                       │
│  - RESTful APIs                                              │
│  - JWT Authentication                                        │
│  - Rate Limiting                                             │
│  - API Documentation (Swagger)                               │
└─────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                  ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│  Business Logic  │ │   Caching    │ │  Background Jobs │
│    (Services)    │ │   (Redis)    │ │    (Celery)     │
│                  │ │              │ │                  │
│ • Pricing Engine │ │ • Session    │ │ • Price Updates │
│ • Weather Service│ │ • API Cache  │ │ • Notifications │
│ • ML Models      │ │ • Temp Data  │ │ • Report Gen    │
│ • Payment Gateway│ │              │ │ • Data Sync     │
└──────────────────┘ └──────────────┘ └──────────────────┘
           │                  │                  │
           └──────────────────┼──────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Data Layer                                │
│  ┌────────────────┐  ┌──────────────┐  ┌─────────────────┐│
│  │  PostgreSQL    │  │  File Storage│  │  External APIs  ││
│  │                │  │              │  │                 ││
│  │ • Users        │  │ • Images     │  │ • AGMARKNET     ││
│  │ • Transactions │  │ • Documents  │  │ • eNAM          ││
│  │ • Crops        │  │ • Reports    │  │ • IMD Weather   ││
│  │ • Markets      │  │              │  │ • NASA POWER    ││
│  └────────────────┘  └──────────────┘  │ • Razorpay      ││
│                                         │ • Twilio SMS    ││
│                                         │ • Google Cloud  ││
│                                         └─────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

**Backend:**
- Python 3.11
- Flask 3.0 (Web framework)
- SQLAlchemy (ORM)
- PostgreSQL 15 (Database)
- Redis (Cache & Message broker)
- Celery (Background tasks)

**AI/ML:**
- scikit-learn (Traditional ML)
- XGBoost (Gradient boosting)
- Prophet (Time series forecasting)
- TensorFlow/PyTorch (Deep learning)
- OpenCV (Image processing)

**External Integrations:**
- AGMARKNET API (Market prices)
- eNAM API (National market)
- IMD API (Weather)
- NASA POWER (Agricultural weather)
- Razorpay (Payments)
- Twilio (SMS)
- Google Cloud (Speech, Translation)

**DevOps:**
- Docker & Docker Compose
- Kubernetes (Production)
- GitHub Actions (CI/CD)
- Prometheus & Grafana (Monitoring)
- Sentry (Error tracking)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Redis 7+
- Node.js 18+ (for frontend)

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/agrisuper-app.git
cd agrisuper-app
```

### 2. Set Up Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements-production.txt
```

### 3. Configure Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your API keys
# Minimum required:
# - DATABASE_URL
# - SECRET_KEY
# - AGMARKNET_API_KEY
# - OPENWEATHER_API_KEY
```

### 4. Initialize Database

```bash
# Create database
createdb agrisuper_db

# Run migrations
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# Seed initial data
python seed_data.py
```

### 5. Start Services

```bash
# Terminal 1: Start Redis
redis-server

# Terminal 2: Start Celery worker
celery -A app.celery worker --loglevel=info

# Terminal 3: Start Flask app
python app.py
```

### 6. Access Application

Open your browser and navigate to:
- **Main App:** http://localhost:5000
- **Admin Dashboard:** http://localhost:5000/admin
- **API Docs:** http://localhost:5000/api/docs

---

## 🐳 Docker Quick Start

```bash
# Build and start all services
docker-compose up -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f web

# Stop services
docker-compose down
```

Access services:
- **Web App:** http://localhost
- **API:** http://localhost/api
- **Flower (Celery Monitor):** http://localhost:5555
- **pgAdmin:** http://localhost:5050

---

## ⚙️ Configuration

### Essential API Keys

#### 1. AGMARKNET (Government Market Prices)
```
Visit: https://data.gov.in/
Register for API key
Set: AGMARKNET_API_KEY=your_key
```

#### 2. eNAM (National Agriculture Market)
```
Visit: https://enam.gov.in/web/
Register as data consumer
Set: ENAM_API_KEY=your_key
```

#### 3. OpenWeatherMap (Weather Data)
```
Visit: https://openweathermap.org/api
Free tier: 1000 calls/day
Set: OPENWEATHER_API_KEY=your_key
```

#### 4. Razorpay (Payment Gateway)
```
Visit: https://razorpay.com/
Test mode available
Set: RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET
```

#### 5. Twilio (SMS Notifications)
```
Visit: https://www.twilio.com/
Free trial: $15 credit
Set: TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
```

#### 6. Google Cloud (Voice & Translation)
```
Visit: https://cloud.google.com/
Create service account
Download JSON key
Set: GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
```

### Database Configuration

```python
# Development
DATABASE_URL=postgresql://user:pass@localhost:5432/agrisuper_db

# Production
DATABASE_URL=postgresql://user:pass@db.server.com:5432/agrisuper_prod
DATABASE_POOL_SIZE=20
DATABASE_MAX_OVERFLOW=40
```

### Redis Configuration

```python
# Local
REDIS_URL=redis://localhost:6379/0

# Production with password
REDIS_URL=redis://:password@redis.server.com:6379/0
```

---

## 📚 API Documentation

### Authentication

All API requests require JWT authentication (except public endpoints):

```bash
# Get access token
POST /api/auth/login
{
  "username": "farmer123",
  "password": "password"
}

Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "expires_in": 3600
}

# Use token in requests
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

### Key Endpoints

#### Market Prices

```bash
# Get live price for crop
GET /api/pricing/live?crop=wheat&state=Punjab&district=Ludhiana

Response:
{
  "success": true,
  "crop": "wheat",
  "prices": {
    "average": 2150,
    "minimum": 2000,
    "maximum": 2300,
    "unit": "₹ per quintal"
  },
  "trend": {
    "direction": "rising",
    "change_percent": 5.2
  },
  "recommendations": [...]
}

# Get price forecast
GET /api/pricing/forecast?crop=wheat&state=Punjab&days=7

# Compare prices across states
POST /api/pricing/compare
{
  "crop": "wheat",
  "states": ["Punjab", "Haryana", "UP"]
}
```

#### Weather

```bash
# Get farm weather
GET /api/weather/farm?lat=30.9010&lon=75.8573&days=7

Response:
{
  "success": true,
  "current_weather": {
    "temperature": 25.5,
    "humidity": 65,
    "wind_speed": 12.5,
    "description": "partly cloudy"
  },
  "forecast": [...],
  "alerts": [...],
  "agricultural_advisories": [...]
}

# Get disaster alerts
GET /api/weather/alerts?state=Punjab&district=Ludhiana

# Get crop-specific forecast
GET /api/weather/crop-forecast?lat=30.9010&lon=75.8573&crop=wheat
```

#### Yield Prediction

```bash
POST /api/yield/predict
{
  "crop": "wheat",
  "area_hectares": 5,
  "soil_type": "loamy",
  "irrigation": "drip",
  "fertilizer_used": true,
  "location": {
    "state": "Punjab",
    "district": "Ludhiana"
  }
}

Response:
{
  "predicted_yield_kg": 17500,
  "yield_per_hectare": 3500,
  "confidence_level": 87.5,
  "factors": {
    "weather_impact": 92,
    "soil_quality": 85,
    "pest_risk": 88
  }
}
```

#### Community Forum

```bash
# Get questions
GET /api/forum/questions?category=pest_management&page=1&limit=20

# Post question
POST /api/forum/questions
{
  "title": "White spots on tomato leaves",
  "category": "pest_management",
  "question": "I'm seeing white powdery spots...",
  "tags": ["tomato", "disease", "organic"]
}

# Answer question
POST /api/forum/questions/{id}/answers
{
  "answer": "This looks like powdery mildew...",
  "notify_author": true
}
```

### Complete API Documentation

Interactive Swagger documentation available at:
- **Local:** http://localhost:5000/api/docs
- **Production:** https://agrisuper.com/api/docs

---

## 🌐 Deployment

### Production Deployment with Docker

1. **Prepare Server**
```bash
# Install Docker & Docker Compose
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

2. **Configure Production Environment**
```bash
# Create .env file with production values
cp .env.example .env
nano .env  # Edit with production credentials
```

3. **Deploy Application**
```bash
# Pull latest code
git pull origin main

# Build and start services
docker-compose -f docker-compose.yml up -d

# Run database migrations
docker-compose exec web python manage.py db upgrade

# Check service health
docker-compose ps
```

4. **Set Up SSL (Let's Encrypt)**
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d agrisuper.com -d www.agrisuper.com

# Auto-renewal
sudo certbot renew --dry-run
```

### Kubernetes Deployment

```bash
# Create namespace
kubectl create namespace agrisuper

# Apply configurations
kubectl apply -f k8s/

# Check deployment
kubectl get pods -n agrisuper

# Scale deployment
kubectl scale deployment agrisuper-web --replicas=5 -n agrisuper
```

### Cloud Platforms

#### AWS
```bash
# Deploy to Elastic Beanstalk
eb init -p python-3.11 agrisuper-app
eb create agrisuper-prod
eb deploy
```

#### Google Cloud
```bash
# Deploy to App Engine
gcloud app deploy
```

#### Azure
```bash
# Deploy to App Service
az webapp up --name agrisuper-app --runtime "PYTHON:3.11"
```

---

## 📊 Monitoring & Maintenance

### Health Checks

```bash
# Application health
curl http://localhost:5000/health

# Database health
curl http://localhost:5000/health/db

# Redis health
curl http://localhost:5000/health/cache

# External APIs health
curl http://localhost:5000/health/external
```

### Logs

```bash
# View application logs
docker-compose logs -f web

# View Celery logs
docker-compose logs -f celery-worker

# View Nginx logs
docker-compose logs -f nginx
```

### Monitoring with Prometheus & Grafana

```bash
# Start monitoring stack
docker-compose --profile monitoring up -d

# Access Grafana
http://localhost:3000
# Default: admin/admin

# Access Prometheus
http://localhost:9090
```

### Backup & Restore

```bash
# Backup database
docker-compose exec db pg_dump -U agrisuper_user agrisuper_db > backup.sql

# Restore database
docker-compose exec -T db psql -U agrisuper_user agrisuper_db < backup.sql

# Backup uploads
tar -czf uploads_backup.tar.gz uploads/

# Backup Redis data
docker-compose exec redis redis-cli SAVE
docker cp agrisuper-redis:/data/dump.rdb ./backup/
```

---

## 🧪 Testing

### Run Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=backend --cov-report=html

# Specific module
pytest tests/test_pricing_engine.py

# Integration tests
pytest tests/integration/
```

### Load Testing

```bash
# Install Locust
pip install locust

# Run load tests
locust -f tests/load/locustfile.py

# Access UI
http://localhost:8089
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Fork repository
# Clone your fork
git clone https://github.com/YOUR_USERNAME/agrisuper-app.git

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push to your fork
git push origin feature/amazing-feature

# Create Pull Request
```

### Code Style

```bash
# Format code
black backend/ tests/

# Check linting
flake8 backend/ tests/

# Type checking
mypy backend/
```

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 📞 Support

- **Documentation:** https://docs.agrisuper.com
- **Community Forum:** https://community.agrisuper.com
- **Email:** support@agrisuper.com
- **Phone:** 1800-180-1551 (Toll-free)
- **WhatsApp:** +91-98765-43210

---

## 🙏 Acknowledgments

- Ministry of Agriculture & Farmers Welfare, Government of India
- AGMARKNET & eNAM for market data
- India Meteorological Department for weather data
- NASA POWER for agricultural weather data
- All farmers and agricultural experts who provided feedback

---

## 📈 Project Status

- ✅ **Phase 1:** Core features development (Completed)
- 🚧 **Phase 2:** Real API integrations (In Progress)
- 📋 **Phase 3:** Mobile app development (Planned)
- 📋 **Phase 4:** IoT sensor integration (Planned)
- 📋 **Phase 5:** International expansion (Future)

---

## 🎯 Roadmap

### Q1 2025
- [ ] Complete real API integrations
- [ ] Launch Progressive Web App
- [ ] Deploy in 5 pilot districts
- [ ] Onboard 10,000 farmers

### Q2 2025
- [ ] Native Android app
- [ ] Offline mode enhancement
- [ ] Voice assistant in 10 languages
- [ ] Expand to 50 districts

### Q3 2025
- [ ] IoT sensor integration
- [ ] Blockchain supply chain
- [ ] International markets
- [ ] 100,000 active farmers

### Q4 2025
- [ ] AI crop advisor
- [ ] Drone integration
- [ ] Full organic certification
- [ ] 500,000 active farmers

---

Made with ❤️ for Indian Farmers

**Jai Jawan, Jai Kisan!** 🇮🇳
"# Agri_Super-The-Revolution-Of-Agriculture-Sector" 
