# [Disclaimer](https://github.com/hakancangunerli/discussions-disclaimers/blob/master/disclaimer.md)

# FRC Analysis

This piece of code is used to analyze the $FRC (First Republic Bank) analysis. As of today (5/1/2023 2AM EST), it's predicted that that either FDIC or another bank will acquire $FRC. To further understand the breakdown of how FRC has been performing, I've decided to analyze the data and see if the company financials and stock performance.

# Key takeaways

The company's cumulative return over the period was -86.28%, indicating that investors who held onto the company's stock during this time would have lost a significant amount of money. The CAGR (Compound Annual Growth Rate) was -14.81%, which is the average annual rate of return over the period. This is a negative rate, indicating that the company's stock lost value over the period. The Sharpe ratio is negative, indicating that the company's returns did not compensate for the level of risk taken. The Smart Sharpe and Sortino ratios are also negative, indicating poor risk-adjusted performance. The company had a high maximum drawdown of 98.4%, meaning that at its worst point during the period, the stock had lost almost all of its value.

The report also includes various financial metrics for the company, such as total assets, total debt, and share issued.Based on the provided financial metrics for the years 2019-2022, the company has a total asset value of 96.38 billion USD. The total liabilities net minority interest is 87.88 billion USD, while the total equity gross minority interest is 7.59 billion USD. The company's total capitalization is 2.70 billion USD, of which 2.49 billion USD is preferred stock equity and 5.11 billion USD is common stock equity. The company has a net tangible asset value of 7.64 billion USD, invested capital of 6.56 billion USD, and tangible book value of 5.15 billion USD. The company has a total debt of 641.86 million USD, and net debt information is not available. The company has issued 14.63 million shares of both ordinary and preferred shares.

Overall, the financial metrics indicate that the company has a significant amount of assets and a considerable amount of debt, this report paints a negative picture of the company's performance over the period, with poor returns, high risk, and extreme losses.

# Packages used

quanstats, pandas, numpy, matplotlib, yfinance, requests, datetime, BeautifulSoup

# References

<https://stackoverflow.com/questions/70090315/balance-sheet-from-using-yfinance-does-not-have-total-debt-like-on-yahoo-finan>