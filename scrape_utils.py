import asyncio

from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

async def crawl_site(url: str):
    """
    Crawles a given url to fetch the sites contents and returns them as
    neatly formatted markdown string. (Which can then be inserted in
    the knowledge base for easier access)
    """
    prune_filter = PruningContentFilter(
        threshold=0.5,
        threshold_type="fixed",  # or "dynamic"
        min_word_threshold=50
    )
    md_generator = DefaultMarkdownGenerator(
        content_filter=prune_filter,
        options={
            "ignore_links": True,
            "escape_html": False,
            "body_width": 80
        },
    )
    browser_config = BrowserConfig()  # Default browser configuration
    run_config = CrawlerRunConfig(
        markdown_generator=md_generator
    )   # Default crawl run configuration
    async with AsyncWebCrawler(config=browser_config) as crawler:
        res = await crawler.arun(
            url=url,
            config=run_config
        )
        if res.success:
            return res.markdown
        else:
            return res.error_message