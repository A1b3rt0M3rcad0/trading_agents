import asyncio
from src.teams.decision_team import run_investment_decision

async def test_decision_with_reports():
    company_symbol = "TSLA"
    
    # Relatório do time de analytics (exemplo)
    analytics_report = """
    ANALYTICS TEAM COMPREHENSIVE ANALYSIS:
    
    FUNDAMENTALS ANALYSIS:
    - Revenue growth: 15% YoY
    - Profit margins: Improving to 12%
    - Debt levels: Decreasing
    - Cash flow: Strong positive
    
    TECHNICAL ANALYSIS:
    - Current price: $180
    - Support levels: $170, $160
    - Resistance levels: $190, $200
    - Trend: Bullish with consolidation
    
    NEWS SENTIMENT:
    - Positive: New product announcements
    - Neutral: Regulatory updates
    - Negative: Supply chain concerns
    
    SOCIAL MEDIA SENTIMENT:
    - Overall: Bullish
    - Engagement: High
    - Influencer sentiment: Positive
    """
    
    # Relatório do time de research (exemplo)
    research_report = """
    RESEARCH TEAM COMPREHENSIVE ANALYSIS:
    
    BULLISH SCENARIOS:
    - Market expansion in Asia
    - New technology breakthroughs
    - Regulatory tailwinds
    - Target price: $220 (22% upside)
    
    BEARISH SCENARIOS:
    - Increased competition
    - Supply chain disruptions
    - Regulatory challenges
    - Risk price: $140 (22% downside)
    
    RISK-REWARD ASSESSMENT:
    - Risk level: Moderate
    - Reward potential: High
    - Time horizon: 6-12 months
    """
    
    print("=" * 60)
    print("INVESTMENT DECISION BASED ON TEAM REPORTS")
    print("=" * 60)
    
    await run_investment_decision(
        company_symbol=company_symbol,
        analytics_report=analytics_report,
        research_report=research_report
    )

if __name__ == "__main__":
    asyncio.run(test_decision_with_reports()) 