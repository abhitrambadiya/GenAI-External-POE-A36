"""Streamlit Web Interface for Research Analyst — Multi-Agent Assistant.

KIT's College of Engineering (Autonomous), Kolhapur
Department of Computer Science & Engineering
Course: Generative and Agentic AI Lab (Course Code: UAMPC0731)
Roll No: 36 (Even Roll Number: Research Analyst Agents)
"""

import os
from pathlib import Path
import streamlit as st

# Configure page
st.set_page_config(
    page_title="Research Analyst — Multi-Agent Assistant",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom White-Themed CSS
st.markdown("""
<style>
    .main {
        background-color: #fafafa;
    }
    .stApp {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .agent-box {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .source-tag {
        display: inline-block;
        background-color: #f1f5f9;
        color: #334155;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 4px 10px;
        margin: 4px;
        font-size: 13px;
        font-weight: 500;
    }
    .disclaimer-card {
        background-color: #fffbeb;
        border-left: 4px solid #f59e0b;
        color: #92400e;
        padding: 12px 16px;
        border-radius: 4px;
        font-size: 13px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

from app import config
from app.agents.team import AGENT_NAMES, build_team, run_workflow
from app.agents.tools import (
    clear_consulted_sources,
    get_last_consulted_sources,
    search_library,
)
from app.data.sample_documents import SAMPLE_DOCUMENTS

# Sidebar Configuration
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/combo-chart.png", width=64)
    st.title("Research Analyst AI")
    st.caption("Undergraduate GenAI & ML DevOps Coursework")
    st.divider()

    st.subheader("🎓 Academic Context")
    st.markdown("**KIT's College of Engineering (Autonomous)**")
    st.markdown("**Lab:** GenAI & ML DevOps (UAMPC0731)")
    st.markdown("**Roll Number:** `36` (Even)")
    st.info("Assign: Research Analyst Agents (Assignment 10)")

    st.divider()
    st.subheader("⚙️ System Status")
    is_ready = config.is_groq_configured()
    if is_ready:
        st.success(f"Groq API Ready: `{config.get_active_model_name()}`")
    else:
        st.error("Groq API Key Unconfigured in .env")

    st.markdown("**Coordinating Agno Team:**")
    for agent in AGENT_NAMES:
        st.markdown(f"- 🟢 **{agent}**")

    st.divider()
    st.subheader("📚 Grounding Library")
    st.caption(f"{len(SAMPLE_DOCUMENTS)} Grounding Knowledge Documents Indexed")
    with st.expander("View Available Research Titles"):
        for doc in SAMPLE_DOCUMENTS:
            st.markdown(f"• **{doc['title']}** ({doc['category']})")

# Main Content Header
st.title("📊 Research Analyst — Multi-Agent Assistant")
st.markdown(
    "Collaborative multi-agent market intelligence platform powered by **Agno Framework** and **Groq**."
)

# Sample Queries
SAMPLE_PROMPTS = [
    "What is the projected capital expenditure growth and accelerator TAM for generative AI semiconductor infrastructure through 2028?",
    "How do Net Revenue Retention (NRR) and the Rule of 40 correlate with enterprise SaaS valuation multiples?",
    "What is the current estimate for the macroeconomic neutral rate (r*) and how is yield curve disinversion transmitting to debt refinancing?",
    "What are the current lithium-ion battery pack cost curves ($/kWh) and project IRRs for utility-scale battery energy storage?",
    "What is the cumulative clinical phase success probability and industry discount rate (WACC) used in biotechnology pipeline valuation?",
]

selected_prompt = st.selectbox("💡 Choose a sample research topic or write your own below:", ["-- Custom Query --"] + SAMPLE_PROMPTS)

default_text = "" if selected_prompt == "-- Custom Query --" else selected_prompt
user_query = st.text_area("Enter your research question or market analysis topic:", value=default_text, height=100)

col1, col2 = st.columns([1, 4])
with col1:
    submit_button = st.button("🚀 Analyze Query", type="primary", use_container_width=True)
with col2:
    if st.button("🔄 Clear", use_container_width=False):
        st.rerun()

# Execution Flow
if submit_button:
    if not user_query.strip() or len(user_query.strip()) < 5:
        st.warning("Please enter a research inquiry of at least 5 characters.")
    elif not config.is_groq_configured():
        st.error("Cannot run analysis: GROQ_API_KEY is not set in `.env`.")
    else:
        with st.status("Executing Multi-Agent Workflow...", expanded=True) as status:
            st.write("🔍 **Query Analyzer:** Deconstructing query, identifying domain, and extracting material variables...")
            
            st.write("📊 **Research Agent:** Invoking `search_library` and retrieving empirical market benchmarks...")
            grounding_text = search_library(user_query)
            consulted = get_last_consulted_sources()

            st.write("⚖️ **Answer Reviewer:** Cross-examining findings, stripping speculative claims, and formatting memorandum...")
            result = run_workflow(user_query)
            status.update(label="Analysis Complete!", state="complete", expanded=False)

        st.subheader("📄 Verified Research Memorandum")
        
        tab_memo, tab_sources, tab_workflow, tab_library = st.tabs([
            "Executive Memo", "Consulted Sources", "Multi-Agent Breakdown", "Live Library Query"
        ])

        with tab_memo:
            st.markdown(result.get("answer", "No answer generated."))
            st.markdown(f'<div class="disclaimer-card">{config.RESEARCH_DISCLAIMER}</div>', unsafe_allow_html=True)

        with tab_sources:
            st.markdown("### Grounding References Cited:")
            sources = result.get("sources", [])
            if sources:
                for s in sources:
                    st.markdown(f'<span class="source-tag">📄 {s}</span>', unsafe_allow_html=True)
            else:
                st.info("No library documents directly cited.")

        with tab_workflow:
            st.markdown("### Multi-Agent Coordination Breakdown:")
            st.markdown("""
            1. **Query Analyzer**: Decomposed question into core domain, target variables, and hypotheses.
            2. **Research Agent**: Scanned local grounding library with `search_library` tool and extracted relevant empirical excerpts.
            3. **Answer Reviewer**: Audited assertions, verified absence of hallucinations, and synthesized final guidance.
            """)

        with tab_library:
            st.markdown("### Grounding Reference Excerpts Used:")
            st.code(grounding_text)
