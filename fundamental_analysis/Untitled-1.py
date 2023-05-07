# %%
# TD AmeriTrade & Fidelity Investing Basics Fundamental Analysis

import fundamentalanalysis as fa

# %%
ticker = 'SCHW'

# get text from the API_KEY.txt file
api_key = open('API_KEY.txt', 'r').read() # read the API_KEY.txt file, and store it as a string


profile = fa.profile(ticker, api_key)

profile


# %%
# Balance sheet 
balance_sheet = fa.balance_sheet_statement(ticker, api_key, period="annual")


balance_sheet



# %%
#Income statement


income_statement = fa.income_statement(ticker, api_key, period="annual")

income_statement





# %%
# get the P/E ratio

# Price/Book value 

# Debt / Equity 


# Return on equity 


# Current ratio 

# net profit margin 

# %%
# Cash flow statement
cash_flow = fa.cash_flow_statement(ticker, api_key, period="annual")

cash_flow

# %%
# get financial_ratios and key_metrics 


financial_ratios = fa.financial_ratios(ticker, api_key, period="annual")

financial_ratios

# %%
key_metrics = fa.key_metrics(ticker, api_key, period="annual")

key_metrics

# %%
# save all of these particular dataframes to a csv file, this way the API doesn't have to be called again for the same data

# save the dataframes to a csv file

balance_sheet.to_csv('balance_sheet.csv')

income_statement.to_csv('income_statement.csv')

cash_flow.to_csv('cash_flow.csv')

financial_ratios.to_csv('financial_ratios.csv')

key_metrics.to_csv('key_metrics.csv')



