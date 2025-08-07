import asyncio
from textwrap import dedent
from agno.team.team import Team
from agno.models.deepseek import DeepSeek
from src.agents.research.bear_research.bear_deepseek_factory import bear_deepseek_factory
from src.agents.research.bull_research.bull_deepseek_factory import bull_deepseek_factory

# Criar instâncias dos agentes de research
bear_researcher = bear_deepseek_factory().agent
bear_researcher.name = "Bear Market Researcher"
bear_researcher.role = "Identify bearish scenarios and short-selling opportunities"

bull_researcher = bull_deepseek_factory().agent
bull_researcher.name = "Bull Market Researcher"
bull_researcher.role = "Identify bullish scenarios and long-term investment opportunities"

# Criar o time de research
research_team = Team(
    name="Research Team",
    mode="collaborate",
    model=DeepSeek(id="deepseek-chat"),
    members=[
        bear_researcher,
        bull_researcher,
    ],
    instructions=[
        "You are the Research Team Coordinator.",
        "Coordinate comprehensive research covering both bullish and bearish perspectives.",
        "Ensure balanced analysis from both bull and bear researchers.",
        "Synthesize findings into a comprehensive investment thesis.",
        "Provide clear risk-reward analysis from both perspectives.",
        "Stop the discussion when both perspectives have been thoroughly analyzed.",
    ],
    success_criteria="Complete balanced research covering both bullish and bearish scenarios with clear investment thesis.",
    enable_agentic_context=True,
    show_tool_calls=True,
    markdown=True,
    show_members_responses=True,
)

async def run_research_analysis(company_symbol: str):
    """Executa análise completa de research para um símbolo de empresa e retorna o resultado"""
    response = await research_team.aprint_response(
        message=f"Conduct comprehensive research analysis for {company_symbol} covering both bullish and bearish scenarios to identify investment opportunities and risks.",
        stream=True,
        stream_intermediate_steps=True,
    )
    return response

if __name__ == "__main__":
    asyncio.run(run_research_analysis("TSLA")) 