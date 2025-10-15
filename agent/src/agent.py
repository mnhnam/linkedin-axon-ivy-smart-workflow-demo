import os
from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatOpenAI

JOB_FINDING_TASK_TEMPLATE = """
    1. Open the {website} homepage.
    2. Locate the search bar and enter the keyword '{search_term}'.
    3. While focusing the search input, press Enter to initiate the search.
    4. Wait until the search results page fully loads.
    5. Get details of the top {number_of_jobs} job listings one by one.
    6. Put all job listings into a single string and return it.
"""

# Load environment variables from .env file
load_dotenv()

async def get_browser() -> Browser:
    browser = Browser(
        keep_alive=True,
        headless=False,  # Use headless mode for better server compatibility
        disable_security=True  # Disable security features that might cause issues
    )
    return browser

async def get_job_postings(
        website: str,
        number_of_jobs: int = 1,
        search_term: str = ""
        ) -> str:

    # Initialize the browser
    browser = await get_browser()

    # Start the browser session
    await browser.start()

    # Get model from environment variable or use default
    model_name = os.getenv("DEFAULT_MODEL", "gpt-4.1-mini")
    
    # Create the agent with the job finding task
    agent = Agent(
        task=JOB_FINDING_TASK_TEMPLATE.format(
            website=website,
            number_of_jobs=number_of_jobs,
            search_term=search_term
        ),
        llm=ChatOpenAI(model=model_name, temperature=0),
        browser_session=browser,
        verbose=True  # log detailed info for debugging
    )

    # Execute the agent's task
    await agent.run()
    
    # Clean up and close the browser session
    await browser.kill()

    # Return the final result from the agent's history
    return agent.history.final_result().strip() or "No job listings found."