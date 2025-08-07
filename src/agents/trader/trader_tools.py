from agno.tools.yfinance import YFinanceTools

tools = [
    YFinanceTools(stock_price=True, 
    company_info=True, 
    stock_fundamentals=True, 
    income_statements=True, 
    key_financial_ratios=True, 
    analyst_recommendations=True, 
    company_news=True, 
    technical_indicators=True, 
    historical_prices=True, 
    enable_all=True),
] 