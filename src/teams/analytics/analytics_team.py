import asyncio
from textwrap import dedent
from agno.team.team import Team
from agno.models.deepseek import DeepSeek
from src.agents.analytics.fundamentals_analyst.fundamental_deepseek_factory import fundamentals_deepseek_factory
from src.agents.analytics.market_analyst.market_deepseek_factory import market_deepseek_factory
from src.agents.analytics.news_analyst.news_deepseek_factory import news_deepseek_factory
from src.agents.analytics.social_media_analyst.social_deepseek_factory import social_deepseek_factory

# Criar instâncias dos agentes de analytics
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

# Criar o time de analytics
analytics_team = Team(
    name="Analytics Team",
    mode="collaborate",
    model=DeepSeek(id="deepseek-chat"),
    members=[
        fundamentals_analyst,
        market_analyst,
        news_analyst,
        social_media_analyst,
    ],
    instructions=[
        "You are the Analytics Team Coordinator.",
        "Coordinate comprehensive analysis across fundamental, technical, news, and social media dimensions.",
        "Ensure each analyst provides their specialized insights.",
        "Synthesize findings into a comprehensive market analysis report.",
        "Stop the discussion when all dimensions have been thoroughly analyzed.",
    ],
    success_criteria="Complete comprehensive analysis covering all analytical dimensions with actionable insights.",
    enable_agentic_context=True,
    show_tool_calls=True,
    markdown=True,
    show_members_responses=True,
)

async def run_analytics_analysis(company_symbol: str):
    """Executa análise completa de analytics para um símbolo de empresa e retorna o resultado"""
    response = await analytics_team.aprint_response(
        message=f"Conduct comprehensive analytics analysis for {company_symbol} covering fundamentals, market trends, news sentiment, and social media sentiment.",
        stream=True,
        stream_intermediate_steps=True,
    )
    return response

if __name__ == "__main__":
    asyncio.run(run_analytics_analysis("AAPL")) 