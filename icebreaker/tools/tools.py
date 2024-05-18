from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(query: str):
    search = TavilySearchResults()
    results = search.run(f"{query}")
    return ", ".join([result["url"] for result in results])