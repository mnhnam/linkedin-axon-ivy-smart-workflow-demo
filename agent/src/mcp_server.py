from mcp.server.fastmcp import FastMCP
from src.itviec_agent import ITViecAgent
from src.vietnamworks_agent import VietnamWorksAgent


mcp = FastMCP("job_postings_agent")

@mcp.tool()
async def get_itviec_job_postings(number_of_jobs: int = 1, search_term: str = "") -> str:
    """
    Tool to get job postings from https://itviec.com/

    Args:
        number_of_jobs (int): The number of job postings to retrieve.
        search_term (str): The search term to filter job listings.

    Returns:
        str: A string containing the job postings.
    """
    agent = ITViecAgent(
            website="https://itviec.com/",
            search_term=search_term,
            number_of_jobs=number_of_jobs
            )

    return await agent.get_job_postings()

@mcp.tool()
async def get_vietnamworks_job_postings(number_of_jobs: int = 1, search_term: str = "") -> str:
    """
    Tool to get job postings from https://www.vietnamworks.com/

    Args:
        number_of_jobs (int): The number of job postings to retrieve.
        search_term (str): The search term to filter job listings.

    Returns:
        str: A string containing the job postings.
    """
    agent = VietnamWorksAgent(
        website="https://www.vietnamworks.com/",
        search_term=search_term,
        number_of_jobs=number_of_jobs
    )

    return await agent.get_job_postings()

def main():
    """Entry point for the direct execution server."""
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()