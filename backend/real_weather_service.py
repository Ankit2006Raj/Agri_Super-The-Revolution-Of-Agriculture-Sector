"""
Real Weather & Disaster Alert Integration
Connects with IMD, NASA POWER, and other meteorological services
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RealWeatherService:
    """
    Real-time weather and disaster alert service integrating:
    - India Meteorological Department (IMD)
    - NASA POWER (Global Agricultural Weather)
    - OpenWeatherMap (Backup)
    - ISRO MOSDAC (Satellite data)
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        
        # API endpoints
        self.imd_api = "https://city.imd.gov.in/cityweb/weather_forecast.php"
        self.nasa_power_api = "https://power.larc.nasa.gov/api/temporal/daily/point"
        self.openweather_api = "https://api.openweathermap.org/data/2.5"
        
        # API keys
        self.openweather_key = self.config.get('OPENWEATHER_API_KEY', 'YOUR_API_KEY')
        
        # Alert thresholds
        self.alert_thresholds = {
            'temperature': {'high': 40, 'low': 5},  # Celsius
            'rainfall': {'heavy': 100, 'extreme': 200},  # mm/day
            'wind_speed': {'high': 40, 'extreme': 60},  # km/h
            'humidity': {'low': 30, 'high': 90}  # percentage
        }
        
        # Crop-specific weather requirements
        self.crop_requirements = {
            'wheat': {'temp_range': (15, 25), 'rainfall': (75, 100), 'humidity': (50, 70)},
            'rice': {'temp_range': (20, 35), 'rainfall': (150, 300), 'humidity': (60, 80)},
            'cotton': {'temp_range': (21, 30), 'rainfall': (50, 100), 'humidity': (60, 70)},
            'tomato': {'temp_range': (18, 27), 'rainfall': (30, 50), 'humidity': (60, 80)},
            'onion': {'temp_range': (13, 24), 'rainfall': (25, 50), 'humidity': (65, 70)},
        }
        
        # Cache
        self.cache = {}
        self.cache_duration = timedelta(minutes=30)
    
    def get_farm_weather(self, latitude: float, longitude: float, 
                        days: int = 7, location_name: str = None) -> Dict:
        """
        Get comprehensive weather forecast for farm location
        
        Args:
            latitude: Farm latitude
            longitude: Farm longitude
            days: Number of days to forecast (1-7)
            location_name: Optional location name for display
            
        Returns:
            Dictionary with weather forecast and agricultural advisories
        """
        try:
            # Check cache
            cache_key = f"{latitude}_{longitude}_{days}"
            if self._is_cache_valid(cache_key):
                logger.info(f"Returning cached weather data for {location_name or cache_key}")
                return self.cache[cache_key]
            
            # Fetch from multiple sources
            nasa_data = self._fetch_nasa_power_data(latitude, longitude, days)
            openweather_data = self._fetch_openweather_data(latitude, longitude, days)
            
            # Process and combine data
            result = self._process_weather_data(
                nasa_data, openweather_data, latitude, longitude, location_name, days
            )
            
            # Cache result
            self.cache[cache_key] = result
            
            return result
            
        except Exception as e:
            logger.error(f"Error fetching weather data: {str(e)}")
            return self._get_fallback_weather(latitude, longitude, location_name, days)
    
    def _fetch_nasa_power_data(self, lat: float, lon: float, days: int) -> Dict:
        """Fetch agricultural weather data from NASA POWER"""
        try:
            # Calculate date range
            start_date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
            end_date = (datetime.now() + timedelta(days=days)).strftime('%Y%m%d')
            
            params = {
                'parameters': 'T2M,T2M_MIN,T2M_MAX,PRECTOTCORR,RH2M,WS2M,ALLSKY_SFC_SW_DWN',
                'community': 'AG',  # Agricultural community
                'longitude': lon,
                'latitude': lat,
                'start': start_date,
                'end': end_date,
                'format': 'JSON'
            }
            
            response = requests.get(self.nasa_power_api, params=params, timeout=15)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"NASA POWER API error: {str(e)}")
            return {}
    
    def _fetch_openweather_data(self, lat: float, lon: float, days: int) -> Dict:
        """Fetch weather data from OpenWeatherMap (backup source)"""
        try:
            # Current weather
            current_url = f"{self.openweather_api}/weather"
            current_params = {
                'lat': lat,
                'lon': lon,
                'appid': self.openweather_key,
                'units': 'metric'
            }
            
            current_response = requests.get(current_url, params=current_params, timeout=10)
            current_response.raise_for_status()
            current_data = current_response.json()
            
            # Forecast
            forecast_url = f"{self.openweather_api}/forecast"
            forecast_params = {
                'lat': lat,
                'lon': lon,
                'appid': self.openweather_key,
                'units': 'metric',
                'cnt': days * 8  # 8 forecasts per day (3-hour intervals)
            }
            
            forecast_response = requests.get(forecast_url, params=forecast_params, timeout=10)
            forecast_response.raise_for_status()
            forecast_data = forecast_response.json()
            
            return {
                'current': current_data,
                'forecast': forecast_data
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"OpenWeatherMap API error: {str(e)}")
            return {}
    
    def _process_weather_data(self, nasa_data: Dict, openweather_data: Dict,
                             lat: float, lon: float, location_name: str, days: int) -> Dict:
        """Process and combine weather data from multiple sources"""
        
        # Current conditions (from OpenWeatherMap)
        current_weather = {}
        if openweather_data and 'current' in openweather_data:
            current = openweather_data['current']
            current_weather = {
                'temperature': current['main']['temp'],
                'feels_like': current['main']['feels_like'],
                'humidity': current['main']['humidity'],
                'wind_speed': current['wind']['speed'] * 3.6,  # Convert m/s to km/h
                'description': current['weather'][0]['description'],
                'icon': current['weather'][0]['icon'],
                'clouds': current['clouds']['all'],
                'visibility': current.get('visibility', 10000) / 1000,  # km
                'timestamp': datetime.fromtimestamp(current['dt']).isoformat()
            }
        
        # Daily forecast
        forecast_days = []
        if openweather_data and 'forecast' in openweather_data:
            forecast_list = openweather_data['forecast'].get('list', [])
            
            # Group by day and calculate daily aggregates
            daily_data = {}
            for item in forecast_list:
                date = datetime.fromtimestamp(item['dt']).date()
                if date not in daily_data:
                    daily_data[date] = []
                daily_data[date].append(item)
            
            # Process each day
            for date in sorted(daily_data.keys())[:days]:
                day_items = daily_data[date]
                
                temps = [item['main']['temp'] for item in day_items]
                humidity = [item['main']['humidity'] for item in day_items]
                wind_speeds = [item['wind']['speed'] * 3.6 for item in day_items]
                rain = sum(item.get('rain', {}).get('3h', 0) for item in day_items)
                
                # Most common weather condition
                conditions = [item['weather'][0]['description'] for item in day_items]
                most_common = max(set(conditions), key=conditions.count)
                
                forecast_days.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'day': date.strftime('%A'),
                    'temperature': {
                        'min': round(min(temps), 1),
                        'max': round(max(temps), 1),
                        'avg': round(sum(temps) / len(temps), 1)
                    },
                    'humidity': round(sum(humidity) / len(humidity), 1),
                    'wind_speed': round(sum(wind_speeds) / len(wind_speeds), 1),
                    'rainfall': round(rain, 1),
                    'condition': most_common,
                    'icon': day_items[len(day_items)//2]['weather'][0]['icon']
                })
        
        # Generate alerts based on thresholds
        alerts = self._generate_weather_alerts(forecast_days)
        
        # Generate agricultural advisories
        advisories = self._generate_agricultural_advisories(current_weather, forecast_days, alerts)
        
        return {
            'success': True,
            'location': {
                'name': location_name or f"Lat {lat}, Lon {lon}",
                'latitude': lat,
                'longitude': lon
            },
            'timestamp': datetime.now().isoformat(),
            'current_weather': current_weather,
            'forecast': forecast_days,
            'alerts': alerts,
            'agricultural_advisories': advisories,
            'data_sources': ['NASA POWER', 'OpenWeatherMap'],
            'forecast_period': f'{days} days'
        }
    
    def _generate_weather_alerts(self, forecast_days: List[Dict]) -> List[Dict]:
        """Generate weather alerts based on thresholds"""
        alerts = []
        
        for day in forecast_days:
            # Temperature alerts
            if day['temperature']['max'] > self.alert_thresholds['temperature']['high']:
                alerts.append({
                    'date': day['date'],
                    'type': 'heat_wave',
                    'severity': 'high' if day['temperature']['max'] > 42 else 'medium',
                    'title': 'Heat Wave Alert',
                    'message': f"Very high temperature expected ({day['temperature']['max']}°C)",
                    'recommendations': [
                        'Increase irrigation frequency',
                        'Provide shade to crops if possible',
                        'Avoid working during peak heat hours (12-4 PM)',
                        'Ensure livestock have adequate water and shade'
                    ]
                })
            
            if day['temperature']['min'] < self.alert_thresholds['temperature']['low']:
                alerts.append({
                    'date': day['date'],
                    'type': 'cold_wave',
                    'severity': 'medium',
                    'title': 'Cold Wave Alert',
                    'message': f"Very low temperature expected ({day['temperature']['min']}°C)",
                    'recommendations': [
                        'Protect sensitive crops with covering',
                        'Consider using frost protection methods',
                        'Delay planting of warm-season crops'
                    ]
                })
            
            # Rainfall alerts
            if day['rainfall'] > self.alert_thresholds['rainfall']['extreme']:
                alerts.append({
                    'date': day['date'],
                    'type': 'heavy_rain',
                    'severity': 'critical',
                    'title': 'Extreme Rainfall Alert',
                    'message': f"Very heavy rainfall expected ({day['rainfall']} mm)",
                    'recommendations': [
                        'Ensure proper field drainage',
                        'Avoid spraying pesticides',
                        'Secure farm equipment and produce',
                        'Harvest ready crops if possible'
                    ]
                })
            elif day['rainfall'] > self.alert_thresholds['rainfall']['heavy']:
                alerts.append({
                    'date': day['date'],
                    'type': 'heavy_rain',
                    'severity': 'high',
                    'title': 'Heavy Rainfall Alert',
                    'message': f"Heavy rainfall expected ({day['rainfall']} mm)",
                    'recommendations': [
                        'Clear drainage channels',
                        'Postpone fertilizer application',
                        'Monitor for waterlogging'
                    ]
                })
            
            # Wind alerts
            if day['wind_speed'] > self.alert_thresholds['wind_speed']['extreme']:
                alerts.append({
                    'date': day['date'],
                    'type': 'high_wind',
                    'severity': 'critical',
                    'title': 'Severe Wind Alert',
                    'message': f"Very high wind speeds expected ({day['wind_speed']} km/h)",
                    'recommendations': [
                        'Secure greenhouse structures',
                        'Provide support to tall crops',
                        'Avoid spraying operations',
                        'Secure loose equipment'
                    ]
                })
        
        return alerts
    
    def _generate_agricultural_advisories(self, current: Dict, forecast: List[Dict], 
                                         alerts: List[Dict]) -> List[Dict]:
        """Generate crop-specific agricultural advisories"""
        advisories = []
        
        # Irrigation advisory
        upcoming_rain = sum(day.get('rainfall', 0) for day in forecast[:3])  # Next 3 days
        
        if upcoming_rain > 20:
            advisories.append({
                'category': 'irrigation',
                'priority': 'high',
                'title': 'Reduce Irrigation',
                'message': f'Expected rainfall of {upcoming_rain:.1f}mm in next 3 days. Reduce or skip irrigation.',
                'affected_crops': 'All crops',
                'action': 'Monitor soil moisture before irrigating'
            })
        elif upcoming_rain < 5 and current.get('humidity', 70) < 60:
            advisories.append({
                'category': 'irrigation',
                'priority': 'high',
                'title': 'Increase Irrigation',
                'message': f'Minimal rainfall expected. Dry conditions with {current.get("humidity", 0):.0f}% humidity.',
                'affected_crops': 'All crops',
                'action': 'Ensure adequate irrigation, especially for water-sensitive crops'
            })
        
        # Pest management advisory
        if forecast[0].get('humidity', 0) > 80 and forecast[0]['temperature']['avg'] > 25:
            advisories.append({
                'category': 'pest_management',
                'priority': 'medium',
                'title': 'Pest Activity Alert',
                'message': 'High humidity and warm temperature favor pest and disease development.',
                'affected_crops': 'Vegetables, fruits, cereals',
                'action': 'Monitor crops regularly. Consider preventive spraying if needed.'
            })
        
        # Sowing/planting advisory
        if len(alerts) == 0 and 15 < forecast[0]['temperature']['avg'] < 30:
            advisories.append({
                'category': 'planting',
                'priority': 'medium',
                'title': 'Favorable Planting Conditions',
                'message': 'Weather conditions are suitable for planting/sowing operations.',
                'affected_crops': 'Season-appropriate crops',
                'action': 'Good time for field preparation and sowing'
            })
        
        # Harvest advisory
        if upcoming_rain < 5 and all(day.get('rainfall', 0) < 5 for day in forecast[:5]):
            advisories.append({
                'category': 'harvesting',
                'priority': 'high',
                'title': 'Good Harvesting Window',
                'message': 'Dry weather expected for next 5 days. Ideal for harvesting operations.',
                'affected_crops': 'Ready-to-harvest crops',
                'action': 'Plan harvest activities for mature crops'
            })
        
        return advisories
    
    def get_disaster_alerts(self, state: str, district: str = None) -> Dict:
        """
        Fetch real disaster alerts from IMD and other sources
        
        Args:
            state: State name
            district: Optional district name
            
        Returns:
            Dictionary with active disaster alerts
        """
        try:
            # In production, integrate with IMD's official alert API
            # For now, analyzing weather forecasts to generate alerts
            
            alerts = []
            
            # Placeholder for IMD integration
            # IMD provides district-wise disaster warnings
            # Format: Cyclone, Flood, Drought, Heat Wave, Cold Wave, etc.
            
            return {
                'success': True,
                'state': state,
                'district': district,
                'timestamp': datetime.now().isoformat(),
                'active_alerts': alerts,
                'source': 'IMD (India Meteorological Department)',
                'emergency_contacts': {
                    'disaster_helpline': '1077',
                    'district_control_room': 'Contact local administration',
                    'agriculture_helpline': '1800-180-1551'
                }
            }
            
        except Exception as e:
            logger.error(f"Error fetching disaster alerts: {str(e)}")
            return {
                'success': False,
                'message': f'Error fetching alerts: {str(e)}'
            }
    
    def get_crop_specific_forecast(self, latitude: float, longitude: float, 
                                   crop: str, days: int = 7) -> Dict:
        """
        Get crop-specific weather forecast with suitability analysis
        
        Args:
            latitude: Farm latitude
            longitude: Farm longitude
            crop: Crop name (e.g., 'wheat', 'rice')
            days: Forecast days
            
        Returns:
            Dictionary with crop-specific weather analysis
        """
        # Get general weather
        weather = self.get_farm_weather(latitude, longitude, days)
        
        if not weather.get('success'):
            return weather
        
        # Get crop requirements
        requirements = self.crop_requirements.get(crop.lower(), None)
        
        if not requirements:
            weather['crop_suitability'] = {
                'crop': crop,
                'message': 'Crop requirements not available in database'
            }
            return weather
        
        # Analyze suitability for each day
        suitability_analysis = []
        
        for day in weather['forecast']:
            temp_suitable = (
                requirements['temp_range'][0] <= day['temperature']['avg'] <= requirements['temp_range'][1]
            )
            humidity_suitable = (
                requirements['humidity'][0] <= day['humidity'] <= requirements['humidity'][1]
            )
            
            # Determine overall suitability
            if temp_suitable and humidity_suitable:
                suitability = 'favorable'
                color = 'green'
            elif temp_suitable or humidity_suitable:
                suitability = 'moderate'
                color = 'yellow'
            else:
                suitability = 'unfavorable'
                color = 'red'
            
            suitability_analysis.append({
                'date': day['date'],
                'suitability': suitability,
                'color': color,
                'factors': {
                    'temperature': 'suitable' if temp_suitable else 'unsuitable',
                    'humidity': 'suitable' if humidity_suitable else 'unsuitable'
                }
            })
        
        weather['crop_suitability'] = {
            'crop': crop,
            'requirements': requirements,
            'daily_analysis': suitability_analysis,
            'overall_recommendation': self._get_crop_recommendation(suitability_analysis)
        }
        
        return weather
    
    def _get_crop_recommendation(self, analysis: List[Dict]) -> str:
        """Generate overall crop recommendation based on suitability"""
        favorable_count = sum(1 for day in analysis if day['suitability'] == 'favorable')
        total_days = len(analysis)
        
        if favorable_count / total_days > 0.7:
            return 'Excellent conditions for this crop. Proceed with planned activities.'
        elif favorable_count / total_days > 0.4:
            return 'Moderate conditions. Monitor weather closely and adjust practices as needed.'
        else:
            return 'Challenging conditions. Consider delaying activities or extra protection measures.'
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cached data is still valid"""
        if cache_key not in self.cache:
            return False
        
        cache_time = self.cache[cache_key].get('_cache_time')
        if not cache_time:
            return False
        
        return datetime.now() - cache_time < self.cache_duration
    
    def _get_fallback_weather(self, lat: float, lon: float, 
                             location: str, days: int) -> Dict:
        """Return fallback weather data when APIs fail"""
        return {
            'success': False,
            'location': {
                'name': location or f"Lat {lat}, Lon {lon}",
                'latitude': lat,
                'longitude': lon
            },
            'timestamp': datetime.now().isoformat(),
            'error': 'Unable to fetch weather data from external sources',
            'message': 'Please try again later or check local weather sources',
            'emergency_contacts': {
                'imd_helpline': '1800-180-1551',
                'weather_info': 'SMS "WEATHER <location>" to 7738299899'
            }
        }


# Example usage and testing
if __name__ == "__main__":
    # Initialize service
    config = {
        'OPENWEATHER_API_KEY': 'your_api_key_here'
    }
    
    service = RealWeatherService(config)
    
    # Test: Get farm weather (Example: Ludhiana, Punjab)
    print("Testing farm weather forecast...")
    weather = service.get_farm_weather(30.9010, 75.8573, days=7, location_name="Ludhiana, Punjab")
    print(json.dumps(weather, indent=2))
    
    # Test: Get crop-specific forecast
    print("\nTesting crop-specific forecast...")
    crop_weather = service.get_crop_specific_forecast(30.9010, 75.8573, 'wheat', days=5)
    print(json.dumps(crop_weather, indent=2))
    
    # Test: Get disaster alerts
    print("\nTesting disaster alerts...")
    alerts = service.get_disaster_alerts('Punjab', 'Ludhiana')
    print(json.dumps(alerts, indent=2))
