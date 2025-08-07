import asyncio
from src.teams.decision_team import run_investment_decision

async def test_decision_team():
    await run_investment_decision("NVDA")

if __name__ == "__main__":
    asyncio.run(test_decision_team()) 