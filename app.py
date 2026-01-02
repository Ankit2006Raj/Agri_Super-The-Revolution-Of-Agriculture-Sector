from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from datetime import datetime, timedelta
import json
import os

# Import all feature modules
from backend.pricing_engine import PricingEngine
from backend.subscription_model import SubscriptionModel
from backend.contract_farming import ContractFarmingEngine
from backend.bulk_deals import BulkDealsEngine
from backend.yield_prediction import YieldPredictionEngine
from backend.crop_rotation import CropRotationEngine
from backend.market_comparison import MarketComparisonEngine
from backend.profit_analyzer import ProfitAnalyzerEngine
from backend.disaster_alerts import DisasterAlertsEngine
from backend.sowing_calendar import SowingCalendarEngine
from backend.pest_alerts import PestAlertsEngine
from backend.elearning_courses import ELearningCourses
from backend.success_stories import SuccessStories
from backend.voice_assistant import VoiceAssistant
from backend.soil_knowledge import SoilKnowledge
from backend.micro_loans import MicroLoans
from backend.crop_insurance import CropInsurance
from backend.digital_wallet import DigitalWallet
from backend.emi_purchase import EMIPurchase
from backend.shared_logistics import SharedLogistics
from backend.storage_booking import StorageBooking
from backend.route_optimization import RouteOptimizer
from backend.export_gateway import ExportGateway
from backend.equipment_rental import EquipmentRental
from backend.fertilizer_price_comparison import FertilizerPriceComparison
from backend.secondhand_marketplace import SecondhandMarketplace
from backend.organic_marketplace import OrganicMarketplace
from backend.farmer_to_farmer_trade import FarmerToFarmerTrade
from backend.farmer_groups import FarmerGroupsManager
from backend.qa_forum import QAForumManager
from backend.mentorship import MentorshipManager
from backend.id_verification import IDVerificationManager
from backend.smart_contracts import SmartContractsManager
from backend.buyer_ratings import BuyerRatingsManager
from backend.organic_farming import OrganicFarmingAdvisory
from backend.water_conservation import WaterConservation
from backend.carbon_credits import CarbonCredits
from backend.admin_dashboard import AdminDashboard
from backend.fraud_detection import FraudDetection
from backend.multilanguage import MultiLanguageSupport
from backend.offline_sms import OfflineSMSSupport
from backend.users import UserManager

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')
app.secret_key = 'agrisuper_secret_key_2024'
app.config['JSON_SORT_KEYS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True

data_folder = 'data'
pricing_engine = PricingEngine()
subscription_model = SubscriptionModel()
contract_farming_engine = ContractFarmingEngine()
bulk_deals = BulkDealsEngine()
yield_prediction = YieldPredictionEngine()
crop_rotation = CropRotationEngine()
market_comparison = MarketComparisonEngine()
profit_analyzer = ProfitAnalyzerEngine()
disaster_alerts = DisasterAlertsEngine()
sowing_calendar = SowingCalendarEngine()
pest_alerts = PestAlertsEngine()
elearning_courses = ELearningCourses()
success_stories = SuccessStories()
voice_assistant = VoiceAssistant()
soil_knowledge = SoilKnowledge()
micro_loans = MicroLoans()
crop_insurance = CropInsurance()
digital_wallet = DigitalWallet()
emi_purchase = EMIPurchase()
shared_logistics = SharedLogistics()
storage_booking = StorageBooking()
route_optimization = RouteOptimizer()
export_gateway = ExportGateway()
equipment_rental = EquipmentRental()
fertilizer_price_comparison = FertilizerPriceComparison(data_folder)
secondhand_marketplace = SecondhandMarketplace(data_folder)
organic_marketplace = OrganicMarketplace(data_folder)
farmer_to_farmer_trade = FarmerToFarmerTrade(data_folder)
farmer_groups = FarmerGroupsManager(data_folder)
qa_forum = QAForumManager(data_folder)
mentorship = MentorshipManager(data_folder)
id_verification = IDVerificationManager(data_folder)
smart_contracts = SmartContractsManager(data_folder)
buyer_ratings = BuyerRatingsManager(data_folder)
organic_farming = OrganicFarmingAdvisory(data_folder)
water_conservation = WaterConservation(data_folder)
carbon_credits = CarbonCredits(data_folder)
admin_dashboard = AdminDashboard(data_folder)
fraud_detection = FraudDetection(data_folder)
multilanguage = MultiLanguageSupport(data_folder)
offline_sms = OfflineSMSSupport(data_folder)
user_manager = UserManager(data_folder)

@app.route('/')
def dashboard():
    """Main dashboard with all 41 features"""
    return render_template('dashboard.html')

@app.route('/categorized-dashboard')
def categorized_dashboard():
    return render_template('categorized_dashboard.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/weather-alerts')
def weather_alerts():
    return render_template('features/weather_alerts.html')

@app.route('/soil-health')
def soil_health():
    return render_template('features/soil_health.html')

@app.route('/crop-management')
def crop_management():
    return render_template('features/crop_management.html')

@app.route('/market-prices')
def market_prices():
    return render_template('features/market_prices.html')

@app.route('/equipment-management')
def equipment_management():
    return render_template('features/equipment_management.html')

@app.route('/community-forum')
def community_forum():
    # Initialize QA forum manager
    from backend.qa_forum import QAForumManager
    qa_manager = QAForumManager()
    
    # Get forum data
    questions = qa_manager.get_all_questions()
    categories = qa_manager.get_categories()
    forum_stats = qa_manager.get_forum_stats()
    
    # Count questions per category
    category_counts = {}
    for category in categories:
        category_counts[category] = len(qa_manager.get_all_questions(category=category))
    
    return render_template('features/community_forum.html', 
                           questions=questions, 
                           categories=categories, 
                           forum_stats=forum_stats,
                           category_counts=category_counts)

@app.route('/submit-question', methods=['POST'])
def submit_question():
    # Initialize QA forum manager
    from backend.qa_forum import QAForumManager
    qa_manager = QAForumManager()
    
    # Get form data
    title = request.form.get('title')
    category = request.form.get('category')
    question_text = request.form.get('question')
    tags = request.form.get('tags', '')
    
    # Process tags
    tags_list = [tag.strip() for tag in tags.split(',')] if tags else []
    
    # Get current user info
    user_id = session.get('user_id')
    username = session.get('username', 'Anonymous')
    
    if not user_id:
        flash('You must be logged in to post a question', 'error')
        return redirect(url_for('community_forum'))
    
    # Add the question
    success = qa_manager.add_question(title, category, question_text, user_id, username, tags_list)
    
    if success:
        flash('Your question has been posted successfully!', 'success')
    else:
        flash('There was an error posting your question. Please try again.', 'error')
    
    return redirect(url_for('community_forum'))

@app.route('/question/<question_id>')
def view_question(question_id):
    # Initialize QA forum manager
    from backend.qa_forum import QAForumManager
    qa_manager = QAForumManager()
    
    # Get question data
    question = qa_manager.get_question_by_id(question_id)
    
    if not question:
        flash('Question not found', 'error')
        return redirect(url_for('community_forum'))
    
    # Update view count
    qa_manager.increment_view_count(question_id)
    
    # Get related questions
    related_questions = qa_manager.get_related_questions(question_id, limit=5)
    
    return render_template('features/question_detail.html', 
                           question=question,
                           related_questions=related_questions)

@app.route('/submit-answer/<question_id>', methods=['POST'])
def submit_answer(question_id):
    # Initialize QA forum manager
    from backend.qa_forum import QAForumManager
    qa_manager = QAForumManager()
    
    # Get form data
    answer_text = request.form.get('answer')
    notify = 'notify' in request.form
    
    # Get current user info
    user_id = session.get('user_id')
    username = session.get('username', 'Anonymous')
    
    if not user_id:
        flash('You must be logged in to answer a question', 'error')
        return redirect(url_for('view_question', question_id=question_id))
    
    # Add the answer
    success = qa_manager.add_answer(question_id, answer_text, user_id, username)
    
    if success:
        flash('Your answer has been posted successfully!', 'success')
    else:
        flash('There was an error posting your answer. Please try again.', 'error')
    
    return redirect(url_for('view_question', question_id=question_id))
    
@app.route('/upvote-answer/<question_id>/<answer_id>', methods=['POST'])
def upvote_answer(question_id, answer_id):
    # Initialize QA forum manager
    from backend.qa_forum import QAForumManager
    qa_manager = QAForumManager()
    
    # Get current user info
    user_id = session.get('user_id')
    
    if not user_id:
        flash('You must be logged in to vote', 'error')
        return redirect(url_for('view_question', question_id=question_id))
    
    # Upvote the answer
    success = qa_manager.upvote_answer(question_id, answer_id, user_id)
    
    if success:
        flash('Vote recorded successfully!', 'success')
    else:
        flash('There was an error recording your vote. You may have already voted.', 'error')
    
    return redirect(url_for('view_question', question_id=question_id))
    
@app.route('/upvote-question/<question_id>', methods=['POST'])
def upvote_question(question_id):
    # Initialize QA forum manager
    from backend.qa_forum import QAForumManager
    qa_manager = QAForumManager()
    
    # Get current user info
    user_id = session.get('user_id')
    
    if not user_id:
        flash('You must be logged in to vote', 'error')
        return redirect(url_for('view_question', question_id=question_id))
    
    # Upvote the question
    success = qa_manager.upvote_question(question_id, user_id)
    
    if success:
        flash('Vote recorded successfully!', 'success')
    else:
        flash('There was an error recording your vote. You may have already voted.', 'error')
    
    return redirect(url_for('view_question', question_id=question_id))
    
@app.route('/share-question/<question_id>', methods=['GET'])
def share_question(question_id):
    # Initialize QA forum manager
    from backend.qa_forum import QAForumManager
    qa_manager = QAForumManager()
    
    # Get question data
    question = qa_manager.get_question_by_id(question_id)
    
    if not question:
        flash('Question not found', 'error')
        return redirect(url_for('community_forum'))
    
    # Generate share URL
    share_url = url_for('view_question', question_id=question_id, _external=True)
    
    # Generate email subject and body
    subject = f"Check out this farming question: {question['title']}"
    body = f"I thought you might be interested in this question from AgriSuper:\n\n{question['title']}\n\nQuestion: {question['question']}\n\nView and answer here: {share_url}"
    
    # Create mailto link
    mailto_link = f"mailto:?subject={subject}&body={body}"
    
    return redirect(mailto_link)

@app.route('/financial-management')
def financial_management():
    return render_template('features/financial_management.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'login' in request.form:
            username = request.form.get('username')
            password = request.form.get('password')
            
            user = user_manager.authenticate_user(username, password)
            if user:
                # In a real app, you would use Flask-Login or similar
                # For now, we'll use a simple session
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['role'] = user['role']
                return redirect(url_for('dashboard'))
            else:
                return render_template('auth/login_register.html', login_error="Invalid username or password")
        
        elif 'register' in request.form:
            # Get form data
            username = request.form.get('reg_username')
            email = request.form.get('reg_email')
            password = request.form.get('reg_password')
            confirm_password = request.form.get('reg_confirm_password')
            full_name = request.form.get('reg_full_name')
            phone = request.form.get('reg_phone', '')
            user_type = request.form.get('reg_user_type', 'farmer')
            
            # Validate form data
            if not all([username, email, password, full_name]):
                return render_template('auth/login_register.html', register_error="All required fields must be filled")
            
            if password != confirm_password:
                return render_template('auth/login_register.html', register_error="Passwords do not match")
            
            # Register the user
            result = user_manager.register_user(username, email, password, full_name, phone, user_type)
            if result['success']:
                return render_template('auth/login_register.html', register_success="Registration successful! Please login.")
            else:
                return render_template('auth/login_register.html', register_error=result['message'])
    
    return render_template('auth/login_register.html')

@app.route('/test-all-features')
def test_all_features():
    """Test endpoint to verify all 41 features are working"""
    test_results = {}
    
    try:
        # Test each feature
        test_results['pricing_engine'] = pricing_engine.test_connection()
        test_results['subscription_model'] = subscription_model.test_connection()
        test_results['contract_farming'] = contract_farming_engine.test_connection()
        test_results['bulk_deals'] = bulk_deals.test_connection()
        test_results['yield_prediction'] = yield_prediction.test_connection()
        test_results['crop_rotation'] = crop_rotation.test_connection()
        test_results['market_comparison'] = market_comparison.test_connection()
        test_results['profit_analyzer'] = profit_analyzer.test_connection()
        test_results['disaster_alerts'] = disaster_alerts.test_connection()
        test_results['sowing_calendar'] = sowing_calendar.test_connection()
        test_results['pest_alerts'] = pest_alerts.test_connection()
        test_results['elearning_courses'] = elearning_courses.test_connection()
        test_results['success_stories'] = success_stories.test_connection()
        test_results['voice_assistant'] = voice_assistant.test_connection()
        test_results['soil_knowledge'] = soil_knowledge.test_connection()
        test_results['micro_loans'] = micro_loans.test_connection()
        test_results['crop_insurance'] = crop_insurance.test_connection()
        test_results['digital_wallet'] = digital_wallet.test_connection()
        test_results['emi_purchase'] = emi_purchase.test_connection()
        test_results['shared_logistics'] = shared_logistics.test_connection()
        test_results['storage_booking'] = storage_booking.test_connection()
        test_results['route_optimization'] = route_optimization.test_connection()
        test_results['export_gateway'] = export_gateway.test_connection()
        test_results['equipment_rental'] = equipment_rental.test_connection()
        test_results['fertilizer_price_comparison'] = fertilizer_price_comparison.test_connection()
        test_results['secondhand_marketplace'] = secondhand_marketplace.test_connection()
        test_results['organic_marketplace'] = organic_marketplace.test_connection()
        test_results['farmer_to_farmer_trade'] = farmer_to_farmer_trade.test_connection()
        test_results['farmer_groups'] = farmer_groups.test_connection()
        test_results['qa_forum'] = qa_forum.test_connection()
        test_results['mentorship'] = mentorship.test_connection()
        test_results['id_verification'] = id_verification.test_connection()
        test_results['smart_contracts'] = smart_contracts.test_connection()
        test_results['buyer_ratings'] = buyer_ratings.test_connection()
        test_results['organic_farming'] = organic_farming.test_connection()
        test_results['water_conservation'] = water_conservation.test_connection()
        test_results['carbon_credits'] = carbon_credits.test_connection()
        test_results['admin_dashboard'] = admin_dashboard.test_connection()
        test_results['fraud_detection'] = fraud_detection.test_connection()
        test_results['multilanguage'] = multilanguage.test_connection()
        test_results['offline_sms'] = offline_sms.test_connection()
        
        return jsonify({
            'status': 'success',
            'message': 'All 41 features tested successfully',
            'results': test_results
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error testing features: {str(e)}',
            'results': test_results
        })

# Feature 1: Dynamic Pricing Engine
@app.route('/pricing-engine')
def pricing_engine_page():
    return render_template('features/pricing_engine.html')

@app.route('/api/pricing-engine/get-price', methods=['POST'])
def get_crop_price():
    data = request.json
    result = pricing_engine.get_dynamic_price(data['crop'], data['location'], data['quantity'])
    return jsonify(result)

# Feature 2: Subscription Model
@app.route('/subscription-model')
def subscription_model_page():
    return render_template('features/subscription_model.html')

@app.route('/api/subscription/create', methods=['POST'])
def create_subscription():
    data = request.json
    result = subscription_model.create_subscription(data)
    return jsonify(result)

# Feature 3: Contract Farming
@app.route('/contract-farming')
def contract_farming_page():
    return render_template('features/contract_farming.html')

@app.route('/api/contract-farming/create', methods=['POST'])
def create_contract():
    data = request.json
    result = contract_farming_engine.create_contract(data)
    return jsonify(result)

# Feature 4: Bulk Deals
@app.route('/bulk-deals')
def bulk_deals_page():
    return render_template('features/bulk_deals.html')

@app.route('/api/bulk-deals/join-pool', methods=['POST'])
def join_deal_pool():
    data = request.json
    result = bulk_deals.join_pool(data)
    return jsonify(result)

# Feature 5: Yield Prediction
@app.route('/yield-prediction')
def yield_prediction_page():
    return render_template('features/yield_prediction.html')

@app.route('/api/yield-prediction/predict', methods=['POST'])
def predict_yield():
    data = request.json
    result = yield_prediction.predict_yield(data)
    return jsonify(result)

# Feature 6: Crop Rotation
@app.route('/crop-rotation')
def crop_rotation_page():
    return render_template('features/crop_rotation.html')

@app.route('/api/crop-rotation/suggest', methods=['POST'])
def suggest_rotation():
    data = request.json
    result = crop_rotation.suggest_rotation(data)
    return jsonify(result)

# Feature 7: Market Comparison
@app.route('/market-comparison')
def market_comparison_page():
    return render_template('features/market_comparison.html')

@app.route('/api/market-comparison/compare', methods=['POST'])
def compare_markets():
    data = request.json
    result = market_comparison.compare_markets(data)
    return jsonify(result)

# Feature 8: Profit Analyzer
@app.route('/profit-analyzer')
def profit_analyzer_page():
    return render_template('features/profit_analyzer.html')

@app.route('/api/profit-analyzer/calculate', methods=['POST'])
def calculate_profit():
    data = request.json
    result = profit_analyzer.calculate_profit(data)
    return jsonify(result)

# Feature 9: Disaster Alerts
@app.route('/disaster-alerts')
def disaster_alerts_page():
    return render_template('features/disaster_alerts.html')

@app.route('/quality_certification')
def quality_certification():
    return render_template('features/quality_certification.html')

@app.route('/api/disaster-alerts/get-alerts', methods=['GET'])
def get_disaster_alerts():
    location = request.args.get('location', 'all')
    result = disaster_alerts.get_alerts(location)
    return jsonify(result)

# Feature 10: Sowing Calendar
@app.route('/sowing-calendar')
def sowing_calendar_page():
    return render_template('features/sowing_calendar.html')

@app.route('/api/sowing-calendar/optimal-dates', methods=['POST'])
def get_optimal_dates():
    data = request.json
    result = sowing_calendar.get_optimal_dates(data)
    return jsonify(result)

# Feature 11: Pest Alerts
@app.route('/pest-alerts')
def pest_alerts_page():
    return render_template('features/pest_alerts.html')

@app.route('/api/pest-alerts/get-alerts', methods=['GET'])
def get_pest_alerts():
    location = request.args.get('location', 'all')
    result = pest_alerts.get_alerts(location)
    return jsonify(result)

# Feature 12: E-Learning Courses
@app.route('/elearning-courses')
def elearning_courses_page():
    return render_template('features/elearning_courses.html')

@app.route('/api/elearning/courses', methods=['GET'])
def get_courses():
    filters = request.args.to_dict()
    result = elearning_courses.get_courses(filters)
    return jsonify(result)

@app.route('/api/elearning/course/<course_id>', methods=['GET'])
def get_course_details(course_id):
    result = elearning_courses.get_course_details(course_id)
    return jsonify(result)

@app.route('/api/elearning/enroll', methods=['POST'])
def enroll_course():
    data = request.json
    result = elearning_courses.enroll_course(data)
    return jsonify(result)

@app.route('/api/elearning/progress', methods=['POST'])
def update_progress():
    data = request.json
    result = elearning_courses.update_progress(data)
    return jsonify(result)

@app.route('/api/elearning/quiz-submit', methods=['POST'])
def submit_quiz():
    data = request.json
    result = elearning_courses.submit_quiz(data)
    return jsonify(result)

@app.route('/api/elearning/certificate/<course_id>', methods=['GET'])
def generate_certificate(course_id):
    user_id = request.args.get('user_id')
    result = elearning_courses.generate_certificate(course_id, user_id)
    return jsonify(result)

# Feature 13: Success Stories
@app.route('/success-stories')
def success_stories_page():
    return render_template('features/success_stories.html')

@app.route('/api/success-stories/stories', methods=['GET'])
def get_stories():
    filters = request.args.to_dict()
    result = success_stories.get_stories(filters)
    return jsonify(result)

@app.route('/api/success-stories/story/<story_id>', methods=['GET'])
def get_story_details(story_id):
    result = success_stories.get_story_details(story_id)
    return jsonify(result)

@app.route('/api/success-stories/submit', methods=['POST'])
def submit_story():
    data = request.json
    result = success_stories.submit_story(data)
    return jsonify(result)

@app.route('/api/success-stories/vote', methods=['POST'])
def vote_story():
    data = request.json
    result = success_stories.vote_story(data)
    return jsonify(result)

# Feature 14: AI Voice Assistant
@app.route('/voice-assistant')
def voice_assistant_page():
    return render_template('features/voice_assistant.html')

@app.route('/api/voice/query', methods=['POST'])
def voice_query():
    data = request.json
    result = voice_assistant.process_query(data)
    return jsonify(result)

@app.route('/api/voice/languages', methods=['GET'])
def get_languages():
    result = voice_assistant.get_supported_languages()
    return jsonify(result)

# Feature 15: Digital Soil Knowledge
@app.route('/soil-knowledge')
def soil_knowledge_page():
    return render_template('features/soil_knowledge.html')

@app.route('/api/soil/analyze', methods=['POST'])
def analyze_soil():
    data = request.json
    result = soil_knowledge.analyze_soil(data)
    return jsonify(result)

@app.route('/api/soil/recommendations', methods=['POST'])
def get_soil_recommendations():
    data = request.json
    result = soil_knowledge.get_recommendations(data)
    return jsonify(result)

@app.route('/api/soil/upload-report', methods=['POST'])
def upload_soil_report():
    data = request.json
    result = soil_knowledge.parse_soil_report(data)
    return jsonify(result)

# Feature 16: Micro-Loan Marketplace
@app.route('/micro-loans')
def micro_loans_page():
    return render_template('features/micro_loans.html')

@app.route('/api/loans/products', methods=['GET'])
def get_loan_products():
    filters = request.args.to_dict()
    result = micro_loans.get_loan_products(filters)
    return jsonify(result)

@app.route('/api/loans/eligibility', methods=['POST'])
def check_eligibility():
    data = request.json
    result = micro_loans.check_eligibility(data)
    return jsonify(result)

@app.route('/api/loans/apply', methods=['POST'])
def apply_loan():
    data = request.json
    result = micro_loans.apply_loan(data)
    return jsonify(result)

@app.route('/api/loans/status/<application_id>', methods=['GET'])
def get_loan_status(application_id):
    result = micro_loans.get_loan_status(application_id)
    return jsonify(result)

# Feature 17: Crop Insurance
@app.route('/crop-insurance')
def crop_insurance_page():
    return render_template('features/crop_insurance.html')

@app.route('/api/insurance/policies', methods=['GET'])
def get_insurance_policies():
    filters = request.args.to_dict()
    result = crop_insurance.get_policies(filters)
    return jsonify(result)

@app.route('/api/insurance/quote', methods=['POST'])
def get_insurance_quote():
    data = request.json
    result = crop_insurance.get_quote(data)
    return jsonify(result)

@app.route('/api/insurance/purchase', methods=['POST'])
def purchase_insurance():
    data = request.json
    result = crop_insurance.purchase_policy(data)
    return jsonify(result)

@app.route('/api/insurance/claim', methods=['POST'])
def file_claim():
    data = request.json
    result = crop_insurance.file_claim(data)
    return jsonify(result)

@app.route('/api/insurance/claim-status/<claim_id>', methods=['GET'])
def get_claim_status(claim_id):
    result = crop_insurance.get_claim_status(claim_id)
    return jsonify(result)

# Feature 18: Digital Wallet
@app.route('/digital-wallet')
def digital_wallet_page():
    return render_template('features/digital_wallet.html')

@app.route('/api/wallet/balance/<user_id>', methods=['GET'])
def get_wallet_balance(user_id):
    result = digital_wallet.get_balance(user_id)
    return jsonify(result)

@app.route('/api/wallet/add-money', methods=['POST'])
def add_money():
    data = request.json
    result = digital_wallet.add_money(data)
    return jsonify(result)

@app.route('/api/wallet/transfer', methods=['POST'])
def transfer_money():
    data = request.json
    result = digital_wallet.transfer_money(data)
    return jsonify(result)

@app.route('/api/wallet/transactions/<user_id>', methods=['GET'])
def get_transactions(user_id):
    filters = request.args.to_dict()
    result = digital_wallet.get_transactions(user_id, filters)
    return jsonify(result)

# Feature 19: EMI Purchase
@app.route('/emi-purchase')
def emi_purchase_page():
    return render_template('features/emi_purchase.html')

@app.route('/api/emi/plans/<product_id>', methods=['GET'])
def get_emi_plans(product_id):
    result = emi_purchase.get_emi_plans(product_id)
    return jsonify(result)

@app.route('/api/emi/calculate', methods=['POST'])
def calculate_emi():
    data = request.json
    result = emi_purchase.calculate_emi(data)
    return jsonify(result)

@app.route('/api/emi/purchase', methods=['POST'])
def purchase_on_emi():
    data = request.json
    result = emi_purchase.purchase_on_emi(data)
    return jsonify(result)

@app.route('/api/emi/payments/<emi_id>', methods=['GET'])
def get_emi_payments(emi_id):
    result = emi_purchase.get_payment_schedule(emi_id)
    return jsonify(result)

# Feature 20: Shared Logistics
@app.route('/shared-logistics')
def shared_logistics_page():
    return render_template('features/shared_logistics.html')

@app.route('/api/logistics/post-shipment', methods=['POST'])
def post_shipment():
    data = request.json
    result = shared_logistics.post_shipment(data)
    return jsonify(result)

@app.route('/api/logistics/find-matches', methods=['POST'])
def find_matches():
    data = request.json
    result = shared_logistics.find_matches(data)
    return jsonify(result)

@app.route('/api/logistics/join-shipment', methods=['POST'])
def join_shipment():
    data = request.json
    result = shared_logistics.join_shipment(data)
    return jsonify(result)

@app.route('/api/logistics/track/<shipment_id>', methods=['GET'])
def track_shipment(shipment_id):
    result = shared_logistics.track_shipment(shipment_id)
    return jsonify(result)

# Feature 21: Storage Booking
@app.route('/storage-booking')
def storage_booking_page():
    return render_template('features/storage_booking.html')

@app.route('/api/storage/warehouses', methods=['GET'])
def get_warehouses():
    filters = request.args.to_dict()
    result = storage_booking.get_warehouses(filters)
    return jsonify(result)

@app.route('/api/storage/availability', methods=['POST'])
def check_availability():
    data = request.json
    result = storage_booking.check_availability(data)
    return jsonify(result)

@app.route('/api/storage/book', methods=['POST'])
def book_storage():
    data = request.json
    result = storage_booking.book_storage(data)
    return jsonify(result)

@app.route('/api/storage/bookings/<user_id>', methods=['GET'])
def get_bookings(user_id):
    result = storage_booking.get_user_bookings(user_id)
    return jsonify(result)

# Feature 22: Route Optimization
@app.route('/route-optimization')
def route_optimization_page():
    return render_template('features/route_optimization.html')

@app.route('/api/route/optimize', methods=['POST'])
def optimize_route():
    data = request.json
    result = route_optimization.optimize_route(data)
    return jsonify(result)

@app.route('/api/route/calculate-cost', methods=['POST'])
def calculate_route_cost():
    data = request.json
    result = route_optimization.calculate_cost(data)
    return jsonify(result)

# Feature 23: Export Gateway
@app.route('/export-gateway')
def export_gateway_page():
    return render_template('features/export_gateway.html')

@app.route('/api/export/countries', methods=['GET'])
def get_export_countries():
    result = export_gateway.get_countries()
    return jsonify(result)

@app.route('/api/export/requirements', methods=['POST'])
def get_export_requirements():
    data = request.json
    result = export_gateway.get_requirements(data)
    return jsonify(result)

@app.route('/api/export/documentation', methods=['POST'])
def generate_export_docs():
    data = request.json
    result = export_gateway.generate_documentation(data)
    return jsonify(result)

# Feature 24: Equipment Rental
@app.route('/equipment-rental')
def equipment_rental_page():
    return render_template('features/equipment_rental.html')

@app.route('/api/equipment/search', methods=['GET'])
def search_equipment():
    filters = request.args.to_dict()
    result = equipment_rental.search_equipment(filters)
    return jsonify(result)

@app.route('/api/equipment/rent', methods=['POST'])
def rent_equipment():
    data = request.json
    result = equipment_rental.rent_equipment(data)
    return jsonify(result)

@app.route('/api/equipment/availability', methods=['POST'])
def check_equipment_availability():
    data = request.json
    result = equipment_rental.check_availability(data)
    return jsonify(result)

# Feature 25: Fertilizer Price Comparison
@app.route('/fertilizer-price-comparison')
def fertilizer_price_comparison_page():
    return render_template('features/fertilizer_price_comparison.html')

@app.route('/api/fertilizer/compare', methods=['POST'])
def compare_fertilizer_prices():
    data = request.json
    result = fertilizer_price_comparison.compare_prices(data)
    return jsonify(result)

@app.route('/api/fertilizer/alerts', methods=['POST'])
def set_price_alert():
    data = request.json
    result = fertilizer_price_comparison.set_price_alert(data)
    return jsonify(result)

# Feature 26: Secondhand Marketplace
@app.route('/secondhand-marketplace')
def secondhand_marketplace_page():
    return render_template('features/secondhand_marketplace.html')

@app.route('/api/secondhand/listings', methods=['GET'])
def get_secondhand_listings():
    filters = request.args.to_dict()
    result = secondhand_marketplace.get_listings(filters)
    return jsonify(result)

@app.route('/api/secondhand/post', methods=['POST'])
def post_secondhand_listing():
    data = request.json
    result = secondhand_marketplace.post_listing(data)
    return jsonify(result)

@app.route('/api/secondhand/buy', methods=['POST'])
def buy_secondhand_item():
    data = request.json
    result = secondhand_marketplace.buy_item(data)
    return jsonify(result)

# Feature 27: Organic Marketplace
@app.route('/organic-marketplace')
def organic_marketplace_page():
    return render_template('features/organic_marketplace.html')

@app.route('/api/organic/products', methods=['GET'])
def get_organic_products():
    filters = request.args.to_dict()
    result = organic_marketplace.get_products(filters)
    return jsonify(result)

@app.route('/api/organic/verify', methods=['POST'])
def verify_organic_certification():
    data = request.json
    result = organic_marketplace.verify_certification(data)
    return jsonify(result)

@app.route('/api/organic/purchase', methods=['POST'])
def purchase_organic_product():
    data = request.json
    result = organic_marketplace.purchase_product(data)
    return jsonify(result)

# Feature 28: Farmer-to-Farmer Trade
@app.route('/farmer-to-farmer-trade')
def farmer_to_farmer_trade_page():
    return render_template('features/farmer_to_farmer_trade.html')

@app.route('/api/farmer-trade/listings', methods=['GET'])
def get_farmer_trade_listings():
    filters = request.args.to_dict()
    result = farmer_to_farmer_trade.get_listings(filters)
    return jsonify(result)

@app.route('/api/farmer-trade/post', methods=['POST'])
def post_farmer_trade():
    data = request.json
    result = farmer_to_farmer_trade.post_trade(data)
    return jsonify(result)

@app.route('/api/farmer-trade/negotiate', methods=['POST'])
def negotiate_trade():
    data = request.json
    result = farmer_to_farmer_trade.negotiate(data)
    return jsonify(result)

# Feature 29: Farmer Groups & Cooperatives
@app.route('/farmer-groups')
def farmer_groups_page():
    return render_template('features/farmer_groups.html')

@app.route('/api/groups/list', methods=['GET'])
def get_farmer_groups():
    filters = request.args.to_dict()
    result = farmer_groups.get_groups(filters)
    return jsonify(result)

@app.route('/api/groups/join', methods=['POST'])
def join_farmer_group():
    data = request.json
    result = farmer_groups.join_group(data)
    return jsonify(result)

@app.route('/api/groups/create', methods=['POST'])
def create_farmer_group():
    data = request.json
    result = farmer_groups.create_group(data)
    return jsonify(result)

# Feature 30: Q&A Forum with Experts
@app.route('/qa-forum')
def qa_forum_page():
    return render_template('features/qa_forum.html')

@app.route('/api/forum/questions', methods=['GET'])
def get_forum_questions():
    filters = request.args.to_dict()
    result = qa_forum.get_questions(filters)
    return jsonify(result)

@app.route('/api/forum/ask', methods=['POST'])
def ask_question():
    data = request.json
    result = qa_forum.ask_question(data)
    return jsonify(result)

@app.route('/api/forum/answer', methods=['POST'])
def answer_question():
    data = request.json
    result = qa_forum.answer_question(data)
    return jsonify(result)

# Feature 31: Mentorship Program
@app.route('/mentorship')
def mentorship_page():
    return render_template('features/mentorship.html')

@app.route('/api/mentorship/mentors', methods=['GET'])
def get_mentors():
    filters = request.args.to_dict()
    result = mentorship.get_mentors(filters)
    return jsonify(result)

@app.route('/api/mentorship/request', methods=['POST'])
def request_mentorship():
    data = request.json
    result = mentorship.request_mentorship(data)
    return jsonify(result)

@app.route('/api/mentorship/sessions', methods=['GET'])
def get_mentorship_sessions():
    user_id = request.args.get('user_id')
    result = mentorship.get_sessions(user_id)
    return jsonify(result)

# Feature 32: ID Verification
@app.route('/id-verification')
def id_verification_page():
    return render_template('features/id_verification.html')

@app.route('/api/verification/submit', methods=['POST'])
def submit_verification():
    data = request.json
    result = id_verification.submit_verification(data)
    return jsonify(result)

@app.route('/api/verification/status/<user_id>', methods=['GET'])
def get_verification_status(user_id):
    result = id_verification.get_status(user_id)
    return jsonify(result)

# Feature 33: Smart Contract Payments
@app.route('/smart-contracts')
def smart_contracts_page():
    return render_template('features/smart_contracts.html')

@app.route('/api/contracts/create', methods=['POST'])
def create_smart_contract():
    data = request.json
    result = smart_contracts.create_contract(data)
    return jsonify(result)

@app.route('/api/contracts/execute', methods=['POST'])
def execute_contract():
    data = request.json
    result = smart_contracts.execute_contract(data)
    return jsonify(result)

@app.route('/api/contracts/status/<contract_id>', methods=['GET'])
def get_contract_status(contract_id):
    result = smart_contracts.get_status(contract_id)
    return jsonify(result)

# Feature 34: Buyer Rating System
@app.route('/buyer-ratings')
def buyer_ratings_page():
    return render_template('features/buyer_ratings.html')

@app.route('/api/ratings/submit', methods=['POST'])
def submit_rating():
    data = request.json
    result = buyer_ratings.submit_rating(data)
    return jsonify(result)

@app.route('/api/ratings/buyer/<buyer_id>', methods=['GET'])
def get_buyer_ratings(buyer_id):
    result = buyer_ratings.get_ratings(buyer_id)
    return jsonify(result)

# Feature 35: Organic Farming Advisory
@app.route('/organic-farming')
def organic_farming_page():
    return render_template('features/organic_farming.html')

@app.route('/api/organic-farming/guidelines', methods=['POST'])
def get_organic_guidelines():
    data = request.json
    result = organic_farming.get_guidelines(data)
    return jsonify(result)

@app.route('/api/organic-farming/certification', methods=['POST'])
def get_certification_info():
    data = request.json
    result = organic_farming.get_certification_info(data)
    return jsonify(result)

# Feature 36: Water Conservation
@app.route('/water-conservation')
def water_conservation_page():
    return render_template('features/water_conservation.html')

@app.route('/api/water/techniques', methods=['POST'])
def get_water_techniques():
    data = request.json
    result = water_conservation.get_techniques(data)
    return jsonify(result)

@app.route('/api/water/calculate-savings', methods=['POST'])
def calculate_water_savings():
    data = request.json
    result = water_conservation.calculate_savings(data)
    return jsonify(result)

# Feature 37: Carbon Credits
@app.route('/carbon-credits')
def carbon_credits_page():
    return render_template('features/carbon_credits.html')

@app.route('/api/carbon/calculate', methods=['POST'])
def calculate_carbon_credits():
    data = request.json
    result = carbon_credits.calculate_credits(data)
    return jsonify(result)

@app.route('/api/carbon/marketplace', methods=['GET'])
def get_carbon_marketplace():
    result = carbon_credits.get_marketplace()
    return jsonify(result)

@app.route('/api/carbon/sell', methods=['POST'])
def sell_carbon_credits():
    data = request.json
    result = carbon_credits.sell_credits(data)
    return jsonify(result)

# Feature 38: Admin Dashboard
@app.route('/admin-dashboard')
def admin_dashboard_page():
    return render_template('features/admin_dashboard.html')

@app.route('/api/admin/analytics', methods=['GET'])
def get_admin_analytics():
    result = admin_dashboard.get_analytics()
    return jsonify(result)

@app.route('/api/admin/users', methods=['GET'])
def get_admin_users():
    filters = request.args.to_dict()
    result = admin_dashboard.get_users(filters)
    return jsonify(result)

@app.route('/api/admin/moderate', methods=['POST'])
def moderate_content():
    data = request.json
    result = admin_dashboard.moderate_content(data)
    return jsonify(result)

# Feature 39: Fraud Detection
@app.route('/fraud-detection')
def fraud_detection_page():
    return render_template('features/fraud_detection.html')

@app.route('/api/fraud/analyze', methods=['POST'])
def analyze_fraud():
    data = request.json
    result = fraud_detection.analyze_transaction(data)
    return jsonify(result)

@app.route('/api/fraud/report', methods=['POST'])
def report_fraud():
    data = request.json
    result = fraud_detection.report_fraud(data)
    return jsonify(result)

# Feature 40: Multi-language Support
@app.route('/multilanguage')
def multilanguage_page():
    return render_template('features/multilanguage.html')

@app.route('/api/language/translate', methods=['POST'])
def translate_content():
    data = request.json
    result = multilanguage.translate(data)
    return jsonify(result)

@app.route('/api/language/supported', methods=['GET'])
def get_supported_languages():
    result = multilanguage.get_supported_languages()
    return jsonify(result)

# Feature 41: Offline/SMS Support
@app.route('/offline-sms')
def offline_sms_page():
    return render_template('features/offline_sms.html')

@app.route('/api/sms/send', methods=['POST'])
def send_sms():
    data = request.json
    result = offline_sms.send_sms(data)
    return jsonify(result)

@app.route('/api/sms/subscribe', methods=['POST'])
def subscribe_sms():
    data = request.json
    result = offline_sms.subscribe(data)
    return jsonify(result)

@app.route('/api/sms/commands', methods=['GET'])
def get_sms_commands():
    result = offline_sms.get_commands()
    return jsonify(result)





if __name__ == '__main__':
    try:
        # Ensure data directory exists
        if not os.path.exists('data'):
            os.makedirs('data')
        
        # Ensure all required data files exist
        for module in [pricing_engine, subscription_model, contract_farming_engine]:
            if hasattr(module, 'load_data'):
                module.load_data()
        
        print("Starting AgriSuper App server...")
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting server: {str(e)}")
        raise
