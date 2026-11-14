# KIT's College of Engineering (Autonomous), Kolhapur
## Department of Computer Science & Engineering
### Course: Generative and Agentic AI Lab (UAMPC0731) — External PoE
**Roll No:** `36` (Even) | **Assignment No:** 10 | **Title:** Research Analyst Multi-Agent Assistant — Containerization & DevOps

---

## 1. Title, Aim, and Problem Statement

### **Title:**
Development, Multi-Agent Orchestration, and Containerized Deployment of an Autonomous Research Analyst Assistant using Agno Framework, Groq API, FastAPI, and Docker/Kubernetes.

### **Aim / Objective:**
To design, implement, and containerize an autonomous multi-agent research analysis system capable of decomposing complex business, financial, and technological queries, grounding insights using an authentic empirical knowledge library, cross-examining assertions to eliminate hallucinations, and deploying the solution using modern DevOps practices (Docker, Docker Compose, Kubernetes, CI/CD).

### **Problem Statement (Even Roll Numbers):**
Design and deploy a containerized **Research Analyst Multi-Agent System** that coordinates three specialized agents (`Query Analyzer`, `Research Agent`, and `Answer Reviewer`) using Agno's `TeamMode.coordinate`, backed by fast inference on Groq open-weight models, exposed via FastAPI REST endpoints and Streamlit UI.

---

## 2. Hand-Drawable Diagrams for Answer Sheet

### Diagram 1: Multi-Agent System Architecture (Hand-Drawable Box Diagram)

*Draw this box-and-arrow diagram prominently on your sheet:*

```text
       +-------------------------------------------------------------+
       |                         USER QUERY                          |
       |  "Analyze AI Semiconductor CapEx & Accelerator TAM to 2028" |
       +------------------------------+------------------------------+
                                      |
                                      v
       +=============================================================+
       |               AGNO MULTI-AGENT TEAM ENGINE                  |
       |                (TeamMode.coordinate + Groq)                 |
       |                                                             |
       |  +-------------------------------------------------------+  |
       |  |  AGENT 1: QUERY ANALYZER                              |  |
       |  |  * Classifies domain (Semi, SaaS, Macro, CleanTech)   |  |
       |  |  * Extracts quantitative variables & time horizons    |  |
       |  |  * Formulates targeted research questions             |  |
       |  +---------------------------+---------------------------+  |
       |                              |                              |
       |                              v                              |
       |  +-------------------------------------------------------+  |
       |  |  AGENT 2: RESEARCH AGENT                              |  |
       |  |  * Executes `search_library` tool                     |  |
       |  |  * Queries Grounding Knowledge Library                |  |
       |  |  * Cites empirical metrics, CAGRs, multiples, tables  |  |
       |  +---------------------------+---------------------------+  |
       |                              |                              |
       |                              v                              |
       |  +-------------------------------------------------------+  |
       |  |  AGENT 3: ANSWER REVIEWER                             |  |
       |  |  * Audits claims against library evidence             |  |
       |  |  * Eliminates speculation & hallucinations            |  |
       |  |  * Synthesizes final structured research memo         |  |
       |  +-------------------------------------------------------+  |
       +==============================+==============================+
                                      |
                                      v
       +-------------------------------------------------------------+
       |                    FINAL STRUCTURED OUTPUT                  |
       |  1. Domain Breakdown & Facts | 2. Empirical Findings        |
       |  3. Strategic Insights       | 4. Consulted Sources Cited   |
       |  5. Mandatory Disclaimer                                    |
       +-------------------------------------------------------------+
```

---

### Diagram 2: Docker Multi-Container Orchestration Architecture

*Draw this to illustrate Docker Compose and networking:*

```text
                                 [ Host Browser ]
                                  |            |
                  Port 8000       |            |   Port 8501
            +---------------------+            +---------------------+
            |                                                        |
            v                                                        v
+------------------------------------+   +------------------------------------+
| CONTAINER 1: research-analyst-api  |   | CONTAINER 2: research-analyst-ui   |
| (FastAPI Backend + SPA Frontend)   |   | (Streamlit Interactive Interface)  |
|                                    |   |                                    |
| * Port: 8000                       |   | * Port: 8501                       |
| * Endpoints: GET /, /health, /ask  |   | * Command: streamlit run           |
| * Healthcheck: curl /health        |   | * Healthcheck: curl /_stcore/health|
| * Env: GROQ_API_KEY, GROQ_MODEL    |   | * Mounts: streamlit_app.py         |
+-----------------+------------------+   +-----------------+------------------+
                  |                                        |
                  +-------------------+--------------------+
                                      |
                       Internal Docker Network Bridge
                        (genaiexternalpoea36_default)
                                      |
                                      v
                        [ Groq Cloud API Endpoint ]
                       (llama-3.3-70b / qwen3.8-27b)
```

---

### Diagram 3: Kubernetes Cloud-Native Deployment Topology

*Draw this for the K8s cluster question:*

```text
               [ External Client Traffic ]
                           |
                           v
               [ Ingress Controller: NGINX ]
               (Host: research-analyst.local)
                           |
                           v
               [ Service: ClusterIP (Port 80) ]
                           |
             +-------------+-------------+
             |                           |
             v                           v
+-------------------------+ +-------------------------+
| Pod 1: Replica 1        | | Pod 2: Replica 2        |
| - Container Port: 8000  | | - Container Port: 8000  |
| - Liveness: /health     | | - Liveness: /health     |
| - Readiness: /health    | | - Readiness: /health    |
| - Limits: 1Gi / 1000m   | | - Limits: 1Gi / 1000m   |
| - Requests: 512Mi / 250m| | - Requests: 512Mi / 250m|
+------------+------------+ +------------+------------+
             |                           |
             +-------------+-------------+
                           |
           +---------------+---------------+
           |                               |
           v                               v
[ ConfigMap: App Config ]       [ Secret: GROQ_API_KEY ]
(HOST, PORT, GROQ_MODEL)        (Base64 Encoded Key)
```

---

## 3. Core Theory Points to Write in Answers

### A. What is an Autonomous Agent vs LLM Chain?
* **LLM Chain (Sequential):** Executes fixed, pre-programmed prompt-response steps without reasoning or adaptive tool invocation.
* **Autonomous Agent:** Possesses reasoning loops (ReAct — Reason, Act, Observe), uses memory, tools, and goals to dynamically decide which action to take.
* **Multi-Agent Coordination (Agno Team):** Multiple specialized agents interact with dedicated system prompts, distinct tools, and roles to solve complex tasks cooperatively.

### B. Why Agno Framework?
1. **Lightweight & Fast:** Minimal overhead compared to heavier legacy orchestration frameworks.
2. **First-Class Team Support:** Built-in `TeamMode.coordinate`, `TeamMode.round_robin`, etc.
3. **Native Tool Integration:** Tools are standard typed Python functions with automatic schema conversion.
4. **Model Agnostic:** Seamless provider switching (Groq, Gemini, OpenAI, Claude).

### C. Why Groq API & LPUs?
* **LPU (Language Processing Unit):** Purpose-built chip for sequential tensor processing, offering 300–800 tokens/second throughput.
* **Low Latency:** Multi-agent workflows require sequential LLM passes; Groq reduces end-to-end multi-agent execution from 20s to < 2.5s.
* **Open-Weight Models:** Runs state-of-the-art open models like `qwen/qwen3.8-27b` and `llama-3.3-70b-versatile`.

---

## 4. REST API Specification

### Endpoint 1: `GET /`
* **Purpose:** Serves the responsive single-page HTML frontend.
* **Response Status:** `200 OK` (`text/html`)

### Endpoint 2: `GET /health`
* **Purpose:** Returns system operational status, active model, and registered agent roles without leaking secrets.
* **Request:** No parameters.
* **Response Status:** `200 OK` (`application/json`)
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

### Endpoint 3: `POST /ask`
* **Purpose:** Submits a query for multi-agent investigation and review.
* **Request Body:**
```json
{
  "question": "What is the projected capital expenditure growth and accelerator TAM for generative AI semiconductor infrastructure through 2028?"
}
```
* **Response Status:** `200 OK` (`application/json`)
```json
{
  "status": "success",
  "question": "What is the projected capital expenditure growth...",
  "answer": "### 1. Classification & Domain Breakdown\n- **Primary Domain**: Semiconductors & AI Hardware\n...",
  "sources": [
    "Global Semiconductor & AI Infrastructure Market Outlook (2024-2028)"
  ],
  "disclaimer": "Disclaimer: Research Analyst Assistant provides educational and informational market analysis and research guidance only..."
}
```

---

## 5. DevOps & Containerization Theory Points

### 1. Dockerfile Best Practices Implemented:
* **Base Image:** `python:3.12-slim` (minimal footprint, reduced CVE vulnerability surface).
* **Environment Variables:** `PYTHONDONTWRITEBYTECODE=1`, `PYTHONUNBUFFERED=1` (prevents `.pyc` clutter, ensures immediate log streaming to container stdout).
* **Layer Caching:** Copies `requirements.txt` first and installs dependencies before copying application code.
* **Built-in Healthcheck:** Periodically executes `curl -f http://127.0.0.1:8000/health` with 30s interval and 3 retries.

### 2. Docker Compose (Multi-Container Orchestration):
* **Service 1 (`api`):** FastAPI backend + single-page UI on port `8000:8000`.
* **Service 2 (`streamlit`):** Streamlit analytics dashboard on port `8501:8501`.
* **Service Dependencies:** `depends_on: { api: { condition: service_healthy } }` ensures the Streamlit UI only starts after the API passes healthchecks.
* **Volume Isolation:** Read-only bind mounts (`:ro`) prevent accidental modification of production container code.

### 3. Kubernetes (Cloud-Native Deployment):
* **ConfigMaps:** Stores non-confidential configurations (`HOST`, `PORT`, `GROQ_MODEL`).
* **Secrets:** Encrypts sensitive credentials (`GROQ_API_KEY`).
* **Deployment (2 Replicas):** Ensures high availability, zero-downtime rolling updates, and self-healing pods.
* **Resource Limits:** `requests` (250m CPU, 512Mi RAM) prevent node starvation; `limits` (1000m CPU, 1Gi RAM) prevent container runaway OOM.
* **Liveness & Readiness Probes:** Routes traffic only to healthy pods and restarts crashed containers automatically.
* **ClusterIP Service:** Exposes pods internally on port 80.
* **Ingress:** Routes external domain traffic (`research-analyst.local`) to the backend service.

### 4. CI/CD Pipeline (GitHub Actions):
* **Trigger:** Triggers on `push` and `pull_request` to `main`/`master`.
* **Stage 1 (Test):** Sets up Python 3.12, installs dependencies, runs `pytest -v` across all 12 tests.
* **Stage 2 (Build & Smoke Test):** Triggers `docker/build-push-action`, spins up the built image, checks `/health`, and safely logs out.

---

## 6. High-Frequency Viva Voce Questions & Model Answers

**Q1: Why did you use three agents instead of one large prompt?**  
*Answer:* Single large prompts suffer from instruction dilution, recency bias, and hallucinations. Decomposing the task into a modular triad (Query Analyzer for scoping, Research Agent with tools for empirical grounding, and Answer Reviewer for adversarial fact-checking) ensures separation of concerns, deterministic tool execution, and high factual fidelity.

**Q2: What is the purpose of `TeamMode.coordinate` in Agno?**  
*Answer:* In coordinate mode, agents work under a coordinated orchestration pattern where the output of the analyzer feeds the researcher's query, and the researcher's empirical grounding is audited by the reviewer before synthesizing the final output.

**Q3: How does the `search_library` tool work without a full vector database?**  
*Answer:* The tool uses multi-token weighted keyword and domain category scoring over structured reference documents, tracking consulted titles in a session set, and returning top-scoring excerpts to ground the agent without external network dependencies.

**Q4: Why is input validation performed using Pydantic?**  
*Answer:* Pydantic enforces strict runtime type checking and custom validators (`min_length=5`, whitespace stripping). Queries with fewer than 5 characters or empty whitespace payloads are rejected with HTTP 422 before reaching the LLM, saving inference compute and preventing empty prompt errors.

**Q5: What is the difference between a Liveness Probe and a Readiness Probe in Kubernetes?**  
*Answer:*  
* **Liveness Probe:** Checks if the container is running. If it fails, Kubernetes kills and restarts the pod.  
* **Readiness Probe:** Checks if the container is ready to accept incoming traffic. If it fails, Kubernetes removes the pod from the Service endpoints without killing it until it becomes healthy.
