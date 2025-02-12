import asyncio

from langchain_core.tools import tool
from rag_utils import RAGManager
from search_utils import search
from scrape_utils import crawl_site

rag = RAGManager()

@tool(response_format="content_and_artifact")
def retrieve(query: str):
    """
    Retrieve information related to a query.
    Returns content as well as the source url if available.
    """
    retrieved_docs = rag.retrieve_from_query(query)
    serialized = "\n\n".join(
        f"Source: {doc.metadata}\n" f"Content: {doc.page_content}"
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

@tool
def search_the_web(query: str, max_results = 5):
    """
    Searches the web using your given query.
    Returns a list of urls and content previews.
    Use that with the scrape tool to get the full
    page content of the url where the preview matches
    your query the most.
    """
    return search(query, max_results)

@tool
async def scrape_website(url: str):
    """
    Visits a given url and returns the websites
    contents as neatly formatted markdown_v2 string.
    """
    mv2 = await crawl_site(url)
    rag.store_markdown(mv2, url)
    return mv2