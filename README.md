# 📊 Research Analyst — Multi-Agent Assistant

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Agno Framework](https://img.shields.io/badge/Agno-TeamMode.coordinate-purple.svg)](https://github.com/agno-agi/agno)
[![Groq API](https://img.shields.io/badge/Groq-Fast%20Open--Weights-orange.svg)](https://console.groq.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com)
[![Tests Passing](https://img.shields.io/badge/Tests-12%20Passed-brightgreen.svg)](#-running-automated-tests)

---

### **Academic Information**
* **Institution:** KIT's College of Engineering (Autonomous), Kolhapur  
* **Department:** Department of Computer Science & Engineering  
* **Course Name:** Generative and Agentic AI Lab  
* **Course Code:** `UAMPC0731`  
* **Examination:** External PoE A.Y. 2026-2027  
* **Student Roll Number:** `36` (**Even Roll Number**)  
* **Assigned Problem:** **Assignment No. 10 — Research Analyst Agents**

---

## 🏛️ Multi-Agent Architecture

The assistant coordinates exactly **three collaborating agents** via the Agno Framework (`TeamMode.coordinate`):

```
+-------------------------------------------------------+
|                      User Query                       |
+---------------------------+---------------------------+
                            |
                            v
+-------------------------------------------------------+
|                       Agno Team                       |
|                                                       |
|  1. Query Analyzer                                    |
|     - Classifies research domain (Semi, SaaS, Macro)  |
|     - Extracts material facts & quantitative metrics  |
|     - Formulates targeted research hypotheses         |
|                                                       |
|                           |                           |
|                           v                           |
|  2. Research Agent                                    |
|     - Invokes `search_library` tool                   |
|     - Grounded in empirical reports & benchmarks      |
|     - Cites relevant CAGRs, multiples, and findings   |
|                                                       |
|                           |                           |
|                           v                           |
|  3. Answer Reviewer                                   |
|     - Cross-examines all claims against evidence      |
|     - Strips unsupported / hallucinated points        |
|     - Synthesizes final structured research memo      |
+---------------------------+---------------------------+
                            |
                            v
+-------------------------------------------------------+
|                Final Reviewed Answer                  |
|                + Consulted Sources                    |
|                + Mandatory Disclaimer                 |
+-------------------------------------------------------+
```

### Agent Roles:
1. **Query Analyzer**: Deconstructs user queries into distinct financial and industrial domains (e.g., Semiconductor Infrastructure, Enterprise SaaS Benchmarks, Macroeconomic Policy, Clean Tech Economics, Biotech Pipeline Valuation) and frames precise analytical questions.
2. **Research Agent**: Executes the `search_library` tool to investigate empirical data, market forecasts, valuation multiples, and industry benchmarks to ground all findings in factual evidence.
3. **Answer Reviewer**: Audits claims against available evidence, eliminates speculative assertions and hallucinations, ensures prudent analytical phrasing, and formats the verified guidance.

---

## 📁 Project Structure

```
.
├── .env.example                     # Environment template
├── .env                             # Active configuration (with Groq API Key)
├── .gitignore                       # Git ignore rules
├── .dockerignore                    # Docker ignore rules
├── requirements.txt                 # Python project dependencies
├── README.md                        # Documentation and guide
├── Dockerfile                       # Multi-stage optimized Docker container
├── docker-compose.yml               # Multi-container orchestration (FastAPI + Streamlit)
├── streamlit_app.py                 # Clean, white-themed Streamlit UI
├── app/
│   ├── __init__.py
│   ├── config.py                    # Environment variable loading & sanitization
│   ├── main.py                      # FastAPI application (GET /, POST /ask, GET /health)
│   ├── schemas.py                   # Pydantic request/response validation schemas
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── team.py                  # Agno Team definition and multi-agent coordination
│   │   └── tools.py                 # `search_library` tool for Research Agent
│   ├── data/
│   │   ├── __init__.py
│   │   └── sample_documents.py      # Grounding documents (Semiconductors, SaaS, Macro, Energy, Biotech)
│   └── static/
│       ├── index.html               # Clean single-page user interface
│       ├── style.css                # Modern design system & styling
│       └── app.js                   # Frontend client logic & progress animation
├── tests/
│   ├── __init__.py
│   ├── test_health.py               # Tests for /health and / endpoints
│   ├── test_validation.py           # Tests for input validation and error handling
│   └── test_agents.py               # Tests for Agno agents, Team, and search_library tool
├── k8s/
│   ├── configmap-secret.yaml        # Kubernetes ConfigMap & Secret manifests
│   └── deployment-service-ingress.yaml # Kubernetes Deployment, Service, & Ingress manifests
└── .github/
    └── workflows/
        └── ci.yml                   # CI/CD pipeline (Pytest test suite & Docker build)
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10, 3.11, 3.12, 3.13, or 3.14
- Docker Desktop (for containerization)
- Free Groq API Key from [Groq Console](https://console.groq.com/keys)

### 2. Virtual Environment Setup
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# macOS / Linux:
source .venv/bin/activate
# Windows:
# .venv\Scripts\Activate.ps1

# Install project dependencies
pip install -r requirements.txt
```

### 3. Environment Variable Configuration
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Ensure your `GROQ_API_KEY` is configured in `.env`:
```ini
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
GROQ_MODEL=qwen/qwen3.8-27b
HOST=127.0.0.1
PORT=8000
REQUEST_TIMEOUT=60
```

---

## 💻 Running the Application

### Option A: Streamlit Frontend (Recommended UI)
Run the clean, white-themed Streamlit interface:
```bash
streamlit run streamlit_app.py
```
Open your browser at **[http://localhost:8501](http://localhost:8501)**.

### Option B: FastAPI Backend & API Endpoints
Run the FastAPI application with live reloading:
```bash
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
- **Web UI:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Health Check Endpoint:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

---

## 🧪 Running Automated Tests

Run the complete test suite using `pytest`:
```bash
pytest -v
```

### All 12 Automated Tests:
- `test_health.py::test_health_endpoint` — Verifies `/health` status and all 3 agents
- `test_health.py::test_root_serves_frontend` — Verifies `GET /` serves HTML frontend
- `test_validation.py::test_ask_empty_payload` — Empty request rejected with 422
- `test_validation.py::test_ask_short_question` — Questions < 5 characters rejected with 422
- `test_validation.py::test_ask_whitespace_only` — Whitespace-only queries rejected with 422
- `test_validation.py::test_ask_missing_api_key` — Graceful 503 when GROQ_API_KEY missing
- `test_validation.py::test_ask_success_with_mocked_workflow` — Formatted multi-agent response
- `test_agents.py::test_agent_names_list` — Verifies 3 agent names
- `test_agents.py::test_build_team` — Verifies Agno Team creation and tool attachment
- `test_agents.py::test_search_library_semiconductors` — Search library semiconductor retrieval
- `test_agents.py::test_search_library_saas` — Search library SaaS benchmarks retrieval
- `test_agents.py::test_search_library_empty_query` — Graceful message on empty search

---

## 🔌 API Endpoints

### 1. `GET /`
Serves the responsive single-page web application.

### 2. `GET /health`
Returns health status, active Groq model, and registered multi-agent roles:
```json
{
  "status": "healthy",
  "app_name": "Research Analyst — Multi-Agent Assistant",
  "groq_configured": true,
  "model": "qwen/qwen3.8-27b",
  "agents": [
    "Query Analyzer",
    "Research Agent",
    "Answer Reviewer"
  ]
}
```

### 3. `POST /ask`
Submits a query to the multi-agent team.

**Request Body:**
```json
{
  "question": "What is the projected capital expenditure growth and accelerator TAM for generative AI semiconductor infrastructure through 2028?"
}
```

**Response Body:**
```json
{
  "status": "success",
  "question": "What is the projected capital expenditure growth and accelerator TAM for generative AI semiconductor infrastructure through 2028?",
  "answer": "### 1. Classification & Domain Breakdown\n- **Primary Domain**: Semiconductors & AI Hardware\n...",
  "sources": [
    "Global Semiconductor & AI Infrastructure Market Outlook (2024-2028)"
  ],
  "disclaimer": "Disclaimer: Research Analyst Assistant provides educational and informational market analysis and research guidance only..."
}
```

---

## 🐳 Containerization & DevOps Scope

### 1. Build Docker Image
```bash
docker build -t research-analyst-agent:latest .
```

### 2. Run Container Standalone
```bash
docker run -d --name analyst-app -p 8000:8000 --env-file .env research-analyst-agent:latest
```

### 3. Local Multi-Container Orchestration (Docker Compose)
Spins up both FastAPI backend (port 8000) and Streamlit frontend (port 8501) with health checks:
```bash
docker-compose up -d
```
Check running services:
```bash
docker-compose ps
```

### 4. Cloud-Native Kubernetes Deployment
Deploy ConfigMap, Secret, Deployment (2 replicas with resource limits), Service, and Ingress:
```bash
kubectl apply -f k8s/configmap-secret.yaml
kubectl apply -f k8s/deployment-service-ingress.yaml
```

### 5. Automated CI/CD Pipeline
GitHub Actions workflow configured in `.github/workflows/ci.yml` runs automated `pytest` across Python versions, builds the Docker image, conducts a health check container smoke test, and securely tags the build.
