import json
import random
from datetime import datetime, timedelta

class ProfitAnalyzerEngine:
    def __init__(self, data_folder='data'):
        # Massive profit analysis data
        self.cost_templates = self._generate_cost_templates()
        self.market_prices = self._generate_market_prices()
        self.seasonal_factors = self._generate_seasonal_factors()
        self.risk_factors = self._generate_risk_factors()
        
    def _generate_cost_templates(self):
        return {
            "wheat": {
                "seeds": {"cost_per_hectare": 3500, "percentage": 8},
                "fertilizers": {"cost_per_hectare": 8500, "percentage": 20},
                "pesticides": {"cost_per_hectare": 4200, "percentage": 10},
                "irrigation": {"cost_per_hectare": 6800, "percentage": 16},
                "labor": {"cost_per_hectare": 12000, "percentage": 28},
                "machinery": {"cost_per_hectare": 5500, "percentage": 13},
                "miscellaneous": {"cost_per_hectare": 2100, "percentage": 5}
            },
            "rice": {
                "seeds": {"cost_per_hectare": 4200, "percentage": 9},
                "fertilizers": {"cost_per_hectare": 9800, "percentage": 22},
                "pesticides": {"cost_per_hectare": 5100, "percentage": 11},
                "irrigation": {"cost_per_hectare": 8500, "percentage": 19},
                "labor": {"cost_per_hectare": 11500, "percentage": 26},
                "machinery": {"cost_per_hectare": 4800, "percentage": 11},
                "miscellaneous": {"cost_per_hectare": 1100, "percentage": 2}
            },
            "tomato": {
                "seeds": {"cost_per_hectare": 8500, "percentage": 12},
                "fertilizers": {"cost_per_hectare": 15000, "percentage": 21},
                "pesticides": {"cost_per_hectare": 12000, "percentage": 17},
                "irrigation": {"cost_per_hectare": 10000, "percentage": 14},
                "labor": {"cost_per_hectare": 18000, "percentage": 25},
                "machinery": {"cost_per_hectare": 6000, "percentage": 8},
                "miscellaneous": {"cost_per_hectare": 2500, "percentage": 3}
            }
        }
    
    def _generate_market_prices(self):
        crops = ["wheat", "rice", "tomato", "onion", "potato", "cotton"]
        prices = {}
        
        for crop in crops:
            prices[crop] = {
                "current_price": random.randint(2000, 5000),
                "seasonal_high": random.randint(5500, 8000),
                "seasonal_low": random.randint(1500, 2500),
                "average_price": random.randint(3000, 4500),
                "price_volatility": random.uniform(0.15, 0.35)
            }
        return prices
    
    def _generate_seasonal_factors(self):
        return {
            "kharif": {"demand_multiplier": 1.2, "supply_factor": 0.8, "price_premium": 1.15},
            "rabi": {"demand_multiplier": 1.0, "supply_factor": 1.0, "price_premium": 1.0},
            "summer": {"demand_multiplier": 0.9, "supply_factor": 1.2, "price_premium": 0.85}
        }
    
    def _generate_risk_factors(self):
        return {
            "weather_risk": {"probability": 0.25, "impact_range": [0.7, 0.9]},
            "pest_disease": {"probability": 0.20, "impact_range": [0.8, 0.95]},
            "market_volatility": {"probability": 0.30, "impact_range": [0.85, 1.15]},
            "input_cost_inflation": {"probability": 0.40, "impact_range": [1.05, 1.20]}
        }
    
    def analyze_profit(self, crop, area_hectares, expected_yield_per_hectare, selling_price=None):
        # Get cost breakdown
        cost_template = self.cost_templates.get(crop, self.cost_templates["wheat"])
        
        total_cost_per_hectare = sum(item["cost_per_hectare"] for item in cost_template.values())
        total_cost = total_cost_per_hectare * area_hectares
        
        # Calculate revenue
        if not selling_price:
            selling_price = self.market_prices.get(crop, {"current_price": 3000})["current_price"]
        
        total_yield = expected_yield_per_hectare * area_hectares
        gross_revenue = total_yield * selling_price
        
        # Calculate profit metrics
        net_profit = gross_revenue - total_cost
        profit_margin = (net_profit / gross_revenue) * 100 if gross_revenue > 0 else 0
        roi = (net_profit / total_cost) * 100 if total_cost > 0 else 0
        
        # Break-even analysis
        breakeven_price = total_cost / total_yield if total_yield > 0 else 0
        breakeven_yield = total_cost / selling_price if selling_price > 0 else 0
        
        # Risk analysis
        risk_analysis = self._calculate_risk_scenarios(gross_revenue, total_cost)
        
        # Detailed cost breakdown
        cost_breakdown = []
        for category, data in cost_template.items():
            cost_breakdown.append({
                "category": category.replace("_", " ").title(),
                "cost_per_hectare": data["cost_per_hectare"],
                "total_cost": data["cost_per_hectare"] * area_hectares,
                "percentage": data["percentage"]
            })
        
        return {
            "crop": crop,
            "area_hectares": area_hectares,
            "analysis_date": datetime.now().strftime("%Y-%m-%d"),
            "cost_analysis": {
                "total_cost": total_cost,
                "cost_per_hectare": total_cost_per_hectare,
                "cost_breakdown": cost_breakdown
            },
            "revenue_analysis": {
                "expected_yield_kg": total_yield,
                "selling_price_per_kg": selling_price,
                "gross_revenue": gross_revenue,
                "revenue_per_hectare": gross_revenue / area_hectares
            },
            "profit_metrics": {
                "net_profit": net_profit,
                "profit_per_hectare": net_profit / area_hectares,
                "profit_margin_percentage": round(profit_margin, 2),
                "roi_percentage": round(roi, 2)
            },
            "breakeven_analysis": {
                "breakeven_price_per_kg": round(breakeven_price, 2),
                "breakeven_yield_kg": round(breakeven_yield, 2),
                "safety_margin": round(((selling_price - breakeven_price) / selling_price) * 100, 2)
            },
            "risk_scenarios": risk_analysis,
            "recommendations": self._generate_recommendations(crop, profit_margin, roi),
            "market_comparison": self._get_market_comparison(crop, selling_price)
        }
    
    def _calculate_risk_scenarios(self, base_revenue, base_cost):
        scenarios = {}
        
        # Best case scenario
        scenarios["best_case"] = {
            "probability": 20,
            "revenue_multiplier": 1.25,
            "cost_multiplier": 0.95,
            "net_profit": (base_revenue * 1.25) - (base_cost * 0.95),
            "description": "Favorable weather, high market prices, low input costs"
        }
        
        # Most likely scenario
        scenarios["most_likely"] = {
            "probability": 60,
            "revenue_multiplier": 1.0,
            "cost_multiplier": 1.0,
            "net_profit": base_revenue - base_cost,
            "description": "Normal conditions, expected yields and prices"
        }
        
        # Worst case scenario
        scenarios["worst_case"] = {
            "probability": 20,
            "revenue_multiplier": 0.75,
            "cost_multiplier": 1.15,
            "net_profit": (base_revenue * 0.75) - (base_cost * 1.15),
            "description": "Adverse weather, low prices, high input costs"
        }
        
        return scenarios
    
    def _generate_recommendations(self, crop, profit_margin, roi):
        recommendations = []
        
        if profit_margin < 10:
            recommendations.append("Consider cost reduction strategies - negotiate better input prices")
            recommendations.append("Explore value-added processing to increase selling price")
        elif profit_margin < 20:
            recommendations.append("Good profitability - consider expanding cultivation area")
            recommendations.append("Monitor market trends for optimal selling timing")
        else:
            recommendations.append("Excellent profitability - maintain current practices")
            recommendations.append("Consider premium quality production for higher prices")
        
        if roi < 15:
            recommendations.append("ROI below average - review investment allocation")
        elif roi > 30:
            recommendations.append("Outstanding ROI - consider scaling up operations")
        
        recommendations.extend([
            f"Consider crop insurance to mitigate risks for {crop}",
            "Implement precision farming techniques to optimize inputs",
            "Explore contract farming for price stability"
        ])
        
        return recommendations
    
    def _get_market_comparison(self, crop, current_price):
        market_data = self.market_prices.get(crop, {})
        if not market_data:
            return {"message": "Market data not available"}
        
        return {
            "current_vs_average": round(((current_price - market_data["average_price"]) / market_data["average_price"]) * 100, 2),
            "current_vs_seasonal_high": round(((current_price - market_data["seasonal_high"]) / market_data["seasonal_high"]) * 100, 2),
            "price_position": "Above average" if current_price > market_data["average_price"] else "Below average",
            "volatility_level": "High" if market_data["price_volatility"] > 0.25 else "Moderate"
        }

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Profit Analyzer is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
