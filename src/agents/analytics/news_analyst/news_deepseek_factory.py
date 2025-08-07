from src.agents.analytics.news_analyst.news_analyst import NewsAnalyst
from src.agents.analytics.news_analyst.news_tools import tools
from agno.models.deepseek import DeepSeek

def news_deepseek_factory() -> NewsAnalyst:
    news_analyst = NewsAnalyst(
        model=DeepSeek(id="deepseek-chat"),
        tools=tools,
    )
    return news_analyst