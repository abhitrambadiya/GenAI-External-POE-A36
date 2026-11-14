"""Configuration management for Research Analyst Assistant.

Handles environment variable loading, secret sanitization, and runtime defaults.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file
load_dotenv(BASE_DIR / ".env", override=True)

GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "").strip()
GROQ_MODEL: str = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b").strip()

HOST: str = os.getenv("HOST", "127.0.0.1").strip()
PORT: int = int(os.getenv("PORT", "8000").strip())
REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "60").strip())

RESEARCH_DISCLAIMER: str = (
    "Disclaimer: Research Analyst Assistant provides educational and informational market analysis "
    "and research guidance only. It does not constitute formal financial, investment, legal, or tax advice. "
    "Consult a licensed financial advisor or conduct independent due diligence before making capital allocation decisions."
)


def is_groq_configured() -> bool:
    """Check if a valid Groq API key is present in environment."""
    dummy_values = {
        "",
        "gsk_your_actual_groq_api_key_here",
        "placeholder",
        "your_groq_api_key_here",
    }
    return bool(GROQ_API_KEY and GROQ_API_KEY not in dummy_values)


def get_active_model_name() -> str:
    """Return the active model name."""
    return GROQ_MODEL or "llama-3.3-70b-versatile"
