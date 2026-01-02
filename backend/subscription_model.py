import json
import uuid
from datetime import datetime, timedelta
import random

class SubscriptionModel:
    def __init__(self, data_folder='data'):
        self.subscriptions = self._load_sample_subscriptions()
        self.buyers = self._load_sample_buyers()
        self.subscription_plans = self._load_subscription_plans()
        self.loyalty_programs = self._load_loyalty_programs()
    
    def _load_sample_subscriptions(self):
        """Load sample subscription data"""
        return {
            'active_subscriptions': [
                {
                    'id': 'SUB001',
                    'buyer_id': 'BUY001',
                    'buyer_name': 'Green Valley Restaurant',
                    'plan': 'Premium Weekly',
                    'crops': ['Tomato', 'Onion', 'Potato', 'Cabbage'],
                    'quantities': {'Tomato': 50, 'Onion': 30, 'Potato': 40, 'Cabbage': 20},
                    'delivery_schedule': 'Every Monday',
                    'start_date': '2024-01-15',
                    'status': 'active',
                    'total_value': 15000,
                    'discount_applied': 12
                },
                {
                    'id': 'SUB002',
                    'buyer_id': 'BUY002',
                    'buyer_name': 'Fresh Mart Supermarket',
                    'plan': 'Business Monthly',
                    'crops': ['Rice', 'Wheat', 'Pulses', 'Vegetables'],
                    'quantities': {'Rice': 500, 'Wheat': 300, 'Pulses': 100, 'Vegetables': 200},
                    'delivery_schedule': '1st and 15th of month',
                    'start_date': '2024-02-01',
                    'status': 'active',
                    'total_value': 85000,
                    'discount_applied': 18
                }
            ]
        }
    
    def _load_sample_buyers(self):
        """Load comprehensive buyer database"""
        return {
            'restaurants': [
                {
                    'id': 'BUY001',
                    'name': 'Green Valley Restaurant',
                    'type': 'Fine Dining',
                    'location': 'Mumbai',
                    'capacity': '200 covers/day',
                    'cuisine': 'Multi-cuisine',
                    'requirements': ['Organic vegetables', 'Premium quality', 'Daily delivery'],
                    'budget_range': '10,000-20,000/week',
                    'contact': '+91-9876543210'
                },
                {
                    'id': 'BUY003',
                    'name': 'Spice Garden',
                    'type': 'Casual Dining',
                    'location': 'Delhi',
                    'capacity': '150 covers/day',
                    'cuisine': 'North Indian',
                    'requirements': ['Fresh spices', 'Seasonal vegetables', 'Flexible delivery'],
                    'budget_range': '8,000-15,000/week',
                    'contact': '+91-9876543211'
                }
            ],
            'retailers': [
                {
                    'id': 'BUY002',
                    'name': 'Fresh Mart Supermarket',
                    'type': 'Supermarket Chain',
                    'location': 'Bangalore',
                    'stores': 15,
                    'customer_base': '50,000+ monthly',
                    'requirements': ['Bulk quantities', 'Consistent quality', 'Competitive pricing'],
                    'budget_range': '50,000-1,00,000/month',
                    'contact': '+91-9876543212'
                },
                {
                    'id': 'BUY004',
                    'name': 'Organic Bazaar',
                    'type': 'Specialty Store',
                    'location': 'Pune',
                    'stores': 3,
                    'customer_base': '5,000+ monthly',
                    'requirements': ['Certified organic', 'Traceability', 'Premium packaging'],
                    'budget_range': '20,000-40,000/month',
                    'contact': '+91-9876543213'
                }
            ],
            'hotels': [
                {
                    'id': 'BUY005',
                    'name': 'Grand Palace Hotel',
                    'type': '5-Star Hotel',
                    'location': 'Goa',
                    'rooms': 200,
                    'restaurants': 4,
                    'requirements': ['Gourmet vegetables', 'Exotic fruits', 'Daily delivery'],
                    'budget_range': '30,000-50,000/week',
                    'contact': '+91-9876543214'
                }
            ]
        }
    
    def _load_subscription_plans(self):
        """Load subscription plan options"""
        return {
            'weekly_plans': [
                {
                    'name': 'Basic Weekly',
                    'duration': '1 week',
                    'min_order': 1000,
                    'discount': 5,
                    'features': ['Weekly delivery', 'Basic support', 'Standard quality'],
                    'price_per_kg': 'Market rate - 5%'
                },
                {
                    'name': 'Premium Weekly',
                    'duration': '1 week',
                    'min_order': 2000,
                    'discount': 12,
                    'features': ['Weekly delivery', 'Priority support', 'Premium quality', 'Flexible timing'],
                    'price_per_kg': 'Market rate - 12%'
                }
            ],
            'monthly_plans': [
                {
                    'name': 'Standard Monthly',
                    'duration': '1 month',
                    'min_order': 5000,
                    'discount': 15,
                    'features': ['Bi-weekly delivery', 'Dedicated manager', 'Quality guarantee'],
                    'price_per_kg': 'Market rate - 15%'
                },
                {
                    'name': 'Business Monthly',
                    'duration': '1 month',
                    'min_order': 10000,
                    'discount': 18,
                    'features': ['Custom delivery schedule', 'Bulk discounts', 'Priority processing'],
                    'price_per_kg': 'Market rate - 18%'
                }
            ],
            'quarterly_plans': [
                {
                    'name': 'Enterprise Quarterly',
                    'duration': '3 months',
                    'min_order': 50000,
                    'discount': 25,
                    'features': ['Custom crop planning', 'Dedicated supply chain', 'Price protection'],
                    'price_per_kg': 'Market rate - 25%'
                }
            ]
        }
    
    def _load_loyalty_programs(self):
        """Load loyalty program details"""
        return {
            'bronze': {
                'threshold': 10000,
                'benefits': ['5% additional discount', 'Priority customer support'],
                'duration': '6 months'
            },
            'silver': {
                'threshold': 50000,
                'benefits': ['8% additional discount', 'Free quality testing', 'Flexible payment terms'],
                'duration': '1 year'
            },
            'gold': {
                'threshold': 100000,
                'benefits': ['12% additional discount', 'Custom packaging', 'Dedicated account manager'],
                'duration': '2 years'
            },
            'platinum': {
                'threshold': 500000,
                'benefits': ['15% additional discount', 'Exclusive varieties access', 'Price protection guarantee'],
                'duration': 'Lifetime'
            }
        }
    
    def create_subscription(self, data):
        """Create new subscription"""
        try:
            subscription_id = f"SUB{random.randint(1000, 9999)}"
            
            # Validate buyer information
            buyer_info = self._validate_buyer(data.get('buyer_id'))
            if not buyer_info:
                return {
                    'success': False,
                    'message': 'Invalid buyer information'
                }
            
            # Calculate subscription details
            subscription_details = self._calculate_subscription_details(data)
            
            # Generate delivery schedule
            delivery_schedule = self._generate_delivery_schedule(data.get('plan_type'), data.get('start_date'))
            
            # Apply loyalty benefits
            loyalty_benefits = self._apply_loyalty_benefits(data.get('buyer_id'), subscription_details['total_value'])
            
            subscription = {
                'id': subscription_id,
                'buyer_info': buyer_info,
                'plan_details': subscription_details,
                'delivery_schedule': delivery_schedule,
                'loyalty_benefits': loyalty_benefits,
                'created_at': datetime.now().isoformat(),
                'status': 'pending_confirmation'
            }
            
            return {
                'success': True,
                'data': subscription,
                'message': 'Subscription created successfully'
            }
        
        except Exception as e:
            return {
                'success': False,
                'message': f'Error creating subscription: {str(e)}'
            }
    
    def _validate_buyer(self, buyer_id):
        """Validate and get buyer information"""
        # Search in all buyer categories
        for category in self.buyers.values():
            for buyer in category:
                if buyer['id'] == buyer_id:
                    return buyer
        
        # Return sample buyer if not found (for demo)
        return {
            'id': buyer_id,
            'name': 'Sample Buyer',
            'type': 'Restaurant',
            'location': 'Mumbai',
            'contact': '+91-9876543210'
        }
    
    def _calculate_subscription_details(self, data):
        """Calculate subscription pricing and details"""
        plan_type = data.get('plan_type', 'weekly')
        crops = data.get('crops', [])
        quantities = data.get('quantities', {})
        
        # Get plan details
        plan_info = None
        for plan_category in self.subscription_plans.values():
            for plan in plan_category:
                if plan['name'].lower().replace(' ', '_') == plan_type.lower():
                    plan_info = plan
                    break
        
        if not plan_info:
            plan_info = self.subscription_plans['weekly_plans'][0]  # Default plan
        
        # Calculate total value
        total_value = 0
        crop_details = []
        
        for crop in crops:
            quantity = quantities.get(crop, 0)
            base_price = random.randint(20, 100)  # Price per kg
            crop_total = quantity * base_price
            total_value += crop_total
            
            crop_details.append({
                'crop': crop,
                'quantity_kg': quantity,
                'price_per_kg': base_price,
                'total_amount': crop_total
            })
        
        # Apply plan discount
        discount_amount = total_value * (plan_info['discount'] / 100)
        final_amount = total_value - discount_amount
        
        return {
            'plan_info': plan_info,
            'crop_details': crop_details,
            'subtotal': total_value,
            'discount_percent': plan_info['discount'],
            'discount_amount': discount_amount,
            'final_amount': final_amount,
            'payment_terms': self._get_payment_terms(plan_info['name'])
        }
    
    def _generate_delivery_schedule(self, plan_type, start_date):
        """Generate delivery schedule based on plan"""
        schedule = []
        start = datetime.strptime(start_date, '%Y-%m-%d') if isinstance(start_date, str) else start_date
        
        if 'weekly' in plan_type.lower():
            # Weekly deliveries for next 12 weeks
            for i in range(12):
                delivery_date = start + timedelta(weeks=i)
                schedule.append({
                    'delivery_date': delivery_date.strftime('%Y-%m-%d'),
                    'status': 'scheduled',
                    'time_slot': '9:00 AM - 12:00 PM'
                })
        
        elif 'monthly' in plan_type.lower():
            # Bi-weekly deliveries for next 6 months
            for i in range(12):  # 12 deliveries over 6 months
                delivery_date = start + timedelta(weeks=i*2)
                schedule.append({
                    'delivery_date': delivery_date.strftime('%Y-%m-%d'),
                    'status': 'scheduled',
                    'time_slot': '10:00 AM - 2:00 PM'
                })
        
        elif 'quarterly' in plan_type.lower():
            # Weekly deliveries for next 3 months
            for i in range(12):
                delivery_date = start + timedelta(weeks=i)
                schedule.append({
                    'delivery_date': delivery_date.strftime('%Y-%m-%d'),
                    'status': 'scheduled',
                    'time_slot': 'Flexible'
                })
        
        return schedule
    
    def _apply_loyalty_benefits(self, buyer_id, total_value):
        """Apply loyalty program benefits"""
        # Simulate buyer's total purchase history
        total_purchases = random.randint(5000, 200000)
        
        loyalty_tier = 'bronze'
        if total_purchases >= 500000:
            loyalty_tier = 'platinum'
        elif total_purchases >= 100000:
            loyalty_tier = 'gold'
        elif total_purchases >= 50000:
            loyalty_tier = 'silver'
        
        tier_info = self.loyalty_programs[loyalty_tier]
        
        # Calculate additional discount
        additional_discount = 0
        if 'additional discount' in tier_info['benefits'][0]:
            additional_discount = int(tier_info['benefits'][0].split('%')[0])
        
        return {
            'tier': loyalty_tier.title(),
            'total_purchases': total_purchases,
            'benefits': tier_info['benefits'],
            'additional_discount_percent': additional_discount,
            'additional_discount_amount': total_value * (additional_discount / 100)
        }
    
    def _get_payment_terms(self, plan_name):
        """Get payment terms based on plan"""
        terms = {
            'Basic Weekly': {
                'advance_payment': 100,
                'payment_cycle': 'Weekly',
                'credit_period': 0,
                'late_fee': '2% per week'
            },
            'Premium Weekly': {
                'advance_payment': 50,
                'payment_cycle': 'Weekly',
                'credit_period': 3,
                'late_fee': '1.5% per week'
            },
            'Standard Monthly': {
                'advance_payment': 30,
                'payment_cycle': 'Monthly',
                'credit_period': 7,
                'late_fee': '1% per week'
            },
            'Business Monthly': {
                'advance_payment': 25,
                'payment_cycle': 'Monthly',
                'credit_period': 15,
                'late_fee': '0.5% per week'
            },
            'Enterprise Quarterly': {
                'advance_payment': 20,
                'payment_cycle': 'Monthly',
                'credit_period': 30,
                'late_fee': '0.25% per week'
            }
        }
        
        return terms.get(plan_name, terms['Basic Weekly'])
    
    def get_subscription_analytics(self, buyer_id=None):
        """Get subscription analytics and insights"""
        analytics = {
            'total_active_subscriptions': len(self.subscriptions['active_subscriptions']),
            'total_monthly_revenue': sum(sub['total_value'] for sub in self.subscriptions['active_subscriptions']),
            'average_subscription_value': 0,
            'top_crops': self._get_top_crops(),
            'buyer_distribution': self._get_buyer_distribution(),
            'retention_rate': random.uniform(85, 95),
            'growth_metrics': {
                'new_subscriptions_this_month': random.randint(15, 30),
                'cancelled_subscriptions': random.randint(2, 8),
                'upgraded_subscriptions': random.randint(5, 12)
            }
        }
        
        if analytics['total_active_subscriptions'] > 0:
            analytics['average_subscription_value'] = analytics['total_monthly_revenue'] / analytics['total_active_subscriptions']
        
        return {
            'success': True,
            'data': analytics
        }
    
    def _get_top_crops(self):
        """Get most subscribed crops"""
        crop_counts = {}
        for sub in self.subscriptions['active_subscriptions']:
            for crop in sub['crops']:
                crop_counts[crop] = crop_counts.get(crop, 0) + 1
        
        return sorted(crop_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    
    def _get_buyer_distribution(self):
        """Get buyer type distribution"""
        return {
            'restaurants': 45,
            'retailers': 35,
            'hotels': 15,
            'others': 5
        }
    
    def test_connection(self):
        """Test if the subscription model is working"""
        try:
            result = self.get_subscription_analytics()
            if result.get('success'):
                return {'status': 'success', 'message': 'Subscription Model is operational'}
            return {'status': 'error', 'message': 'Subscription Model test failed'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
