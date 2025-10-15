from .abstract_agent import AbstractAgent
from browser_use import Agent, ChatOpenAI

class ITViecAgent(AbstractAgent):
    """
    Job gathering agent specifically designed for ITViec (https://itviec.com/).
    """

    SIMPLE_TASK_TEMPLATE = """
        You are a job search assistant. Your task is to find job postings on the specified website.
        ---
        Instructions:
        1. Navigate to the homepage of the website: {website}.
        2. Locate the search bar and enter the keyword '{search_term}'.
        3. Press Enter to initiate the search.
        4. Wait until the search results page fully loads.
        5. Extract details of the top {number_of_jobs} job listings one by one.
        6. Compile all job listings into a single string and return it.
    """
    async def get_job_postings(self) -> str:
        """
        Main method to extract job postings from the specified website.
        """

        # Initialize the browser
        self.browser = await self.get_browser()
        
        # Start the browser session
        await self.browser.start()
        
        try:

            # Initialize search task
            task_1 = self.SIMPLE_TASK_TEMPLATE.format(
                    website=self.website,
                    number_of_jobs=self.number_of_jobs,
                    search_term=self.search_term
                )

            # Create the agent with the job finding task
            agent = Agent(
                task=task_1,
                llm=ChatOpenAI(model=self.model_name, temperature=0),
                browser_session=self.browser,
                verbose=True  # log detailed info for debugging
            )

            # You can define more tasks if needed, for example, a follow-up task to refine results

            # Execute the agent
            await agent.run()
            
            # Return the final result from the agent's history
            return agent.history.final_result().strip() or "No job listings found."
            
        finally:
            # Clean up and close the browser session
            if self.browser:
                await self.browser.kill()