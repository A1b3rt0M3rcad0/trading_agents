from src.agents.research.bear_research.bear_research import BearResearch
from src.agents.research.bear_research.bear_research_tools import tools
from agno.models.deepseek import DeepSeek

def bear_deepseek_factory() -> BearResearch:
    bear_research = BearResearch(
        model=DeepSeek(id="deepseek-chat"),
        tools=tools,
    )
    return bear_research 