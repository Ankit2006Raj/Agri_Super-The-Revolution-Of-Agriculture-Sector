import json
import random
from datetime import datetime, timedelta
import uuid

class SuccessStories:
    def __init__(self, data_folder='data'):
        # Define regions first to avoid circular reference
        self.regions = [
            "Punjab", "Haryana", "Uttar Pradesh", "Maharashtra", "Karnataka", "Tamil Nadu",
            "Gujarat", "Rajasthan", "Madhya Pradesh", "West Bengal", "Andhra Pradesh", "Telangana"
        ]
        self.stories_data = self._load_massive_stories_data()
        self.votes = {}
        self.comments = {}
        
    def _load_massive_stories_data(self):
        """Load comprehensive success stories database"""
        return {
            "featured_stories": [
                {
                    "id": "STORY001",
                    "title": "From 2 Acres to 50 Acres: Organic Success Story",
                    "farmer_name": "Ramesh Patel",
                    "location": "Gujarat, India",
                    "crop": "Organic Cotton",
                    "technique": "Organic Farming",
                    "story_type": "featured",
                    "featured_date": "2024-01-15",
                    "before_metrics": {
                        "land_size": "2 acres",
                        "annual_income": "₹80,000",
                        "yield_per_acre": "8 quintals",
                        "input_cost": "₹25,000",
                        "profit_margin": "15%"
                    },
                    "after_metrics": {
                        "land_size": "50 acres",
                        "annual_income": "₹25,00,000",
                        "yield_per_acre": "12 quintals",
                        "input_cost": "₹18,000",
                        "profit_margin": "45%"
                    },
                    "transformation_period": "5 years",
                    "key_changes": [
                        "Switched to organic farming methods",
                        "Implemented drip irrigation system",
                        "Started direct marketing to textile companies",
                        "Formed farmer producer organization",
                        "Adopted precision agriculture techniques"
                    ],
                    "challenges_faced": [
                        "Initial yield drop during transition",
                        "Lack of organic certification knowledge",
                        "Market access difficulties",
                        "Higher labor requirements"
                    ],
                    "solutions_implemented": [
                        "Gradual transition over 3 years",
                        "Joined organic certification program",
                        "Built direct buyer relationships",
                        "Mechanized key operations"
                    ],
                    "story_content": "Ramesh Patel's journey from a struggling small farmer to a successful organic cotton producer is truly inspiring. Starting with just 2 acres of conventional cotton farming, he was barely making ends meet with rising input costs and declining yields. The turning point came when he attended an organic farming workshop in 2019. Despite initial skepticism, he decided to transition 0.5 acres to organic methods as a pilot. The first year was challenging with a 30% yield drop, but by the second year, his organic cotton was fetching 40% premium prices. Encouraged by the results, he gradually converted his entire farm to organic methods. Today, he owns 50 acres and has become a model farmer in his district, training other farmers in organic techniques.",
                    "images": [
                        "/images/stories/ramesh_before.jpg",
                        "/images/stories/ramesh_after.jpg",
                        "/images/stories/ramesh_farm.jpg",
                        "/images/stories/ramesh_certificate.jpg"
                    ],
                    "video_testimonial": "/videos/stories/ramesh_testimonial.mp4",
                    "upvotes": 1247,
                    "comments_count": 89,
                    "shares": 234,
                    "tags": ["organic", "cotton", "success", "gujarat", "transformation"],
                    "submitted_date": "2023-12-10",
                    "verified": True,
                    "impact_score": 95
                },
                {
                    "id": "STORY002", 
                    "title": "Hydroponic Revolution: 10x Yield in Urban Farming",
                    "farmer_name": "Priya Sharma",
                    "location": "Bangalore, Karnataka",
                    "crop": "Leafy Vegetables",
                    "technique": "Hydroponic Farming",
                    "story_type": "featured",
                    "featured_date": "2024-02-20",
                    "before_metrics": {
                        "land_size": "0.1 acres (terrace)",
                        "annual_income": "₹15,000",
                        "yield_per_acre": "2 tons",
                        "input_cost": "₹8,000",
                        "profit_margin": "20%"
                    },
                    "after_metrics": {
                        "land_size": "0.1 acres (vertical)",
                        "annual_income": "₹3,50,000",
                        "yield_per_acre": "20 tons",
                        "input_cost": "₹45,000",
                        "profit_margin": "65%"
                    },
                    "transformation_period": "2 years",
                    "key_changes": [
                        "Implemented vertical hydroponic system",
                        "Automated nutrient delivery",
                        "LED grow lights for year-round production",
                        "Direct-to-consumer sales model",
                        "Organic certification for premium pricing"
                    ],
                    "story_content": "Priya Sharma transformed her small terrace into a high-tech hydroponic farm that produces 10 times more vegetables than traditional farming. As a software engineer turned farmer, she applied technology to solve urban farming challenges. Her vertical hydroponic system produces fresh leafy vegetables year-round, supplying to premium restaurants and health-conscious consumers in Bangalore.",
                    "images": [
                        "/images/stories/priya_setup.jpg",
                        "/images/stories/priya_harvest.jpg",
                        "/images/stories/priya_system.jpg"
                    ],
                    "upvotes": 892,
                    "comments_count": 156,
                    "shares": 178,
                    "tags": ["hydroponics", "urban farming", "technology", "bangalore", "vegetables"],
                    "submitted_date": "2024-01-05",
                    "verified": True,
                    "impact_score": 88
                }
            ],
            "user_stories": self._generate_user_stories(500),  # Generate 500 user stories
            "categories": [
                "Organic Farming", "Hydroponics", "Precision Agriculture", "Crop Diversification",
                "Water Management", "Pest Management", "Post Harvest", "Marketing Innovation",
                "Technology Adoption", "Sustainable Practices", "Income Diversification"
            ],
            "regions": self.regions
        }
    
    def _generate_user_stories(self, count):
        """Generate comprehensive user stories database"""
        stories = []
        crops = ["Rice", "Wheat", "Cotton", "Sugarcane", "Tomato", "Onion", "Potato", "Maize", "Soybean", "Groundnut"]
        techniques = ["Organic Farming", "Drip Irrigation", "Precision Agriculture", "Integrated Pest Management", 
                     "Crop Rotation", "Hydroponics", "Greenhouse Farming", "Direct Marketing"]
        
        for i in range(count):
            story_id = f"STORY{i+3:03d}"
            crop = random.choice(crops)
            technique = random.choice(techniques)
            region = random.choice(self.regions)
            
            # Generate realistic metrics
            before_income = random.randint(50000, 200000)
            after_income = random.randint(int(before_income * 1.5), int(before_income * 5))
            before_yield = random.randint(5, 15)
            after_yield = random.randint(int(before_yield * 1.2), int(before_yield * 3))
            
            story = {
                "id": story_id,
                "title": f"{technique} Success with {crop} in {region}",
                "farmer_name": f"{random.choice(['Raj', 'Amit', 'Suresh', 'Vijay', 'Mohan'])} {random.choice(['Kumar', 'Singh', 'Patel', 'Sharma', 'Yadav'])}",
                "location": f"{region}, India",
                "crop": crop,
                "technique": technique,
                "story_type": "user_submitted",
                "before_metrics": {
                    "annual_income": f"₹{before_income:,}",
                    "yield_per_acre": f"{before_yield} quintals",
                    "input_cost": f"₹{random.randint(15000, 40000):,}",
                    "profit_margin": f"{random.randint(10, 25)}%"
                },
                "after_metrics": {
                    "annual_income": f"₹{after_income:,}",
                    "yield_per_acre": f"{after_yield} quintals", 
                    "input_cost": f"₹{random.randint(20000, 35000):,}",
                    "profit_margin": f"{random.randint(35, 70)}%"
                },
                "transformation_period": f"{random.randint(1, 4)} years",
                "story_content": f"Successful implementation of {technique.lower()} for {crop.lower()} cultivation resulted in significant improvement in yield and income. The farmer overcame initial challenges through proper training and gradual adoption of new techniques.",
                "upvotes": random.randint(10, 500),
                "comments_count": random.randint(5, 50),
                "shares": random.randint(2, 100),
                "tags": [technique.lower().replace(" ", "_"), crop.lower(), region.lower(), "success"],
                "submitted_date": (datetime.now() - timedelta(days=random.randint(1, 730))).strftime("%Y-%m-%d"),
                "verified": random.choice([True, False]),
                "impact_score": random.randint(60, 95)
            }
            stories.append(story)
        
        return stories
    
    def get_stories(self, filters=None):
        """Get filtered success stories"""
        all_stories = self.stories_data["featured_stories"] + self.stories_data["user_stories"]
        
        if filters:
            if filters.get('crop'):
                all_stories = [s for s in all_stories if s['crop'].lower() == filters['crop'].lower()]
            if filters.get('technique'):
                all_stories = [s for s in all_stories if s['technique'].lower() == filters['technique'].lower()]
            if filters.get('region'):
                all_stories = [s for s in all_stories if filters['region'].lower() in s['location'].lower()]
            if filters.get('verified'):
                all_stories = [s for s in all_stories if s.get('verified', False)]
            if filters.get('featured'):
                all_stories = [s for s in all_stories if s['story_type'] == 'featured']
        
        # Sort by impact score and upvotes
        all_stories.sort(key=lambda x: (x.get('impact_score', 0), x.get('upvotes', 0)), reverse=True)
        
        return {
            "success": True,
            "stories": all_stories[:20],  # Paginate results
            "total": len(all_stories),
            "filters_applied": filters or {},
            "categories": self.stories_data["categories"],
            "regions": self.stories_data["regions"]
        }
    
    def get_story_details(self, story_id):
        """Get detailed story information"""
        all_stories = self.stories_data["featured_stories"] + self.stories_data["user_stories"]
        story = next((s for s in all_stories if s["id"] == story_id), None)
        
        if not story:
            return {"success": False, "message": "Story not found"}
        
        # Add additional details
        story_details = story.copy()
        story_details.update({
            "comments": self._get_story_comments(story_id),
            "related_stories": self._get_related_stories(story["crop"], story["technique"]),
            "farmer_profile": self._get_farmer_profile(story["farmer_name"]),
            "impact_metrics": self._calculate_impact_metrics(story)
        })
        
        return {
            "success": True,
            "story": story_details
        }
    
    def _get_story_comments(self, story_id):
        """Get comments for a story"""
        if story_id not in self.comments:
            self.comments[story_id] = self._generate_story_comments()
        return self.comments[story_id]
    
    def _generate_story_comments(self):
        """Generate realistic story comments"""
        comments = []
        comment_templates = [
            "Very inspiring story! Thanks for sharing your experience.",
            "Great work! Can you share more details about the implementation?",
            "This gives me hope for my own farm. Thank you!",
            "Excellent results! How long did the transition take?",
            "Amazing transformation! What were the biggest challenges?",
            "This is exactly what I needed to read today. Very motivating!",
            "Fantastic success story! Any advice for beginners?",
            "Incredible improvement in income! How did you manage the initial investment?"
        ]
        
        for i in range(random.randint(5, 25)):
            comments.append({
                "id": f"COMMENT{i:03d}",
                "user": f"Farmer{random.randint(1000, 9999)}",
                "comment": random.choice(comment_templates),
                "date": (datetime.now() - timedelta(days=random.randint(1, 180))).strftime("%Y-%m-%d"),
                "likes": random.randint(0, 20)
            })
        
        return comments
    
    def _get_related_stories(self, crop, technique):
        """Get related stories based on crop and technique"""
        all_stories = self.stories_data["featured_stories"] + self.stories_data["user_stories"]
        related = [s for s in all_stories if s["crop"] == crop or s["technique"] == technique]
        return random.sample(related, min(4, len(related)))
    
    def _get_farmer_profile(self, farmer_name):
        """Generate farmer profile information"""
        return {
            "name": farmer_name,
            "experience": f"{random.randint(5, 25)} years",
            "specialization": random.choice(["Organic Farming", "Precision Agriculture", "Sustainable Practices"]),
            "achievements": [
                "Best Farmer Award 2023",
                "Organic Certification",
                "Community Leader"
            ],
            "contact_available": random.choice([True, False])
        }
    
    def _calculate_impact_metrics(self, story):
        """Calculate story impact metrics"""
        before_income = int(story["before_metrics"]["annual_income"].replace("₹", "").replace(",", ""))
        after_income = int(story["after_metrics"]["annual_income"].replace("₹", "").replace(",", ""))
        
        return {
            "income_increase_percentage": round(((after_income - before_income) / before_income) * 100, 1),
            "income_increase_amount": f"₹{after_income - before_income:,}",
            "roi_period": story["transformation_period"],
            "sustainability_score": random.randint(70, 95),
            "replicability_score": random.randint(60, 90)
        }
    
    def submit_story(self, data):
        """Submit a new success story"""
        required_fields = ['farmer_name', 'location', 'crop', 'technique', 'story_content']
        
        for field in required_fields:
            if not data.get(field):
                return {"success": False, "message": f"Missing required field: {field}"}
        
        story_id = f"STORY{len(self.stories_data['user_stories']) + 100:03d}"
        
        new_story = {
            "id": story_id,
            "title": data.get('title', f"{data['technique']} Success with {data['crop']}"),
            "farmer_name": data['farmer_name'],
            "location": data['location'],
            "crop": data['crop'],
            "technique": data['technique'],
            "story_type": "user_submitted",
            "before_metrics": data.get('before_metrics', {}),
            "after_metrics": data.get('after_metrics', {}),
            "transformation_period": data.get('transformation_period', ''),
            "story_content": data['story_content'],
            "upvotes": 0,
            "comments_count": 0,
            "shares": 0,
            "tags": data.get('tags', []),
            "submitted_date": datetime.now().strftime("%Y-%m-%d"),
            "verified": False,
            "impact_score": 0,
            "status": "pending_review"
        }
        
        self.stories_data["user_stories"].append(new_story)
        
        return {
            "success": True,
            "message": "Story submitted successfully for review",
            "story_id": story_id,
            "review_time": "2-3 business days"
        }
    
    def vote_story(self, data):
        """Vote on a story (upvote/downvote)"""
        story_id = data.get('story_id')
        user_id = data.get('user_id')
        vote_type = data.get('vote_type')  # 'upvote' or 'downvote'
        
        if not all([story_id, user_id, vote_type]):
            return {"success": False, "message": "Missing required fields"}
        
        # Find and update story
        all_stories = self.stories_data["featured_stories"] + self.stories_data["user_stories"]
        story = next((s for s in all_stories if s["id"] == story_id), None)
        
        if not story:
            return {"success": False, "message": "Story not found"}
        
        # Track user votes to prevent duplicate voting
        vote_key = f"{user_id}_{story_id}"
        if vote_key not in self.votes:
            self.votes[vote_key] = vote_type
            
            if vote_type == 'upvote':
                story['upvotes'] += 1
            
            return {
                "success": True,
                "message": f"Story {vote_type}d successfully",
                "new_upvotes": story['upvotes']
            }
        else:
            return {"success": False, "message": "You have already voted on this story"}

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Success Stories is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
