import asyncio
from textwrap import dedent
from agno.team.team import Team
from agno.models.deepseek import DeepSeek
from src.agents.analytics.fundamentals_analyst.fundamental_deepseek_factory import fundamentals_deepseek_factory
from src.agents.analytics.market_analyst.market_deepseek_factory import market_deepseek_factory
from src.agents.analytics.news_analyst.news_deepseek_factory import news_deepseek_factory
from src.agents.analytics.social_media_analyst.social_deepseek_factory import social_deepseek_factory
from src.agents.research.bear_research.bear_deepseek_factory import bear_deepseek_factory
from src.agents.research.bull_research.bull_deepseek_factory import bull_deepseek_factory
from src.agents.trader.trader_deepseek_factory import trader_deepseek_factory

# Criar instâncias dos agentes
fundamentals_analyst = fundamentals_deepseek_factory().agent
fundamentals_analyst.name = "Fundamentals Analyst"
fundamentals_analyst.role = "Analyze company fundamentals and financial metrics"

market_analyst = market_deepseek_factory().agent
market_analyst.name = "Market Analyst"
market_analyst.role = "Analyze technical indicators and market trends"

news_analyst = news_deepseek_factory().agent
news_analyst.name = "News Analyst"
news_analyst.role = "Analyze news sentiment and market-moving events"

social_media_analyst = social_deepseek_factory().agent
social_media_analyst.name = "Social Media Analyst"
social_media_analyst.role = "Analyze social media sentiment and public opinion"

bear_researcher = bear_deepseek_factory().agent
bear_researcher.name = "Bear Market Researcher"
bear_researcher.role = "Identify bearish scenarios and short-selling opportunities"

bull_researcher = bull_deepseek_factory().agent
bull_researcher.name = "Bull Market Researcher"
bull_researcher.role = "Identify bullish scenarios and long-term investment opportunities"

trader = trader_deepseek_factory().agent
trader.name = "Senior Trader"
trader.role = "Make final trading decisions based on all analysis and research"

# Criar o time de trading
trading_team = Team(
    name="Trading Team",
    mode="collaborate",
    model=DeepSeek(id="deepseek-chat"),
    members=[
        fundamentals_analyst,
        market_analyst,
        news_analyst,
        social_media_analyst,
        bear_researcher,
        bull_researcher,
        trader,
    ],
    instructions=[
        "You are the Trading Team Coordinator.",
        "Coordinate comprehensive analysis from all team members.",
        "Ensure each analyst and researcher provides their specialized insights.",
        "The Senior Trader will make the final trading decision.",
        "Provide clear BUY, HOLD, or SELL recommendation with specific price targets.",
        "Include risk management and position sizing recommendations.",
        "Stop the discussion when a final trading decision has been reached.",
    ],
    success_criteria="Complete trading analysis with final BUY/HOLD/SELL recommendation and specific price targets.",
    enable_agentic_context=True,
    show_tool_calls=True,
    markdown=True,
    show_members_responses=True,
)

async def run_trading_analysis(company_symbol: str):
    """Executa análise completa de trading para um símbolo de empresa"""
    await trading_team.aprint_response(
        message=f"Conduct comprehensive trading analysis for {company_symbol} and provide final BUY/HOLD/SELL recommendation with specific price targets and risk management.",
        stream=True,
        stream_intermediate_steps=True,
    )

if __name__ == "__main__":
    asyncio.run(run_trading_analysis("AAPL")) 