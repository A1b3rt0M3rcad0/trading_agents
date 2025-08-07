from src.agents.analytics.market_analyst.market_analyst import MarketAnalyst
from src.agents.analytics.market_analyst.market_tools import tools
from agno.models.deepseek import DeepSeek

def market_deepseek_factory() -> MarketAnalyst:
    market_analyst = MarketAnalyst(
        model=DeepSeek(id="deepseek-chat"),
        tools=tools,
    )
    return market_analyst