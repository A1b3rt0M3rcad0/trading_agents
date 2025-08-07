import asyncio
from src.teams.research import run_research_analysis

async def test_research_team():
    await run_research_analysis("TSLA")

if __name__ == "__main__":
    asyncio.run(test_research_team()) 