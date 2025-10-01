import asyncio
import re

import aiohttp
from bs4 import BeautifulSoup
from loguru import logger

def extract_urls(text: str) -> list[str]:
    """Extract URLs from a given text using regex."""
    url_pattern = r"(?P<url>https?:\/\/[^\s]+)" # 1
    urls = re.findall(url_pattern, text) # url_pattern is the regex pattern to find URLs, text is the input text
    return urls

def parse_inner_html(html_string: str) -> list[str]:
    """Parse the inner HTML content from a given HTML string."""
    soup = BeautifulSoup(html_string, "lxml") # Parse the HTML string using BeautifulSoup with the 'lxml' parser
    if content := soup.find_all("div", id="bodyContent"):
        return content.get_text() # Extract and return the text content from the found div
    logger.warning("Could not parse the HTML content.")
    return "" # Return an empty string if the desired content is not found

async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    """Fetch the HTML content from a given URL asynchronously."""
    async with session.get(url) as response: # Make an asynchronous GET request to the URL
        html_string = await response.text() # Await the response text
        return parse_inner_html(html_string) # Parse and return the inner HTML content
    
async def fetch_all(urls: list[str]) -> str:
    """Fetch HTML content from multiple URLs concurrently."""
    async with aiohttp.ClientSession() as session: # Create an asynchronous HTTP session
        results = await asyncio.gather(
            *[fetch(session, url) for url in urls], return_exceptions=True # Fetch all URLs concurrently and gather results
        )
        success_results = [result for result in results if not isinstance(result, str)]
        if len(results) != len(success_results):
            logger.warning("Some URLs could not be fetched.")
        return " ".join(success_results) # Join and return all successfully fetched contents