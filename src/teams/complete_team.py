import asyncio
from textwrap import dedent
from agno.team.team import Team
from agno.models.deepseek import DeepSeek
from typing import Literal, Optional

# Importar todos os agentes de analytics
from src.agents.analytics.fundamentals_analyst.fundamental_deepseek_factory import fundamentals_deepseek_factory
from src.agents.analytics.market_analyst.market_deepseek_factory import market_deepseek_factory
from src.agents.analytics.news_analyst.news_deepseek_factory import news_deepseek_factory
from src.agents.analytics.social_media_analyst.social_deepseek_factory import social_deepseek_factory

# Importar todos os agentes de research
from src.agents.research.bear_research.bear_deepseek_factory import bear_deepseek_factory
from src.agents.research.bull_research.bull_deepseek_factory import bull_deepseek_factory

# Importar o agente trader
from src.agents.trader.trader_deepseek_factory import trader_deepseek_factory

# Criar instâncias de todos os agentes
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

senior_trader = trader_deepseek_factory().agent
senior_trader.name = "Senior Investment Decision Maker"
senior_trader.role = "Make final investment decisions based on comprehensive analysis from all teams"

# Criar o time completo
complete_team = Team(
    name="Complete Investment Team",
    mode="collaborate",
    model=DeepSeek(id="deepseek-chat"),
    members=[
        fundamentals_analyst,
        market_analyst,
        news_analyst,
        social_media_analyst,
        bear_researcher,
        bull_researcher,
        senior_trader,
    ],
    instructions=[
        "You are the Complete Investment Team Coordinator.",
        "Coordinate comprehensive analysis across all dimensions: fundamentals, technical, news, social media, bullish scenarios, and bearish scenarios.",
        "Each analyst should provide their specialized insights.",
        "The Senior Investment Decision Maker will synthesize all findings and make the final decision.",
        "Ensure balanced analysis from all perspectives.",
        "Provide clear BUY, HOLD, or SELL recommendation with specific price targets.",
        "Include detailed risk management, position sizing, and timeline recommendations.",
        "Provide confidence level and reasoning for the final decision.",
        "Stop the discussion when all dimensions have been thoroughly analyzed and a final decision is reached.",
    ],
    success_criteria="Complete investment decision with final BUY/HOLD/SELL recommendation, specific price targets with OCO setup, risk management, and confidence level based on comprehensive team analysis.",
    enable_agentic_context=True,
    show_tool_calls=True,
    markdown=True,
    show_members_responses=True,
)

async def run_complete_analysis(company_symbol: str, mode:Literal["run", "print"] = "print") -> Optional[str]:
    """Executa análise completa e toma decisão de investimento para um símbolo de empresa"""
    if mode == "run":
        response = await complete_team.arun(
            message=f"Conduct comprehensive investment analysis for {company_symbol}. Each analyst should provide their specialized insights, and the Senior Investment Decision Maker should synthesize all findings to make the final BUY/HOLD/SELL recommendation with specific price targets, risk management, and confidence level.",
        )
        return response
    elif mode == "print":
        await complete_team.aprint_response(
            message=f"Conduct comprehensive investment analysis for {company_symbol}. Each analyst should provide their specialized insights, and the Senior Investment Decision Maker should synthesize all findings to make the final BUY/HOLD/SELL recommendation with specific price targets, risk management, and confidence level.",
        )
    else:
        raise ValueError(f"Invalid mode: {mode}")

if __name__ == "__main__":
    asyncio.run(run_complete_analysis("AAPL"))
