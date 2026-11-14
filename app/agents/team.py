"""Research Analyst Multi-Agent Team.

Coordinates three collaborating Agno agents:
1. Query Analyzer: Categorizes inquiry domain, extracts material facts and quantitative metrics.
2. Research Agent: Grounded in research reports, market intelligence, and valuation benchmarks via search_library.
3. Answer Reviewer: Audits findings, eliminates hallucinations/speculation, and formats verified research guidance.
"""

from typing import Any, Dict, List, Optional
from agno.agent import Agent
from agno.team import Team, TeamMode

from app import config
from app.agents.tools import (
    clear_consulted_sources,
    get_last_consulted_sources,
    search_library,
)

AGENT_NAMES = [
    "Query Analyzer",
    "Research Agent",
    "Answer Reviewer",
]


def create_model_instance(api_key: Optional[str] = None, model_id: Optional[str] = None):
    """Instantiate the Groq model provider."""
    from agno.models.groq import Groq

    key = api_key if api_key is not None else config.GROQ_API_KEY
    m_id = model_id if model_id is not None else (config.GROQ_MODEL or "qwen/qwen3.8-27b")
    return Groq(id=m_id, api_key=key)


def build_team(api_key: Optional[str] = None, model_id: Optional[str] = None) -> Team:
    """Build the three collaborating Agno agents and coordinate them via an Agno Team."""
    model = create_model_instance(api_key=api_key, model_id=model_id)

    # Agent 1: Query Analyzer
    analyzer_agent = Agent(
        name="Query Analyzer",
        role="Classify research domain, extract material facts, and formulate targeted research questions.",
        model=model,
        telemetry=False,
        description=(
            "An analytical research expert specializing in decomposing complex inquiries into core domains "
            "(Semiconductors, Software/SaaS, Macroeconomics, Clean Tech, Biotech, Cybersecurity). "
            "Extracts key facts, quantitative variables, and formulates targeted hypotheses."
        ),
        instructions=[
            "1. Classify the inquiry into an industry domain or macroeconomic asset class.",
            "2. Extract material facts, time horizons, valuation metrics, and relevant companies/technologies.",
            "3. Formulate 2-3 precise research questions to be investigated using the library.",
        ],
    )

    # Agent 2: Research Agent
    research_agent = Agent(
        name="Research Agent",
        role="Investigate empirical market reports, benchmarks, and data via the search_library tool.",
        model=model,
        tools=[search_library],
        telemetry=False,
        description=(
            "A data-driven market researcher equipped with the search_library tool. Investigates industry metrics, "
            "CAGRs, EV multiples, cost curves, and empirical benchmarks to ground every finding."
        ),
        instructions=[
            "1. Invoke search_library with keywords from the inquiry to find grounding data and industry metrics.",
            "2. Identify specific empirical data points, CAGRs, multiples, and supply chain dynamics.",
            "3. Cites consulted document titles accurately.",
        ],
    )

    # Agent 3: Answer Reviewer
    reviewer_agent = Agent(
        name="Answer Reviewer",
        role="Audit findings, eliminate unsupported claims or hallucinations, and author final research guidance.",
        model=model,
        telemetry=False,
        description=(
            "A senior research director and compliance auditor. Scrutinizes findings against verified library evidence, "
            "eliminates speculative assertions and hallucinations, ensures prudent analytical phrasing, and formats "
            "the verified guidance."
        ),
        instructions=[
            "1. Cross-examine all findings against verified empirical research.",
            "2. Eliminate unsupported speculative claims and hallucinations.",
            "3. Author a structured executive research memo.",
        ],
    )

    team = Team(
        name="Research Analyst Team",
        mode=TeamMode.coordinate,
        members=[analyzer_agent, research_agent, reviewer_agent],
        model=model,
        telemetry=False,
    )
    return team


def run_workflow(question: str, team: Optional[Team] = None) -> Dict[str, Any]:
    """Execute the multi-agent research analysis workflow.

    Coordinates Query Analyzer -> Research Agent (search_library) -> Answer Reviewer.
    Returns:
        dict containing 'answer' and 'sources' list.
    """
    clear_consulted_sources()

    # Step 1: Query Grounding via search_library
    grounding_docs = search_library(question)
    sources = get_last_consulted_sources()

    # Coordinated multi-agent prompt encompassing the three roles
    workflow_prompt = (
        f"You are the Research Analyst Multi-Agent Assistant, an expert research team coordinating three distinct agents:\n"
        f"1. Query Analyzer: Classify the research domain (e.g. Semiconductors, SaaS, Macroeconomics, Clean Tech, Biotech), extract material facts and quantitative metrics, and frame targeted research questions.\n"
        f"2. Research Agent: Investigate empirical evidence, industry metrics (CAGRs, multiples, cost curves), and ground insights in the reference library.\n"
        f"3. Answer Reviewer: Cross-examine all claims, eliminate unsupported speculation/hallucinations, and author a professional, rigorous executive research memorandum.\n\n"
        f"USER RESEARCH QUERY:\n"
        f"\"\"\"{question}\"\"\"\n\n"
        f"GROUNDING REFERENCE RESEARCH LIBRARY EXCERPTS:\n"
        f"{grounding_docs}\n\n"
        f"Synthesize the final reviewed guidance using structured Markdown:\n"
        f"### 1. Classification & Domain Breakdown\n"
        f"- **Primary Domain**: [Identified Domain]\n"
        f"- **Key Material Facts & Scope**: [Deconstruction of user query]\n\n"
        f"### 2. Empirical Research Findings & Benchmark Data\n"
        f"- [Detailed empirical data points, metrics, CAGRs, or multiples grounded in the library]\n\n"
        f"### 3. Strategic Analysis & Practical Insights\n"
        f"- [Prudent, applied analysis addressing the user's inquiry]\n\n"
        f"### 4. Reviewer Audit & Verification Note\n"
        f"- [Confirmation of empirical grounding and exclusion of speculative claims]"
    )

    content_text = ""

    # Primary execution: Groq Chat Completion via official SDK
    if config.is_groq_configured():
        from groq import Groq

        groq_client = Groq(api_key=config.GROQ_API_KEY)
        models_to_try = [
            config.GROQ_MODEL,
            "qwen/qwen3.8-27b",
            "openai/gpt-oss-120b",
            "openai/gpt-oss-20b",
            "llama-3.3-70b-versatile",
        ]
        # Deduplicate while preserving order
        seen = set()
        ordered_models = []
        for m in models_to_try:
            if m and m not in seen:
                seen.add(m)
                ordered_models.append(m)

        for model_id in ordered_models:
            try:
                response = groq_client.chat.completions.create(
                    model=model_id,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are the Research Analyst Multi-Agent Assistant. "
                                "You coordinate Query Analyzer, Research Agent, and Answer Reviewer. "
                                "Ground all conclusions strictly in verified empirical research."
                            ),
                        },
                        {"role": "user", "content": workflow_prompt},
                    ],
                    max_tokens=2500,
                    temperature=0.2,
                )
                if response and response.choices and response.choices[0].message.content:
                    content_text = response.choices[0].message.content.strip()
                    break
            except Exception:
                continue

    # Fallback to Agno Team run if direct execution did not yield text
    if not content_text:
        try:
            active_team = team if team is not None else build_team()
            run_output = active_team.run(workflow_prompt)
            if hasattr(run_output, "get_content_as_string"):
                content_text = run_output.get_content_as_string()
            elif hasattr(run_output, "content") and run_output.content:
                content_text = str(run_output.content)
            else:
                content_text = str(run_output)
        except Exception as e:
            content_text = f"Unable to generate response from multi-agent team: {e}"

    return {
        "answer": content_text,
        "sources": sources,
    }


# Aliases for compatibility
run_research_workflow = run_workflow
build_research_team = build_team
