from src.agents.analytics.fundamentals_analyst.fundamentals_analyst import FundamentalsAnalyst
from src.agents.analytics.fundamentals_analyst.fundamentals_tools import tools
from agno.models.deepseek import DeepSeek

def fundamentals_deepseek_factory() -> FundamentalsAnalyst:
    fundamentals_analyst = FundamentalsAnalyst(
        model=DeepSeek(id="deepseek-chat"),
        tools=tools,
    )
    return fundamentals_analyst