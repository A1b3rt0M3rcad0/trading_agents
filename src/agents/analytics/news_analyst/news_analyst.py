from src.agents.agent.agent_like import AgentLike
from agno.agent import Agent
from agno.models.openai.like import OpenAILike
from agno.tools import Toolkit

class NewsAnalyst(AgentLike):
    def __init__(self, model: OpenAILike, tools: list[Toolkit], markdown: bool = True) -> None:
        self.message = """
        You are a news researcher and macroeconomics specialist. Your primary task is to write a comprehensive report on the current state of the world, focusing on news and trends from the past week that are relevant for trading and macroeconomics.

        **Key Responsibilities:**
        - Analyze recent news and market trends from the past week.
        - Synthesize information from specific sources, including **EODHD** and **Finnhub**, to ensure a comprehensive view.

        **Analysis Requirements:**
        - The report must be detailed and insightful.
        - Do not simply state that "trends are mixed."
        - Provide a detailed and fine-grained analysis, offering specific insights that can help traders make informed decisions.

        **Report Formatting:**
        - Conclude your report by appending a well-organized **Markdown table** that summarizes the key points and findings.
        """
        self._agent = Agent(
            model=model,
            tools=tools,
            instructions=self.message,
            markdown=markdown,
        )

    def run(self, company_symbol: str, *args, **kwargs):
        self._agent.print_response(f"Analyze the news information for {company_symbol} over the past week.", stream=True)

    @property
    def agent(self) -> Agent:
        return self._agent