import asyncio
from textwrap import dedent
from agno.team.team import Team
from agno.models.deepseek import DeepSeek
from src.agents.trader.trader_deepseek_factory import trader_deepseek_factory

# Criar instância do trader que tomará a decisão final
senior_trader = trader_deepseek_factory().agent
senior_trader.name = "Senior Investment Decision Maker"
senior_trader.role = "Make final investment decisions based on comprehensive analysis from analytics and research teams"

# Criar o time de decisão final
decision_team = Team(
    name="Investment Decision Team",
    mode="collaborate",
    model=DeepSeek(id="deepseek-chat"),
    members=[
        senior_trader,
    ],
    instructions=[
        "You are the Senior Investment Decision Maker.",
        "You will receive comprehensive analysis from the Analytics Team and Research Team.",
        "Your role is to synthesize all the information and make the final investment decision.",
        "Consider all perspectives: fundamental analysis, technical analysis, news sentiment, social media sentiment, bullish scenarios, and bearish scenarios.",
        "Provide clear BUY, HOLD, or SELL recommendation with specific price targets.",
        "Include detailed risk management, position sizing, and timeline recommendations.",
        "Provide confidence level and reasoning for the final decision.",
        "Base your decision on the comprehensive analysis provided by the other teams.",
    ],
    success_criteria="Complete investment decision with final BUY/HOLD/SELL recommendation, specific price targets, risk management, and confidence level based on comprehensive team analysis.",
    enable_agentic_context=True,
    show_tool_calls=True,
    markdown=True,
    show_members_responses=True,
)

async def run_investment_decision(company_symbol: str, analytics_report: str = None, research_report: str = None):
    """Executa decisão de investimento baseada nos relatórios dos outros times"""
    
    # Construir o contexto com os relatórios dos outros times
    context_parts = []
    
    if analytics_report:
        context_parts.append(f"ANALYTICS TEAM REPORT:\n{analytics_report}")
    
    if research_report:
        context_parts.append(f"RESEARCH TEAM REPORT:\n{research_report}")
    
    if not context_parts:
        context_parts.append("No team reports provided. Conducting independent analysis.")
    
    context = "\n\n" + "\n\n".join(context_parts)
    
    await decision_team.aprint_response(
        message=f"Based on the comprehensive analysis provided by the Analytics and Research teams, make the final investment decision for {company_symbol}.{context}",
        stream=True,
        stream_intermediate_steps=True,
    )

if __name__ == "__main__":
    # Exemplo de uso com relatórios dos outros times
    analytics_report = """
    ANALYTICS TEAM FINDINGS:
    - Fundamentals: Strong financial metrics, growing revenue
    - Technical: Bullish trend with support at $150
    - News: Positive sentiment, new product launch
    - Social Media: High engagement, positive sentiment
    """
    
    research_report = """
    RESEARCH TEAM FINDINGS:
    - Bullish Scenario: Strong growth potential, market expansion
    - Bearish Scenario: Competition risks, regulatory concerns
    - Risk Assessment: Moderate risk with high reward potential
    """
    
    asyncio.run(run_investment_decision("AAPL", analytics_report, research_report)) 