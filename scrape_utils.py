from crawl4ai import WebCrawler
from crawl4ai.models import MarkdownGenerationResult

def crawl_site(url: str) -> MarkdownGenerationResult | None:
    """
    Crawles a given url to fetch the sites contents and returns them as
    neatly formatted markdown string. (Which can then be inserted in
    the knowledge base for easier access)
    """
    res = WebCrawler().run(url)
    return res.markdown_v2
