// AgriSuper Main JavaScript Functions

// Global variables
const currentFeature = null
const loadingStates = {}
const $ = window.jQuery // Declare the $ variable
const bootstrap = window.bootstrap // Declare the bootstrap variable
const handleCalculation = () => {
  console.log("Calculation button clicked")
} // Declare handleCalculation
const handlePrediction = () => {
  console.log("Prediction button clicked")
} // Declare handlePrediction
const handleAnalysis = () => {
  console.log("Analysis button clicked")
} // Declare handleAnalysis

// Initialize application
$(document).ready(() => {
  initializeApp()
  setupEventListeners()
  loadDashboardData()
})

// Initialize application
function initializeApp() {
  console.log("AgriSuper Application Initialized")

  // Add fade-in animation to cards
  $(".feature-card").each(function (index) {
    $(this)
      .delay(index * 100)
      .queue(function () {
        $(this).addClass("fade-in").dequeue()
      })
  })

  // Initialize tooltips
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl))
  
  // Initialize categorized dashboard
  initializeCategorizedDashboard()
}

// Initialize the categorized dashboard functionality
function initializeCategorizedDashboard() {
    if (window.location.pathname === '/categorized-dashboard') {
        // Initialize counters with animation
        $('.counter').each(function() {
            const $this = $(this);
            const countTo = parseInt($this.text().replace(/[^0-9]/g, ''));
            
            $({ countNum: 0 }).animate({
                countNum: countTo
            }, {
                duration: 2000,
                easing: 'swing',
                step: function() {
                    if ($this.text().includes('₹')) {
                        $this.text('₹' + Math.floor(this.countNum).toLocaleString());
                    } else {
                        $this.text(Math.floor(this.countNum) + '%');
                    }
                },
                complete: function() {
                    if ($this.text().includes('₹')) {
                        $this.text('₹' + countTo.toLocaleString());
                    } else {
                        $this.text(countTo + '%');
                    }
                }
            });
        });
        
        // Feature search functionality
        $('#featureSearch').on('input', function() {
            const searchTerm = $(this).val().toLowerCase();
            
            $('.feature-card').each(function() {
                const cardTitle = $(this).find('.card-title').text().toLowerCase();
                const cardText = $(this).find('.card-text').text().toLowerCase();
                
                if (cardTitle.includes(searchTerm) || cardText.includes(searchTerm)) {
                    $(this).closest('.col-md-4').show();
                } else {
                    $(this).closest('.col-md-4').hide();
                }
            });
            
            // Show/hide category headers based on visible cards
            $('.category-title').each(function() {
                const categorySection = $(this).closest('.col-12');
                const visibleCards = categorySection.find('.feature-card').filter(function() {
                    return $(this).closest('.col-md-4').is(':visible');
                });
                
                if (visibleCards.length === 0) {
                    categorySection.hide();
                } else {
                    categorySection.show();
                }
            });
        });
        
        // Clear search when switching tabs
        $('#featureCategories .nav-link').on('click', function() {
            $('#featureSearch').val('');
            $('.feature-card').closest('.col-md-4').show();
            $('.category-title').closest('.col-12').show();
        });
    }
}

// Setup event listeners
function setupEventListeners() {
  // Form submissions
  $(document).on("submit", ".ajax-form", handleAjaxForm)

  // Button clicks
  $(document).on("click", ".btn-calculate", handleCalculation)
  $(document).on("click", ".btn-predict", handlePrediction)
  $(document).on("click", ".btn-analyze", handleAnalysis)

  // Real-time updates
  setInterval(updateRealTimeData, 30000) // Update every 30 seconds
  
  // Mobile menu functionality
  setupMobileMenu()
}

// Setup mobile menu functionality
function setupMobileMenu() {
  // Close mobile menu when a link is clicked
  $('.navbar-nav .nav-link, .list-group-item-action').on('click', function() {
    if ($(window).width() < 992) {
      $('.navbar-collapse').collapse('hide');
      $('#mobileCategoryMenu').collapse('hide');
    }
  });
  
  // Handle mobile category menu toggle
  $('.mobile-menu-toggle').on('click', function() {
    const isExpanded = $(this).attr('aria-expanded') === 'true';
    $(this).find('i').toggleClass('fa-th-large fa-times');
    
    if (isExpanded) {
      $(this).html('<i class="fas fa-th-large me-2"></i>Feature Categories');
    } else {
      $(this).html('<i class="fas fa-times me-2"></i>Close Categories');
    }
  });
  
  // Adjust navbar on scroll for mobile
  $(window).on('scroll', function() {
    if ($(window).width() < 992) {
      if ($(this).scrollTop() > 50) {
        $('.navbar').addClass('navbar-shrink');
      } else {
        $('.navbar').removeClass('navbar-shrink');
      }
    }
  });
}

// Load dashboard data
function loadDashboardData() {
  // Simulate loading dashboard statistics
  setTimeout(() => {
    updateDashboardStats()
  }, 1000)
}

// Update dashboard statistics
function updateDashboardStats() {
  const stats = {
    totalFarmers: 15420,
    activeBuyers: 2340,
    totalTransactions: 89650,
    totalRevenue: "Rs. 45.2 Cr",
  }

  // Animate counters if elements exist
  animateCounter("#total-farmers", stats.totalFarmers)
  animateCounter("#active-buyers", stats.activeBuyers)
  animateCounter("#total-transactions", stats.totalTransactions)
}

// Animate counter
function animateCounter(selector, target) {
  const element = $(selector)
  if (element.length) {
    $({ counter: 0 }).animate(
      { counter: target },
      {
        duration: 2000,
        easing: "swing",
        step: function () {
          element.text(Math.ceil(this.counter).toLocaleString())
        },
      },
    )
  }
}

// Handle AJAX form submissions
function handleAjaxForm(e) {
  e.preventDefault()

  const form = $(this)
  const url = form.attr("action")
  const method = form.attr("method") || "POST"
  const formData = new FormData(form[0])

  // Show loading state
  showLoading(form)

  // Convert FormData to JSON for API calls
  const jsonData = {}
  for (const [key, value] of formData.entries()) {
    jsonData[key] = value
  }

  $.ajax({
    url: url,
    method: method,
    data: JSON.stringify(jsonData),
    contentType: "application/json",
    success: (response) => {
      handleApiResponse(response, form)
    },
    error: (xhr, status, error) => {
      handleApiError(error, form)
    },
    complete: () => {
      hideLoading(form)
    },
  })
}

// Handle API responses
function handleApiResponse(response, form) {
  if (response.success) {
    showSuccess(response.message || "Operation completed successfully")

    // Update UI based on response type
    if (response.data) {
      updateUIWithData(response.data, form)
    }
  } else {
    showError(response.message || "Operation failed")
  }
}

// Handle API errors
function handleApiError(error, form) {
  console.error("API Error:", error)
  showError("An error occurred. Please try again.")
}

// Update UI with response data
function updateUIWithData(data, form) {
  const resultContainer = form.siblings(".result-container")

  if (resultContainer.length) {
    // Clear previous results
    resultContainer.empty()

    // Generate result HTML based on data type
    if (data.chart) {
      renderChart(data.chart, resultContainer)
    }

    if (data.table) {
      renderTable(data.table, resultContainer)
    }

    if (data.cards) {
      renderCards(data.cards, resultContainer)
    }

    // Show results with animation
    resultContainer.addClass("slide-up").show()
  }
}

// Render chart
function renderChart(chartData, container) {
  const chartHtml = `
        <div class="card mb-4">
            <div class="card-header">
                <h5><i class="fas fa-chart-line me-2"></i>${chartData.title}</h5>
            </div>
            <div class="card-body">
                <canvas id="chart-${Date.now()}" class="chart-canvas"></canvas>
            </div>
        </div>
    `
  container.append(chartHtml)

  // Initialize chart (placeholder for actual chart library)
  console.log("Chart data:", chartData)
}

// Render table
function renderTable(tableData, container) {
  let tableHtml = `
        <div class="card mb-4">
            <div class="card-header">
                <h5><i class="fas fa-table me-2"></i>${tableData.title}</h5>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-striped table-hover">
                        <thead>
                            <tr>
    `

  // Add headers
  tableData.headers.forEach((header) => {
    tableHtml += `<th>${header}</th>`
  })

  tableHtml += `
                            </tr>
                        </thead>
                        <tbody>
    `

  // Add rows
  tableData.rows.forEach((row) => {
    tableHtml += "<tr>"
    row.forEach((cell) => {
      tableHtml += `<td>${cell}</td>`
    })
    tableHtml += "</tr>"
  })

  tableHtml += `
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    `

  container.append(tableHtml)
}

// Render cards
function renderCards(cardsData, container) {
  let cardsHtml = '<div class="row g-3 mb-4">'

  cardsData.forEach((card) => {
    cardsHtml += `
            <div class="col-md-4">
                <div class="card text-center">
                    <div class="card-body">
                        <div class="display-6 text-${card.color || "primary"} mb-2">
                            <i class="${card.icon || "fas fa-info-circle"}"></i>
                        </div>
                        <h5 class="card-title">${card.title}</h5>
                        <p class="card-text display-6 fw-bold text-${card.color || "primary"}">${card.value}</p>
                        ${card.description ? `<small class="text-muted">${card.description}</small>` : ""}
                    </div>
                </div>
            </div>
        `
  })

  cardsHtml += "</div>"
  container.append(cardsHtml)
}

// Show loading state
function showLoading(element) {
  const loadingHtml = `
        <div class="loading-overlay">
            <div class="text-center">
                <div class="spinner-border text-success" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
                <p class="mt-2">Processing...</p>
            </div>
        </div>
    `

  element.append(loadingHtml)
  element.find('button[type="submit"]').prop("disabled", true)
}

// Hide loading state
function hideLoading(element) {
  element.find(".loading-overlay").remove()
  element.find('button[type="submit"]').prop("disabled", false)
}

// Show success message
function showSuccess(message) {
  showAlert(message, "success")
}

// Show error message
function showError(message) {
  showAlert(message, "danger")
}

// Show alert
function showAlert(message, type) {
  const alertHtml = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            <i class="fas fa-${type === "success" ? "check-circle" : "exclamation-circle"} me-2"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `

  // Add to top of main content
  $(".main-content").prepend(alertHtml)

  // Auto-dismiss after 5 seconds
  setTimeout(() => {
    $(".alert").fadeOut()
  }, 5000)
}

// Update real-time data
function updateRealTimeData() {
  // Update disaster alerts
  updateDisasterAlerts()

  // Update pest alerts
  updatePestAlerts()

  // Update market prices
  updateMarketPrices()
}

// Update disaster alerts
function updateDisasterAlerts() {
  $.get("/api/disaster-alerts/get-alerts", (response) => {
    if (response && Array.isArray(response) && response.length > 0) {
      updateAlertBadge("disaster-alerts", response.length)
    }
  })
}

// Update pest alerts
function updatePestAlerts() {
  $.get("/api/pest-alerts/get-alerts", (response) => {
    if (response && Array.isArray(response) && response.length > 0) {
      updateAlertBadge("pest-alerts", response.length)
    }
  })
}

// Update market prices
function updateMarketPrices() {
  // Placeholder for real-time market price updates
  console.log("Updating market prices...")
}

// Update alert badge
function updateAlertBadge(type, count) {
  const badge = $(`.alert-badge[data-type="${type}"]`)
  if (badge.length) {
    badge.text(count).show()
  }
}

// Utility functions
function formatCurrency(amount) {
  return new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
  }).format(amount)
}

function formatDate(date) {
  return new Intl.DateTimeFormat("en-IN").format(new Date(date))
}

function debounce(func, wait) {
  let timeout
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout)
      func(...args)
    }
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
  }
}

// Export functions for use in feature-specific scripts
window.AgriSuper = {
  showLoading,
  hideLoading,
  showSuccess,
  showError,
  formatCurrency,
  formatDate,
  debounce,
  handleApiResponse,
  handleApiError,
}
