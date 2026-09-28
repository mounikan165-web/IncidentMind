# IncidentMind 🧠

IncidentMind is an incident-response memory tool that helps engineering teams remember and reuse knowledge from previous production incidents.

Instead of investigating the same type of problem from scratch, engineers can store previous incident information and ask questions about past incidents.

## 🎯 Problem Statement

When production incidents happen, engineers often spend valuable time searching through previous incident reports, notes, and documentation.

Important knowledge about previous incidents can easily be forgotten or scattered across different places.

IncidentMind addresses this problem by providing a persistent memory layer for incident knowledge.

## 💡 Our Solution

IncidentMind uses **Hindsight** as a persistent memory layer.

The workflow is simple:

1. An engineer records information about an incident.
2. IncidentMind stores the incident in Hindsight.
3. When a similar problem happens again, the engineer asks a question.
4. IncidentMind searches its stored incident memory and provides relevant information from previous incidents.

This allows teams to reuse previous operational knowledge during future investigations.

## ✨ Key Features

- 🧠 Persistent incident memory
- 📝 Store production incident notes
- 🔎 Ask questions about previous incidents
- ♻️ Reuse knowledge from previous incidents
- 🌐 Lightweight browser-based interface
- ⚡ FastAPI backend
- 💾 Hindsight-powered memory

## 🏗️ Architecture

```text
User
  ↓
IncidentMind Web Interface
  ↓
FastAPI Backend
  ↓
Hindsight Memory
  ↓
Stored Incident Knowledge
Technology Stack
Python
FastAPI
Hindsight
Hindsight Client
Pydantic
Uvicorn
HTML
CSS
JavaScript
📂 Project Structure
IncidentMind/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── sample_incidents.json
│
└── frontend/
    ├── index.html
    ├── app.js
    └── style.css
🚀 How to Run
1. Clone the repository
git clone https://github.com/mounikan165-web/IncidentMind.git
cd IncidentMind
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
On Windows PowerShell:
.venv\Scripts\Activate.ps1
4. Install dependencies
python -m pip install -r requirements.txt
5. Start the Hindsight server
Start the local Hindsight server separately on:
http://localhost:8888
6. Start IncidentMind
python -m uvicorn app:app --reload
7. Open the application
Open:
http://127.0.0.1:8000
🔎 Example
An engineer can store an incident such as:
Payment API returned 503 errors after deployment v2.4.1. The root cause was an incorrect connection pool configuration. The team fixed it by reverting the configuration and restarting the payment service.
Later, the engineer can ask:
Have we seen a similar Payment API 503 incident before? What caused it and how was it fixed?
IncidentMind uses the stored incident memory to provide relevant information.
🧠 Why Hindsight?
IncidentMind uses Hindsight as its persistent memory layer.
Hindsight allows IncidentMind to retain incident knowledge and retrieve relevant information when engineers ask questions about previous incidents.
🔐 Security
Do not commit sensitive information to the repository.
Never upload:
API keys
Passwords
.env files
Authentication credentials
Private tokens
Virtual environments
👥 Team
Team Name: Binary Duo
Hackathon: Hack With Hyderabad 3.0
🚀 Future Improvements
Future versions of IncidentMind could include:
Automatic incident summarization
Incident similarity detection
Incident severity classification
Integration with monitoring and alerting systems
Integration with issue trackers
Incident analytics and dashboards
Team-based authentication
More advanced incident search
📌 Project Goal
The goal of IncidentMind is to turn
previous incident experience into reusable engineering knowledge,
 helping teams avoid repeatedly solving the same problems from scratch.
