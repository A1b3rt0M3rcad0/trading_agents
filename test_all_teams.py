import asyncio
from src.teams import run_analytics_analysis, run_research_analysis, run_investment_decision

async def test_all_teams():
    company_symbol = "AAPL"
    
    print("=" * 60)
    print(f"TESTING ANALYTICS TEAM FOR {company_symbol}")
    print("=" * 60)
    await run_analytics_analysis(company_symbol)
    
    print("\n" + "=" * 60)
    print(f"TESTING RESEARCH TEAM FOR {company_symbol}")
    print("=" * 60)
    await run_research_analysis(company_symbol)
    
    print("\n" + "=" * 60)
    print(f"TESTING DECISION TEAM FOR {company_symbol}")
    print("=" * 60)
    await run_investment_decision(company_symbol)

if __name__ == "__main__":
    asyncio.run(test_all_teams()) 