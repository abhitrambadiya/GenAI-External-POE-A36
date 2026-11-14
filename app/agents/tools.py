"""Tools for Research Analyst Agno Agents.

Provides access to the research knowledge base and market benchmark library,
allowing the Research Agent to inspect and cite empirical findings, market sizing, and valuation models.
"""

from typing import List, Set
from app.data.sample_documents import SAMPLE_DOCUMENTS

# Query-level consulted source tracker
_last_consulted_sources: Set[str] = set()


def get_last_consulted_sources() -> List[str]:
    """Retrieve document titles consulted during the most recent research session."""
    return sorted(list(_last_consulted_sources))


def clear_consulted_sources() -> None:
    """Reset the consulted sources tracker before starting a new inquiry."""
    _last_consulted_sources.clear()


def search_library(query: str) -> str:
    """Search the research and market intelligence library for relevant benchmarks, statistics, and reports.

    Args:
        query: The search keywords, topic, ticker, sector, or analytical question.

    Returns:
        A formatted string containing relevant excerpts and citations from the research library.
    """
    if not query or not query.strip():
        return "No query provided. Please specify research topics, keywords, or market questions."

    query_tokens = [w.lower().strip("?,.;:\"'()") for w in query.split() if len(w) > 2]
    matched_docs = []

    for doc in SAMPLE_DOCUMENTS:
        score = 0
        doc_keywords = [k.lower() for k in doc.get("keywords", [])]
        title_lower = doc.get("title", "").lower()
        content_lower = doc.get("content", "").lower()
        category_lower = doc.get("category", "").lower()

        for token in query_tokens:
            if token in doc_keywords:
                score += 3
            if token in title_lower:
                score += 4
            if token in category_lower:
                score += 2
            if token in content_lower:
                score += 1

        if score > 0:
            matched_docs.append((score, doc))

    if not matched_docs:
        available_titles = ", ".join(f"'{d['title']}'" for d in SAMPLE_DOCUMENTS)
        return (
            f"No direct matches found in research library for '{query}'. "
            f"Available research categories in library include: {available_titles}."
        )

    # Sort descending by relevance score
    matched_docs.sort(key=lambda item: item[0], reverse=True)

    results: List[str] = []
    for _, doc in matched_docs[:2]:  # Top 2 most relevant documents
        _last_consulted_sources.add(doc["title"])
        content_preview = doc["content"][:400] + ("..." if len(doc["content"]) > 400 else "")
        results.append(
            f"[{doc['title']}]\nCategory: {doc['category']}\nSummary: {doc['summary']}\nKey Findings & Metrics:\n{content_preview}\n"
        )

    return "\n".join(results)


# Alias for backward compatibility
search_research_library = search_library
