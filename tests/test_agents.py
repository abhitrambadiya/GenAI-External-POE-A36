"""Tests for Multi-Agent Architecture, Team Coordination, and Library Retrieval."""

from app.agents.team import AGENT_NAMES, build_team
from app.agents.tools import (
    clear_consulted_sources,
    get_last_consulted_sources,
    search_library,
)


def test_agent_names_list():
    """Verify exactly 3 designated agents are present."""
    assert len(AGENT_NAMES) == 3
    assert "Query Analyzer" in AGENT_NAMES
    assert "Research Agent" in AGENT_NAMES
    assert "Answer Reviewer" in AGENT_NAMES


def test_build_team():
    """Verify Agno Team composition, members, and tool attachments."""
    team = build_team(api_key="mock_test_key_xyz")
    assert team.name == "Research Analyst Team"
    assert len(team.members) == 3

    member_names = [m.name for m in team.members]
    assert "Query Analyzer" in member_names
    assert "Research Agent" in member_names
    assert "Answer Reviewer" in member_names

    # Check that Research Agent has search_library tool attached
    research_agent = next(m for m in team.members if m.name == "Research Agent")
    assert research_agent.tools is not None
    assert len(research_agent.tools) >= 1
    assert any(getattr(t, "__name__", "") == "search_library" for t in research_agent.tools)


def test_search_library_semiconductors():
    """Verify search tool returns semiconductor outlook for hardware/capex queries."""
    clear_consulted_sources()
    result = search_library("semiconductor gpu accelerator capex")
    assert "Semiconductor" in result or "TAM" in result
    sources = get_last_consulted_sources()
    assert any("Global Semiconductor" in s for s in sources)


def test_search_library_saas():
    """Verify search tool returns SaaS benchmarks for net retention and multiples queries."""
    clear_consulted_sources()
    result = search_library("enterprise saas net retention rule of 40 multiples")
    assert "Rule of 40" in result or "SaaS" in result
    sources = get_last_consulted_sources()
    assert any("Enterprise SaaS Benchmarks" in s for s in sources)


def test_search_library_empty_query():
    """Verify graceful handling and guidance on empty search query."""
    result = search_library("")
    assert "No query provided" in result
