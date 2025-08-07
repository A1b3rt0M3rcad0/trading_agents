from agno.agent import Agent
from src.agents.agent.agent_like import AgentLike
from agno.models.openai.like import OpenAILike
from agno.tools import Toolkit

class Trader(AgentLike):
    def __init__(self, model: OpenAILike, tools: list[Toolkit], markdown: bool = True) -> None:
        self.message = self.message = """
        You are a highly skilled and decisive trading agent. Your role is to analyze a comprehensive investment plan and various market reports to make a definitive trading recommendation: **BUY**, **HOLD**, or **SELL**.

        **Your Analytical Framework:**

        1.  **Evaluate the Investment Plan:**
            -   Assess the core proposal provided by the analyst team.
            -   Identify the key drivers and underlying rationale.

        2.  **Integrate External Data:**
            -   Synthesize insights from provided reports on **market trends**, **macroeconomic indicators**, **social media sentiment**, and **fundamental analysis**.
            -   Cross-reference all data points to identify correlations or contradictions.

        3.  **Learn from Past Experience:**
            -   Carefully review and apply lessons from your past trading decisions in similar situations.
            -   Use this historical knowledge to avoid repeating mistakes and to refine your current strategy.

        **Final Decision & Output:**

        - Your response must present a clear, detailed, and reasoned analysis supporting your final recommendation.
        - Be firm and unambiguous in your decision.
        - If your recommendation is **BUY** or **SELL**, you must provide a complete OCO (One Cancels the Other) order setup:
            - For **BUY**:
                - Entry price (recommended buy point)
                - Take-profit target (price to sell for profit)
                - Stop-loss level (price to limit loss)
            - For **SELL**:
                - Entry price (recommended sell point or short entry)
                - Take-profit target (price to buy back and close the short)
                - Stop-loss level (price to cut losses)
        - If your recommendation is **HOLD**, no price levels are needed — simply explain why holding is the best course of action at the moment.
        - Your response must **always** conclude with the exact phrase:
        """
        self._agent = Agent(
            model=model,
            tools=tools,
            instructions=self.message,
            markdown=markdown,
        )

    def run(self, company_symbol: str, *args, investment_plan: str = None, market_report: str = None, 
            sentiment_report: str = None, news_report: str = None, fundamentals_report: str = None, 
            past_memories: str = None, **kwargs):
        
        # Build context from available reports
        context_parts = []
        if market_report:
            context_parts.append(f"Market Analysis: {market_report}")
        if sentiment_report:
            context_parts.append(f"Sentiment Analysis: {sentiment_report}")
        if news_report:
            context_parts.append(f"News Analysis: {news_report}")
        if fundamentals_report:
            context_parts.append(f"Fundamentals Analysis: {fundamentals_report}")
        
        context = "\n\n".join(context_parts) if context_parts else "No additional context provided."
        
        # Build the analysis request
        analysis_request = f"Analyze the investment opportunity for {company_symbol}."
        
        if investment_plan:
            analysis_request += f"\n\nProposed Investment Plan: {investment_plan}"
        
        if context:
            analysis_request += f"\n\nAdditional Context:\n{context}"
        
        if past_memories:
            analysis_request += f"\n\nPast Trading Lessons:\n{past_memories}"
        
        self._agent.print_response(analysis_request, stream=True)

    @property
    def agent(self) -> Agent:
        return self._agent 