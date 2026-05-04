import random

def get_ai_response(user_input):
    user_input = user_input.lower().strip()

    # 🎯 ROLE DATA
    roles = {
        "data scientist": {
            "skills": [
                "Python, Statistics, Machine Learning",
                "Pandas, NumPy, Scikit-learn",
                "Data Visualization, SQL",
                "Basic Deep Learning and NLP"
            ],
            "projects": [
                "House Price Prediction",
                "Customer Segmentation",
                "Spam Detection System",
                "Sentiment Analysis (NLP)"
            ],
            "roadmap": [
                "Learn Python basics",
                "Understand statistics & probability",
                "Study ML algorithms",
                "Work on real datasets (Kaggle)",
                "Build and deploy projects"
            ],
            "tips": [
                "Focus on data understanding",
                "Explain insights clearly",
                "Practice real-world datasets",
                "Build strong portfolio"
            ]
        },

        "data engineer": {
            "skills": [
                "SQL, Python",
                "ETL pipelines",
                "Apache Airflow, Spark",
                "Cloud (AWS/Azure)"
            ],
            "projects": [
                "ETL Pipeline Project",
                "Data Warehouse Design",
                "Streaming Data Pipeline"
            ],
            "roadmap": [
                "Learn SQL deeply",
                "Understand databases",
                "Learn ETL tools",
                "Work with big data tools"
            ],
            "tips": [
                "Focus on scalability",
                "Work with real-time data",
                "Understand distributed systems"
            ]
        },

        "ml engineer": {
            "skills": [
                "Python, Machine Learning",
                "Deep Learning (TensorFlow/PyTorch)",
                "Model Deployment",
                "MLOps basics"
            ],
            "projects": [
                "Image Classification",
                "Recommendation System",
                "ML Model Deployment"
            ],
            "roadmap": [
                "Learn ML fundamentals",
                "Study deep learning",
                "Learn deployment tools",
                "Build end-to-end projects"
            ],
            "tips": [
                "Focus on deployment",
                "Learn APIs & backend",
                "Optimize models"
            ]
        },

        "cloud engineer": {
            "skills": [
                "AWS/Azure/GCP",
                "Docker, Kubernetes",
                "Networking",
                "CI/CD pipelines"
            ],
            "projects": [
                "Deploy app on AWS",
                "CI/CD pipeline",
                "Containerized app"
            ],
            "roadmap": [
                "Learn cloud basics",
                "Practice deployment",
                "Understand architecture"
            ],
            "tips": [
                "Get certifications",
                "Work on real cloud setups"
            ]
        },

        "data analyst": {
            "skills": [
                "Excel, SQL, Python",
                "Power BI / Tableau",
                "Data Cleaning",
                "Visualization"
            ],
            "projects": [
                "Sales Dashboard",
                "Customer Analysis",
                "Business Insights Dashboard"
            ],
            "roadmap": [
                "Learn Excel & SQL",
                "Practice visualization",
                "Work on real datasets"
            ],
            "tips": [
                "Focus on storytelling",
                "Improve communication"
            ]
        }
    }

    # 🔍 ROLE-BASED RESPONSE
    for role in roles:
        if role in user_input:
            data = roles[role]
            response = f"🎯 Role: {role.title()}\n\n"

            if "skill" in user_input:
                response += "💡 Skills Required:\n"
                for s in data["skills"]:
                    response += f"• {s}\n"

            if "project" in user_input:
                response += "\n📁 Recommended Projects:\n"
                for p in data["projects"]:
                    response += f"• {p}\n"

            if "roadmap" in user_input or "how" in user_input:
                response += "\n🛣️ Roadmap:\n"
                for r in data["roadmap"]:
                    response += f"• {r}\n"

            response += "\n🔥 Pro Tips:\n"
            for t in data["tips"]:
                response += f"• {t}\n"

            return response

    # 🔧 ML-SPECIFIC PROJECT DETECTION
    if "project" in user_input:
        if "ml" in user_input or "machine learning" in user_input:
            return """📁 Machine Learning Project Ideas:
• House Price Prediction
• Movie Recommendation System
• Spam Email Classifier
• Sentiment Analysis (NLP)

🔥 Pro Tips:
• Use real datasets (Kaggle)
• Deploy using Streamlit
• Show accuracy metrics"""

        else:
            return """📁 General Project Ideas:
• Resume Analyzer
• Dashboard (Power BI)
• Chatbot Application

🔥 Pro Tips:
• Solve real-world problems
• Add GitHub projects
• Explain your project clearly"""

    # 🔹 GENERAL RESPONSES
    if "skill" in user_input:
        return "Focus on Python, SQL, Machine Learning, and communication skills."

    elif "resume" in user_input:
        return "Keep resume concise, use bullet points, and add measurable achievements."

    elif "interview" in user_input:
        return "Prepare DSA, core subjects, and practice mock interviews."

    elif "hello" in user_input or "hi" in user_input:
        return "Hi! I can help you with skills, roles, projects, and career guidance."

    return "Ask about roles (Data Scientist, ML Engineer, etc.), skills, projects, or roadmap."
