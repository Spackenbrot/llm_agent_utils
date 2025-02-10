from duckduckgo_search import DDGS

def search(query: str, max_results = 5):
    """
    Searches the web for the query you give it.
    Returns a list of dicts, where each entry contains 'title', 'body' (preview of the site content)
    and 'href' (url, which you can then use to scrape the entire page)
    """
    return DDGS().text(keywords=query, max_results=max_results, safesearch='off')