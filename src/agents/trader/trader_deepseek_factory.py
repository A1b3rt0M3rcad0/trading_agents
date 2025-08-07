from src.agents.trader.trader import Trader
from src.agents.trader.trader_tools import tools
from agno.models.deepseek import DeepSeek

def trader_deepseek_factory() -> Trader:
    trader = Trader(
        model=DeepSeek(id="deepseek-chat"),
        tools=tools,
    )
    return trader 