from typing import Optional
from .abstract_agent import AbstractAgent
from .itviec_agent import ITViecAgent
from .vietnamworks_agent import VietnamWorksAgent

def create_agent(website: str, search_term: str, number_of_jobs: int) -> Optional[AbstractAgent]:
    """
    Create and return the appropriate agent based on the website URL.
    """
    website_url_lower = website.lower()
    
    if "itviec.com" in website_url_lower:
        return ITViecAgent(
            website=website,
            search_term=search_term,
            number_of_jobs=number_of_jobs
            )
    elif "vietnamworks.com" in website_url_lower:
        return VietnamWorksAgent(
            website=website,
            search_term=search_term,
            number_of_jobs=number_of_jobs
        )
    else:
        return None

def get_supported_websites():
    """
    Get a list of all supported website URLs.
    
    Returns:
        list: List of supported website URL patterns
    """
    return ["itviec.com", "vietnamworks.com"]