🚀 Gemini-Powered FastAPI Intelligent Query Chatbot

An AI-powered backend application that allows users to query network equipment and POP (Point of Presence) data using natural language, powered by Google Gemini LLM and FastAPI.

This project demonstrates how Large Language Models (LLMs) can intelligently interpret user queries, identify relevant data sources, generate optimized database queries, and return precise results — without exposing sensitive enterprise data.

🧠 Key Features
	•	🔍 Natural Language Querying
	•	Ask questions like:
	•	“Show all switches with model X from Juniper”
	•	🤖 Gemini LLM Integration
	•	Uses Gemini for intent understanding and query normalization
	•	🗄️ Multi-Database Support
	•	Works with separate equipment and pop databases
	•	⚡ FastAPI Backend
	•	High-performance, scalable API
	•	🧩 Modular & Clean Architecture
	•	Repository pattern for database operations
	•	🔐 Enterprise-Safe Design
	•	No confidential data exposed publicly

🏗️ Project Architecture
├── app.py              # FastAPI application entry
├── main.py             # App launcher
├── chatbot.py          # Gemini-based query interpreter
├── connection.py       # Database connection handler
├── equipment_repo.py   # Equipment database queries
├── pop_repo.py         # POP database queries
├── schema.py           # Response schemas
├── config.yaml         # Configuration file (ignored)
├── requirements.txt    # Dependencies
└── README.md

⚙️ Tech Stack
	•	Python
	•	FastAPI
	•	Google Gemini LLM
	•	SQLite
	•	PyYAML
	•	Pandas
	•	Rich (for logging & debugging)

🔐 Data Privacy & Security

⚠️ Important Notice
  •	Actual databases (equipment.db, pop.db) are NOT included in this repository
  •	Databases contain confidential enterprise data
  •	Only application logic and AI workflow are shared 

📄 License

This project is for educational and demonstration purposes.
Commercial usage of actual data is restricted.
