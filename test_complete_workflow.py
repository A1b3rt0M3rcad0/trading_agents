import asyncio
from src.teams.analytics import run_analytics_analysis
from src.teams.research import run_research_analysis
from src.teams.decision_team import run_investment_decision

async def test_complete_workflow():
    company_symbol = "NVDA"
    
    print("=" * 60)
    print("STEP 1: ANALYTICS TEAM ANALYSIS")
    print("=" * 60)
    
    # Executar análise do time de analytics
    analytics_result = await run_analytics_analysis(company_symbol)
    
    print("\n" + "=" * 60)
    print("STEP 2: RESEARCH TEAM ANALYSIS")
    print("=" * 60)
    
    # Executar análise do time de research
    research_result = await run_research_analysis(company_symbol)
    
    print("\n" + "=" * 60)
    print("STEP 3: FINAL INVESTMENT DECISION")
    print("=" * 60)
    print("Using results from Analytics and Research teams to make final decision...")
    
    # Usar os resultados dos outros times para tomar a decisão final
    await run_investment_decision(
        company_symbol=company_symbol,
        analytics_report=str(analytics_result) if analytics_result else "Analytics analysis completed",
        research_report=str(research_result) if research_result else "Research analysis completed"
    )

if __name__ == "__main__":
    asyncio.run(test_complete_workflow()) 