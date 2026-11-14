"""Tests for Health and Frontend Endpoints."""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    """Verify /health returns 200 and lists all 3 Agno agents."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "healthy"
    assert "Research Analyst" in data["app_name"]
    assert "model" in data
    assert isinstance(data["groq_configured"], bool)

    agents = data["agents"]
    assert len(agents) == 3
    assert "Query Analyzer" in agents
    assert "Research Agent" in agents
    assert "Answer Reviewer" in agents


def test_root_serves_frontend():
    """Verify GET / returns 200 and serves HTML interface."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")
    assert "Research Analyst" in response.text
    assert "Query Analyzer" in response.text
