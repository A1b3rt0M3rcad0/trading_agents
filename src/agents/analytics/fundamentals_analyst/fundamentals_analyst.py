from agno.agent import Agent
from src.agents.agent.agent_like import AgentLike
from agno.models.openai.like import OpenAILike
from agno.tools import Toolkit

class FundamentalsAnalyst(AgentLike):
    def __init__(self, model: OpenAILike, tools: list[Toolkit], markdown: bool = True) -> None:
        self.message = """
        You are a financial researcher specializing in fundamental analysis. Your task is to generate a comprehensive report on a given company's fundamental information over the past week to assist traders.

        The report must cover the following areas in detail:
        - **Company Profile:** Key information about the company.
        - **Financial Documents:** Recent and relevant filings.
        - **Basic Financials:** Current financial metrics and health.
        - **Financial History:** Past performance and trends.
        - **Insider Sentiment:** Analysis of insider buying/selling activity.
        - **Insider Transactions:** Detailed review of recent insider trades.

        Your analysis must be detailed and specific. Avoid vague statements like "trends are mixed." Instead, provide fine-grained insights that can directly inform trading decisions.

        The report should conclude with a clearly organized Markdown table summarizing the key findings.
        """
        self._agent = Agent(
            model=model,
            tools=tools,
            instructions=self.message,
            markdown=markdown,
        )

    def run(self, company_symbol: str, *args, **kwargs):
        self._agent.print_response(f"Analyze the fundamental information for {company_symbol} over the past week.", stream=True)

    @property
    def agent(self) -> Agent:
        return self._agent