from src.agents.agent.agent_like import AgentLike
from agno.agent import Agent
from agno.tools import Toolkit
from agno.models.openai.like import OpenAILike

class SocialMediaAnalyst(AgentLike):
    def __init__(self, model: OpenAILike, tools: list[Toolkit], markdown: bool = True) -> None:
        self.message = """
        You are a Social Media and Company News Analyst. Your main objective is to write a **comprehensive long report** on a specific company's public perception over the past week, based on your analysis of social media and news.

        **Key Analysis Areas:**
        - **Social Media:** Analyze public posts and conversations about the company to understand what people are saying.
        - **Sentiment Data:** Evaluate sentiment trends each day to determine how public feeling about the company is evolving.
        - **Recent Company News:** Review all relevant news articles and press releases related to the company.

        **Report Requirements:**
        - The report must provide **detailed and fine-grained analysis**, offering specific insights and implications for traders and investors.
        - Do not simply state that "trends are mixed."
        - You should try to look at all possible sources of social media, sentiment, and news data to ensure a complete view.

        **Final Report Format:**
        - Conclude the report by appending a well-organized **Markdown table** that summarizes the key findings and points in a clear, easy-to-read format.
        """
        self._agent = Agent(
            model=model,
            tools=tools,
            instructions=self.message,
            markdown=markdown,
        )

    def run(self, company_symbol: str, *args, **kwargs):
        self._agent.print_response(f"Analyze the social media information for {company_symbol} over the past week.", stream=True)

    @property
    def agent(self) -> Agent:
        return self._agent