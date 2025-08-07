from src.agents.research.bull_research.bull_research import BullResearch
from src.agents.research.bull_research.bull_research_tools import tools
from agno.models.deepseek import DeepSeek

def bull_deepseek_factory() -> BullResearch:
    bull_research = BullResearch(
        model=DeepSeek(id="deepseek-chat"),
        tools=tools,
    )
    return bull_research 