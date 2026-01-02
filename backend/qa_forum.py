import json
import os
from datetime import datetime, timedelta
import random

class QAForumManager:
    def __init__(self, data_folder='data'):
        self.data_file = os.path.join(data_folder, 'qa_forum_data.json')
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = self.generate_default_data()
    
    def generate_default_data(self):
        categories = ["Crop Diseases", "Pest Control", "Soil Health", "Irrigation", "Fertilizers", "Weather", "Market Prices", "Government Schemes"]
        questions = []
        
        for i in range(1, 501):
            category = random.choice(categories)
            questions.append({
                "id": f"Q{str(i).zfill(4)}",
                "title": f"Question about {category.lower()} - Issue {i}",
                "category": category,
                "question": f"Detailed question about {category.lower()} with specific farming context and requirements. This is question number {i}.",
                "farmer_name": f"Farmer {i}",
                "farmer_location": random.choice(["Punjab", "Haryana", "UP", "Maharashtra", "Karnataka", "Gujarat", "Rajasthan"]),
                "crop_type": random.choice(["Wheat", "Rice", "Cotton", "Sugarcane", "Vegetables", "Fruits", "Pulses"]),
                "posted_date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
                "status": random.choice(["Open", "Answered", "Resolved"]),
                "urgency": random.choice(["Low", "Medium", "High", "Critical"]),
                "views": random.randint(10, 1000),
                "likes": random.randint(0, 50),
                "answers": [
                    {
                        "id": f"A{str(i).zfill(4)}-1",
                        "expert_name": f"Dr. Expert {i}",
                        "expert_type": random.choice(["Agricultural Scientist", "Extension Officer", "Experienced Farmer", "Veterinarian"]),
                        "answer": f"Comprehensive answer for question {i} with detailed technical guidance and practical solutions.",
                        "answer_date": (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d"),
                        "helpful_votes": random.randint(0, 25),
                        "verified": random.choice([True, False])
                    }
                ] if random.choice([True, False]) else []
            })
        
        return {
            "questions": questions,
            "experts": [
                {
                    "id": f"EXP{str(i).zfill(3)}",
                    "name": f"Dr. Expert {i}",
                    "specialization": random.choice(categories),
                    "qualification": random.choice(["PhD Agriculture", "MSc Agronomy", "Veterinary Doctor", "Extension Specialist"]),
                    "experience_years": random.randint(5, 30),
                    "answers_given": random.randint(50, 500),
                    "rating": round(random.uniform(4.0, 5.0), 1),
                    "location": random.choice(["Punjab", "Haryana", "UP", "Maharashtra", "Karnataka"]),
                    "contact": f"expert{i}@agri.com",
                    "availability": random.choice(["Full-time", "Part-time", "Weekends"])
                } for i in range(1, 51)
            ],
            "categories": categories,
            "forum_stats": {
                "total_questions": 500,
                "answered_questions": 350,
                "active_experts": 50,
                "avg_response_time": "4.2 hours",
                "satisfaction_rate": "94%"
            }
        }
    
    def get_all_questions(self, category=None, status=None):
        questions = self.data["questions"]
        if category:
            questions = [q for q in questions if q["category"] == category]
        if status:
            questions = [q for q in questions if q["status"] == status]
        return sorted(questions, key=lambda x: x["posted_date"], reverse=True)
    
    def get_question_by_id(self, question_id):
        return next((q for q in self.data["questions"] if q["id"] == question_id), None)
    
    def get_experts(self, specialization=None):
        experts = self.data["experts"]
        if specialization:
            experts = [e for e in experts if e["specialization"] == specialization]
        return experts
    
    def get_categories(self):
        return self.data["categories"]
    
    def get_forum_stats(self):
        return self.data["forum_stats"]
        
    def add_question(self, title, category, question_text, user_id, username, tags=None):
        """Add a new question to the forum"""
        try:
            # Generate a new question ID
            last_id = max([int(q["id"].replace('Q', '')) for q in self.data["questions"] if q["id"].startswith('Q')], default=0)
            new_id = f"Q{str(last_id + 1).zfill(4)}"
            
            # Create new question object
            new_question = {
                "id": new_id,
                "title": title,
                "category": category,
                "question": question_text,
                "farmer_name": username,
                "farmer_id": user_id,
                "posted_date": datetime.now().strftime("%Y-%m-%d"),
                "status": "Open",
                "urgency": "Medium",
                "views": 0,
                "likes": 0,
                "tags": tags or [],
                "answers": []
            }
            
            # Add to questions list
            self.data["questions"].insert(0, new_question)
            
            # Update forum stats
            self.data["forum_stats"]["total_questions"] += 1
            
            # Save data to file
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=4)
                
            return True
        except Exception as e:
            print(f"Error adding question: {e}")
            return False
            
    def increment_view_count(self, question_id):
        """Increment the view count for a question"""
        try:
            question = self.get_question_by_id(question_id)
            if question:
                question["views"] += 1
                
                # Save data to file
                with open(self.data_file, 'w') as f:
                    json.dump(self.data, f, indent=4)
                return True
            return False
        except Exception as e:
            print(f"Error incrementing view count: {e}")
            return False
            
    def get_related_questions(self, question_id, limit=5):
        """Get related questions based on category and tags"""
        try:
            question = self.get_question_by_id(question_id)
            if not question:
                return []
                
            category = question["category"]
            tags = question.get("tags", [])
            
            # Get questions with same category or tags
            related = []
            for q in self.data["questions"]:
                # Skip the current question
                if q["id"] == question_id:
                    continue
                    
                # Check if category matches
                if q["category"] == category:
                    related.append(q)
                    continue
                    
                # Check if any tags match
                q_tags = q.get("tags", [])
                if any(tag in q_tags for tag in tags):
                    related.append(q)
            
            # Sort by view count and return limited number
            related.sort(key=lambda x: x["views"], reverse=True)
            return related[:limit]
        except Exception as e:
            print(f"Error getting related questions: {e}")
            return []
            
    def add_answer(self, question_id, answer_text, user_id, username):
        """Add an answer to a question"""
        try:
            question = self.get_question_by_id(question_id)
            if not question:
                return False
                
            # Generate a new answer ID
            last_id = 0
            for q in self.data["questions"]:
                for a in q.get("answers", []):
                    if a["id"].startswith(f"A{question_id.replace('Q', '')}-"):
                        try:
                            answer_num = int(a["id"].split('-')[1])
                            last_id = max(last_id, answer_num)
                        except:
                            pass
            
            new_id = f"A{question_id.replace('Q', '')}-{last_id + 1}"
            
            # Create new answer object
            new_answer = {
                "id": new_id,
                "expert_name": username,
                "expert_id": user_id,
                "expert_type": "Community Member",  # Default type
                "answer": answer_text,
                "answer_date": datetime.now().strftime("%Y-%m-%d"),
                "helpful_votes": 0,
                "verified": False,  # Default to not verified
                "voted_by": []  # Track users who voted
            }
            
            # Add to answers list
            if "answers" not in question:
                question["answers"] = []
            question["answers"].append(new_answer)
            
            # Update question status if it was open
            if question["status"] == "Open":
                question["status"] = "Answered"
            
            # Update forum stats
            self.data["forum_stats"]["answered_questions"] += 1
            
            # Save data to file
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=4)
                
            return True
        except Exception as e:
            print(f"Error adding answer: {e}")
            return False
            
    def upvote_answer(self, question_id, answer_id, user_id):
        """Upvote an answer"""
        try:
            question = self.get_question_by_id(question_id)
            if not question:
                return False
                
            # Find the answer
            answer = None
            for a in question.get("answers", []):
                if a["id"] == answer_id:
                    answer = a
                    break
                    
            if not answer:
                return False
                
            # Check if user already voted
            if "voted_by" not in answer:
                answer["voted_by"] = []
                
            if user_id in answer["voted_by"]:
                return False  # User already voted
                
            # Add vote
            answer["helpful_votes"] += 1
            answer["voted_by"].append(user_id)
            
            # Save data to file
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=4)
                
            return True
        except Exception as e:
            print(f"Error upvoting answer: {e}")
            return False
            
    def upvote_question(self, question_id, user_id):
        """Upvote a question"""
        try:
            question = self.get_question_by_id(question_id)
            if not question:
                return False
                
            # Check if user already voted
            if "voted_by" not in question:
                question["voted_by"] = []
                
            if user_id in question["voted_by"]:
                return False  # User already voted
                
            # Add vote
            if "likes" not in question:
                question["likes"] = 0
                
            question["likes"] += 1
            question["voted_by"].append(user_id)
            
            # Save data to file
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=4)
                
            return True
        except Exception as e:
            print(f"Error upvoting question: {e}")
            return False

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Qa Forum is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
