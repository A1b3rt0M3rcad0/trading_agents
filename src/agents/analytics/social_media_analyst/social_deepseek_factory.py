from src.agents.analytics.social_media_analyst.social_media_analyst import SocialMediaAnalyst
from src.agents.analytics.social_media_analyst.social_media_tools import tools
from agno.models.deepseek import DeepSeek

def social_deepseek_factory() -> SocialMediaAnalyst:
    social_media_analyst = SocialMediaAnalyst(
        model=DeepSeek(id="deepseek-chat"),
        tools=tools,
    )
    return social_media_analyst