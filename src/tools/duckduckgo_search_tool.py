from duckduckgo_search import DDGS
from crewai.tools import tool

@tool("DuckDuckGo Search")
def duckduckgo_search(query: str) -> str:
    """Use DuckDuckGo to perform a simple web search and return top results."""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        output = []
        for r in results:
            output.append(f"- {r['title']}: {r['href']}\n  {r['body']}")
        return "\n\n".join(output)
