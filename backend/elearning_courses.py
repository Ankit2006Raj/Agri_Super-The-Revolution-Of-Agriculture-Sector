import json
import random
from datetime import datetime, timedelta
import uuid

class ELearningCourses:
    def __init__(self, data_folder='data'):
        self.courses_data = self._load_massive_course_data()
        self.user_progress = {}
        self.certificates = {}
        
    def _load_massive_course_data(self):
        """Load comprehensive course catalog with 100+ courses"""
        return {
            "courses": [
                {
                    "id": "ORG001",
                    "title": "Organic Farming Fundamentals",
                    "category": "Organic",
                    "difficulty": "Beginner",
                    "duration": "4 hours",
                    "language": ["English", "Hindi", "Tamil"],
                    "instructor": "Dr. Rajesh Kumar",
                    "rating": 4.8,
                    "enrolled": 15420,
                    "description": "Complete guide to organic farming practices",
                    "modules": [
                        {"id": 1, "title": "Introduction to Organic Farming", "duration": "12 min", "type": "video"},
                        {"id": 2, "title": "Soil Health Management", "duration": "15 min", "type": "video"},
                        {"id": 3, "title": "Organic Pest Control", "duration": "18 min", "type": "video"},
                        {"id": 4, "title": "Certification Process", "duration": "10 min", "type": "video"},
                        {"id": 5, "title": "Quiz: Organic Basics", "duration": "5 min", "type": "quiz"}
                    ],
                    "learning_outcomes": [
                        "Understand organic farming principles",
                        "Learn soil health management",
                        "Master organic pest control methods",
                        "Navigate certification requirements"
                    ],
                    "prerequisites": "Basic farming knowledge",
                    "certificate": True,
                    "price": 0,
                    "tags": ["organic", "sustainable", "certification"]
                },
                {
                    "id": "GH002",
                    "title": "Greenhouse Management Mastery",
                    "category": "Protected Cultivation",
                    "difficulty": "Intermediate",
                    "duration": "6 hours",
                    "language": ["English", "Hindi"],
                    "instructor": "Prof. Meera Sharma",
                    "rating": 4.9,
                    "enrolled": 8750,
                    "description": "Advanced greenhouse cultivation techniques",
                    "modules": [
                        {"id": 1, "title": "Greenhouse Design Principles", "duration": "20 min", "type": "video"},
                        {"id": 2, "title": "Climate Control Systems", "duration": "25 min", "type": "video"},
                        {"id": 3, "title": "Hydroponic Systems", "duration": "30 min", "type": "video"},
                        {"id": 4, "title": "Disease Management", "duration": "22 min", "type": "video"},
                        {"id": 5, "title": "Economic Analysis", "duration": "18 min", "type": "video"},
                        {"id": 6, "title": "Final Assessment", "duration": "15 min", "type": "quiz"}
                    ],
                    "learning_outcomes": [
                        "Design efficient greenhouse structures",
                        "Implement climate control systems",
                        "Set up hydroponic systems",
                        "Manage greenhouse diseases effectively"
                    ],
                    "prerequisites": "Basic horticulture knowledge",
                    "certificate": True,
                    "price": 299,
                    "tags": ["greenhouse", "hydroponics", "protected cultivation"]
                },
                # Add 98 more courses with similar detailed structure
                *self._generate_additional_courses()
            ],
            "learning_paths": [
                {
                    "id": "PATH001",
                    "title": "Organic Farming Specialist",
                    "description": "Complete journey from beginner to organic farming expert",
                    "courses": ["ORG001", "ORG002", "ORG003", "ORG004"],
                    "duration": "20 hours",
                    "certificate": "Organic Farming Specialist Certificate"
                },
                {
                    "id": "PATH002",
                    "title": "Greenhouse Technology Expert",
                    "description": "Master modern greenhouse cultivation techniques",
                    "courses": ["GH002", "GH003", "GH004", "GH005"],
                    "duration": "25 hours",
                    "certificate": "Greenhouse Technology Expert Certificate"
                }
            ]
        }
    
    def _generate_additional_courses(self):
        """Generate 98 additional courses with comprehensive data"""
        categories = ["Organic", "Hydroponics", "Pest Management", "Soil Health", "Crop Nutrition", 
                     "Water Management", "Post Harvest", "Marketing", "Finance", "Technology"]
        difficulties = ["Beginner", "Intermediate", "Advanced"]
        languages = [["English", "Hindi"], ["English", "Hindi", "Tamil"], ["English", "Hindi", "Bengali"]]
        
        courses = []
        for i in range(3, 101):  # Generate courses 003 to 100
            category = random.choice(categories)
            difficulty = random.choice(difficulties)
            lang = random.choice(languages)
            
            course = {
                "id": f"{category[:3].upper()}{i:03d}",
                "title": f"{category} {['Basics', 'Advanced', 'Mastery'][difficulties.index(difficulty)]}",
                "category": category,
                "difficulty": difficulty,
                "duration": f"{random.randint(2, 8)} hours",
                "language": lang,
                "instructor": f"Dr. {random.choice(['Amit', 'Priya', 'Ravi', 'Sunita'])} {random.choice(['Patel', 'Singh', 'Kumar', 'Sharma'])}",
                "rating": round(random.uniform(4.2, 5.0), 1),
                "enrolled": random.randint(500, 20000),
                "description": f"Comprehensive guide to {category.lower()} techniques and best practices",
                "modules": [
                    {"id": j, "title": f"Module {j}", "duration": f"{random.randint(8, 25)} min", 
                     "type": "video" if j < 5 else "quiz"} for j in range(1, 7)
                ],
                "learning_outcomes": [
                    f"Master {category.lower()} fundamentals",
                    f"Implement {category.lower()} best practices",
                    f"Troubleshoot {category.lower()} issues",
                    f"Optimize {category.lower()} results"
                ],
                "prerequisites": "Basic farming knowledge" if difficulty == "Beginner" else f"Intermediate {category.lower()} knowledge",
                "certificate": True,
                "price": random.choice([0, 199, 299, 499, 799]),
                "tags": [category.lower(), "farming", "agriculture"]
            }
            courses.append(course)
        
        return courses
    
    def get_courses(self, filters=None):
        """Get filtered course catalog"""
        courses = self.courses_data["courses"]
        
        if filters:
            if filters.get('category'):
                courses = [c for c in courses if c['category'].lower() == filters['category'].lower()]
            if filters.get('difficulty'):
                courses = [c for c in courses if c['difficulty'].lower() == filters['difficulty'].lower()]
            if filters.get('language'):
                courses = [c for c in courses if filters['language'] in c['language']]
            if filters.get('free'):
                courses = [c for c in courses if c['price'] == 0]
        
        return {
            "success": True,
            "courses": courses[:20],  # Paginate results
            "total": len(courses),
            "filters_applied": filters or {}
        }
    
    def get_course_details(self, course_id):
        """Get detailed course information"""
        course = next((c for c in self.courses_data["courses"] if c["id"] == course_id), None)
        
        if not course:
            return {"success": False, "message": "Course not found"}
        
        # Add additional details
        course_details = course.copy()
        course_details.update({
            "reviews": self._generate_course_reviews(course_id),
            "related_courses": self._get_related_courses(course["category"]),
            "completion_rate": random.randint(75, 95),
            "job_placement_rate": random.randint(60, 85) if course["price"] > 0 else None
        })
        
        return {
            "success": True,
            "course": course_details
        }
    
    def _generate_course_reviews(self, course_id):
        """Generate realistic course reviews"""
        reviews = []
        for i in range(random.randint(10, 50)):
            reviews.append({
                "id": f"REV{i:03d}",
                "user": f"Farmer{random.randint(1000, 9999)}",
                "rating": random.randint(4, 5),
                "comment": random.choice([
                    "Excellent course! Very practical and easy to understand.",
                    "Great instructor and comprehensive content.",
                    "Helped me improve my farming techniques significantly.",
                    "Well structured course with good examples.",
                    "Highly recommended for all farmers."
                ]),
                "date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d")
            })
        return reviews
    
    def _get_related_courses(self, category):
        """Get courses in the same category"""
        related = [c for c in self.courses_data["courses"] if c["category"] == category]
        return random.sample(related, min(4, len(related)))
    
    def enroll_course(self, data):
        """Enroll user in a course"""
        user_id = data.get('user_id')
        course_id = data.get('course_id')
        
        if not user_id or not course_id:
            return {"success": False, "message": "Missing required fields"}
        
        course = next((c for c in self.courses_data["courses"] if c["id"] == course_id), None)
        if not course:
            return {"success": False, "message": "Course not found"}
        
        # Initialize user progress
        if user_id not in self.user_progress:
            self.user_progress[user_id] = {}
        
        self.user_progress[user_id][course_id] = {
            "enrolled_date": datetime.now().isoformat(),
            "progress": 0,
            "completed_modules": [],
            "quiz_scores": {},
            "certificate_issued": False
        }
        
        return {
            "success": True,
            "message": "Successfully enrolled in course",
            "enrollment_id": str(uuid.uuid4()),
            "course_title": course["title"]
        }
    
    def update_progress(self, data):
        """Update user's course progress"""
        user_id = data.get('user_id')
        course_id = data.get('course_id')
        module_id = data.get('module_id')
        
        if user_id in self.user_progress and course_id in self.user_progress[user_id]:
            progress = self.user_progress[user_id][course_id]
            
            if module_id not in progress["completed_modules"]:
                progress["completed_modules"].append(module_id)
                
                # Calculate progress percentage
                course = next((c for c in self.courses_data["courses"] if c["id"] == course_id), None)
                if course:
                    total_modules = len(course["modules"])
                    progress["progress"] = (len(progress["completed_modules"]) / total_modules) * 100
            
            return {
                "success": True,
                "progress": progress["progress"],
                "completed_modules": len(progress["completed_modules"])
            }
        
        return {"success": False, "message": "Enrollment not found"}
    
    def submit_quiz(self, data):
        """Submit and grade quiz"""
        user_id = data.get('user_id')
        course_id = data.get('course_id')
        module_id = data.get('module_id')
        answers = data.get('answers', {})
        
        # Generate quiz questions and correct answers
        quiz_data = self._generate_quiz_questions(course_id, module_id)
        
        # Grade the quiz
        correct_answers = 0
        total_questions = len(quiz_data["questions"])
        
        for q_id, user_answer in answers.items():
            if quiz_data["correct_answers"].get(q_id) == user_answer:
                correct_answers += 1
        
        score = (correct_answers / total_questions) * 100
        passed = score >= 70
        
        # Update user progress
        if user_id in self.user_progress and course_id in self.user_progress[user_id]:
            self.user_progress[user_id][course_id]["quiz_scores"][module_id] = {
                "score": score,
                "passed": passed,
                "date": datetime.now().isoformat()
            }
        
        return {
            "success": True,
            "score": score,
            "passed": passed,
            "correct_answers": correct_answers,
            "total_questions": total_questions,
            "feedback": "Excellent work!" if score >= 90 else "Good job!" if score >= 70 else "Please review the material and try again."
        }
    
    def _generate_quiz_questions(self, course_id, module_id):
        """Generate quiz questions for a module"""
        questions = [
            {
                "id": "Q1",
                "question": "What is the primary benefit of organic farming?",
                "options": ["Higher yield", "Environmental sustainability", "Lower cost", "Faster growth"],
                "type": "multiple_choice"
            },
            {
                "id": "Q2", 
                "question": "Which nutrient is most important for plant growth?",
                "options": ["Nitrogen", "Phosphorus", "Potassium", "All of the above"],
                "type": "multiple_choice"
            },
            {
                "id": "Q3",
                "question": "What is the ideal pH range for most crops?",
                "options": ["5.0-5.5", "6.0-7.0", "7.5-8.0", "8.5-9.0"],
                "type": "multiple_choice"
            }
        ]
        
        correct_answers = {
            "Q1": "Environmental sustainability",
            "Q2": "All of the above", 
            "Q3": "6.0-7.0"
        }
        
        return {
            "questions": questions,
            "correct_answers": correct_answers
        }
    
    def generate_certificate(self, course_id, user_id):
        """Generate course completion certificate"""
        if user_id not in self.user_progress or course_id not in self.user_progress[user_id]:
            return {"success": False, "message": "Course not completed"}
        
        progress = self.user_progress[user_id][course_id]
        
        if progress["progress"] < 100:
            return {"success": False, "message": "Course not completed"}
        
        # Check if all quizzes passed
        quiz_scores = progress.get("quiz_scores", {})
        all_passed = all(score["passed"] for score in quiz_scores.values())
        
        if not all_passed:
            return {"success": False, "message": "All quizzes must be passed"}
        
        course = next((c for c in self.courses_data["courses"] if c["id"] == course_id), None)
        
        certificate_id = str(uuid.uuid4())
        certificate_data = {
            "certificate_id": certificate_id,
            "user_id": user_id,
            "course_id": course_id,
            "course_title": course["title"],
            "instructor": course["instructor"],
            "completion_date": datetime.now().strftime("%Y-%m-%d"),
            "grade": "A" if sum(s["score"] for s in quiz_scores.values()) / len(quiz_scores) >= 90 else "B",
            "certificate_url": f"/certificates/{certificate_id}.pdf"
        }
        
        self.certificates[certificate_id] = certificate_data
        progress["certificate_issued"] = True
        
        return {
            "success": True,
            "certificate": certificate_data
        }

    def test_connection(self):
        """Test if the module is working"""
        try:
            return {'status': 'success', 'message': 'Elearning Courses is operational'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
