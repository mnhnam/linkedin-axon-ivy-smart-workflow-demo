import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from browser_use import Browser

# Load environment variables from .env file
load_dotenv()

class AbstractAgent(ABC):
    """
    Abstract base class for agents.
    """

    search_term: str = ""
    website: str = ""
    number_of_jobs: int = 1

    def __init__(self, website: str, search_term: str, number_of_jobs: int):
        self.browser = None
        self.model_name = os.getenv("DEFAULT_MODEL", "gpt-4.1-mini")
        self.website = website
        self.search_term = search_term
        self.number_of_jobs = number_of_jobs

    async def get_browser(self) -> Browser:
        """Initialize and return a browser instance."""
        browser = Browser(
            keep_alive=True,
            headless=False,  # Use headless mode for better server compatibility
            disable_security=True  # Disable security features that might cause issues
        )
        return browser

    @abstractmethod
    async def get_job_postings(self) -> str:
        pass