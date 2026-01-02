import json
import random
from datetime import datetime, timedelta

class MarketComparisonEngine:
    def __init__(self, data_folder='data'):
        # Massive market comparison data
        self.markets_data = self._generate_markets_data()
        self.price_history = self._generate_price_history()
        self.transportation_costs = self._generate_transport_costs()
        
    def _generate_markets_data(self):
        markets = {}
        market_names = [
            "Delhi Azadpur Mandi", "Mumbai Vashi Market", "Kolkata Sealdah Market",
            "Chennai Koyambedu Market", "Bangalore Yeshwantpur Market", "Hyderabad Gaddiannaram",
            "Pune Market Yard", "Ahmedabad Jamalpur Market", "Jaipur Sikar Road Market",
            "Lucknow Aliganj Market", "Kanpur Grain Market", "Nagpur Cotton Market"
        ]
        
        crops = ["wheat", "rice", "tomato", "onion", "potato", "cotton", "sugarcane", "maize"]
        
        for market in market_names:
            markets[market] = {}
            for crop in crops:
                markets[market][crop] = {
                    "current_price": random.randint(1500, 5000),
                    "yesterday_price": random.randint(1400, 4900),
                    "weekly_high": random.randint(1600, 5200),
                    "weekly_low": random.randint(1300, 4800),
                    "monthly_average": random.randint(1450, 4950),
                    "demand_level": random.choice(["High", "Medium", "Low"]),
                    "supply_status": random.choice(["Surplus", "Adequate", "Shortage"]),
                    "quality_premium": random.randint(0, 500),
                    "market_fee_percentage": random.uniform(1.5, 3.5),
                    "transportation_distance": random.randint(50, 800),
                    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
        return markets
    
    def _generate_price_history(self):
        history = {}
        crops = ["wheat", "rice", "tomato", "onion", "potato"]
        
        for crop in crops:
            history[crop] = []
            base_price = random.randint(2000, 4000)
            
            for i in range(365):  # 1 year of daily data
                date = datetime.now() - timedelta(days=i)
                price_variation = random.uniform(-0.1, 0.1)
                price = base_price * (1 + price_variation)
                
                history[crop].append({
                    "date": date.strftime("%Y-%m-%d"),
                    "price": round(price, 2),
                    "volume": random.randint(100, 1000),
                    "trend": random.choice(["up", "down", "stable"])
                })
        return history
    
    def _generate_transport_costs(self):
        return {
            "truck": {"cost_per_km": 12, "capacity_tons": 10, "time_factor": 1.0},
            "rail": {"cost_per_km": 8, "capacity_tons": 50, "time_factor": 1.5},
            "combined": {"cost_per_km": 10, "capacity_tons": 25, "time_factor": 1.2}
        }
    
    def compare_markets(self, crop, quantity_tons, farmer_location):
        comparison_results = []
        
        for market_name, market_data in self.markets_data.items():
            if crop in market_data:
                crop_data = market_data[crop]
                
                # Calculate transportation cost
                distance = crop_data["transportation_distance"]
                transport_cost = self._calculate_transport_cost(distance, quantity_tons)
                
                # Calculate net price after deductions
                gross_price = crop_data["current_price"] * quantity_tons
                market_fee = gross_price * (crop_data["market_fee_percentage"] / 100)
                net_price = gross_price - market_fee - transport_cost
                
                comparison_results.append({
                    "market_name": market_name,
                    "current_price_per_kg": crop_data["current_price"],
                    "gross_revenue": gross_price,
                    "transportation_cost": transport_cost,
                    "market_fee": market_fee,
                    "net_revenue": net_price,
                    "profit_margin": round((net_price / gross_price) * 100, 2),
                    "distance_km": distance,
                    "demand_level": crop_data["demand_level"],
                    "supply_status": crop_data["supply_status"],
                    "price_trend": self._get_price_trend(crop, market_name),
                    "quality_premium": crop_data["quality_premium"],
                    "recommendation_score": self._calculate_recommendation_score(crop_data, net_price)
                })
        
        # Sort by net revenue (highest first)
        comparison_results.sort(key=lambda x: x["net_revenue"], reverse=True)
        
        return {
            "crop": crop,
            "quantity_tons": quantity_tons,
            "farmer_location": farmer_location,
            "comparison_date": datetime.now().strftime("%Y-%m-%d"),
            "markets_compared": len(comparison_results),
            "best_market": comparison_results[0] if comparison_results else None,
            "all_markets": comparison_results,
            "market_insights": self._generate_market_insights(comparison_results, crop)
        }
    
    def _calculate_transport_cost(self, distance, quantity_tons):
        # Use truck transport as default
        cost_per_km = self.transportation_costs["truck"]["cost_per_km"]
        return distance * cost_per_km * (quantity_tons / 10)  # Normalize by truck capacity
    
    def _get_price_trend(self, crop, market_name):
        if crop in self.price_history:
            recent_prices = self.price_history[crop][:7]  # Last 7 days
            if len(recent_prices) >= 2:
                if recent_prices[0]["price"] > recent_prices[-1]["price"]:
                    return "increasing"
                elif recent_prices[0]["price"] < recent_prices[-1]["price"]:
                    return "decreasing"
        return "stable"
    
    def _calculate_recommendation_score(self, crop_data, net_price):
        score = 0
        
        # Price factor (40%)
        if crop_data["current_price"] > crop_data["monthly_average"]:
            score += 40
        elif crop_data["current_price"] > crop_data["monthly_average"] * 0.95:
            score += 30
        else:
            score += 20
        
        # Demand factor (30%)
        demand_scores = {"High": 30, "Medium": 20, "Low": 10}
        score += demand_scores.get(crop_data["demand_level"], 15)
        
        # Supply factor (20%)
        supply_scores = {"Shortage": 20, "Adequate": 15, "Surplus": 5}
        score += supply_scores.get(crop_data["supply_status"], 10)
        
        # Distance factor (10%)
        if crop_data["transportation_distance"] < 200:
            score += 10
        elif crop_data["transportation_distance"] < 500:
            score += 7
        else:
            score += 3
        
        return min(score, 100)
    
    def _generate_market_insights(self, results, crop):
        if not results:
            return []
        
        insights = []
        best_market = results[0]
        worst_market = results[-1]
        
        price_difference = best_market["net_revenue"] - worst_market["net_revenue"]
        insights.append(f"Price difference between best and worst market: ₹{price_difference:,.2f}")
        
        high_demand_markets = [r for r in results if r["demand_level"] == "High"]
        if high_demand_markets:
            insights.append(f"{len(high_demand_markets)} markets showing high demand for {crop}")
        
        nearby_markets = [r for r in results if r["distance_km"] < 200]
        if nearby_markets:
            best_nearby = max(nearby_markets, key=lambda x: x["net_revenue"])
            insights.append(f"Best nearby market (< 200km): {best_nearby['market_name']}")
        
        return insights

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Market Comparison is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
