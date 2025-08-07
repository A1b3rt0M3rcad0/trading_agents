import asyncio
from src.teams.analytics import run_analytics_analysis

async def test_analytics_team():
    await run_analytics_analysis("AAPL")

if __name__ == "__main__":
    asyncio.run(test_analytics_team()) 