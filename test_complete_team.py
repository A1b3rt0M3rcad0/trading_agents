import asyncio
from src.teams.complete_team import run_complete_analysis

async def test_complete_team():
    company_symbol = "NVDA"
    mode = "print"
    
    print("=" * 80)
    print("COMPLETE TEAM ANALYSIS")
    print("=" * 80)
    print(f"Analyzing {company_symbol} with all agents working together...")
    print("=" * 80)
    
    # Executar análise completa com todos os agentes
    result = await run_complete_analysis(company_symbol, mode)
    
    if mode != "print":
        print("\n" + "=" * 80)
        print("FINAL DECISION")
        print("=" * 80)
    else:
        print("\n" + "=" * 80)
        print("FINAL DECISION")
        print("=" * 80)
        print(result)
        print("=" * 80)

if __name__ == "__main__":
    asyncio.run(test_complete_team()) 