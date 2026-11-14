"""Tests for Input Validation and Error Handling."""

from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ask_empty_payload():
    """Verify empty POST payload returns 422 Unprocessable Entity."""
    response = client.post("/ask", json={})
    assert response.status_code == 422


def test_ask_short_question():
    """Verify question below 5 characters is rejected with 422."""
    response = client.post("/ask", json={"question": "gdp?"})
    assert response.status_code == 422


def test_ask_whitespace_only():
    """Verify question containing only whitespace is rejected with 422."""
    response = client.post("/ask", json={"question": "          "})
    assert response.status_code == 422


def test_ask_missing_api_key(monkeypatch):
    """Verify 503 Service Unavailable when GROQ_API_KEY is not configured."""
    monkeypatch.setattr("app.config.GROQ_API_KEY", "")
    response = client.post(
        "/ask",
        json={"question": "What is the expected hyperscaler CapEx allocation for AI semiconductors?"}
    )
    assert response.status_code == 503
    data = response.json()
    assert "GROQ_API_KEY is not configured" in data["detail"]


def test_ask_success_with_mocked_workflow(monkeypatch):
    """Verify successful response formatting when workflow returns answer and sources."""
    monkeypatch.setattr("app.config.GROQ_API_KEY", "mock_valid_key_123")

    mock_result = {
        "answer": "AI accelerator total addressable market is expected to expand at 34.2% CAGR to $280B by 2028.",
        "sources": ["Global Semiconductor & AI Infrastructure Market Outlook (2024-2028)"],
    }

    with patch("app.main.run_workflow", return_value=mock_result):
        response = client.post(
            "/ask",
            json={"question": "What is the forecasted CAGR and TAM for AI accelerators?"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "34.2% CAGR" in data["answer"]
        assert "Global Semiconductor & AI Infrastructure Market Outlook (2024-2028)" in data["sources"]
        assert "Disclaimer:" in data["disclaimer"]
