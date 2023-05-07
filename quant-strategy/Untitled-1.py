# %%
# import all of the csvs into separate dataframes

import pandas as pd

# import https://github.com/johngunerli/Hedge-Fund-Reports/blob/e6a0035bcea33ae517d520f2886fbc31229b81b9/master_list.csv csv 

hedgefunds = pd.read_csv('https://raw.githubusercontent.com/johngunerli/Hedge-Fund-Reports/master/master_list.csv?token=GHSAT0AAAAAAB6JE3RQLBTECSSC236P2ZO6ZBXANHQ', index_col=0)

hedgefunds

# %%
# get the cusip of the GlobalTitans

globaltitans = pd.read_csv('./OtherIndexes/GlobalTitans.csv')


# use Fidelity500 to get the cusip of the stocks for globaltitans

fidelity500 = pd.read_csv('./500s/topHoldingsFidelity500.csv')

# drop the emptys 
fidelity500 = fidelity500.dropna()



# set the columns as security_name, market_value, ticker, and cusip


fidelity500.columns = ['security_name', 'market_value', 'ticker', 'cusip']

fidelity500 = fidelity500[['ticker', 'cusip']]

fidelity500

# %%
# remove header, country, corporation, industry

globaltitans = globaltitans.drop(['Header','Country', 'Corporation', 'Industry'], axis=1)


# get the right side of the semicolon in Ticker

globaltitans['Ticker'] = globaltitans['Ticker'].str.split(':').str[1]


# strip the space in the ticker

globaltitans['Ticker'] = globaltitans['Ticker'].str.strip()

# %%
# convert fidelity500 to a lookup dictionary
lookup = dict(fidelity500.values)

lookup

# %%
# for all values in globaltitans, if the ticker is in fidelity500, then get the cusip

globaltitans['cusip'] = globaltitans['Ticker'].apply(lambda x: lookup[x] if x in lookup else None)

globaltitans

# %%
# if the cusip does not exist, it's most likely not an american company, so drop it

globaltitans = globaltitans.dropna()

globaltitans

# %%
# now use the hedgefunds dataframe's cusips and the globaltitans dataframe's cusips to get the common ones

hedgefund_cusips = hedgefunds['cusip'].tolist()

globaltitans_cusips = globaltitans['cusip'].tolist()


# get the common cusips

common_cusips = list(set(hedgefund_cusips) & set(globaltitans_cusips))

common_cusips

# %%
# then, find what these common cusips are in the hedgefunds dataframe

strategic_funds = hedgefunds[hedgefunds['cusip'].isin(common_cusips)]

# reset index and show the dataframe

strategic_funds = strategic_funds.reset_index(drop=True)

strategic_funds

strategic_funds.to_csv('strategic_funds.csv')

# convert this to excel 

strategic_funds.to_excel('strategic_funds.xlsx')


