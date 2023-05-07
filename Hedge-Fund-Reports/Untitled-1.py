# %%
# # !pip install secedgar

# from secedgar import filings, FilingType

# import nest_asyncio
# nest_asyncio.apply()

# %%
#FIXME: For some reason, the API does not seem to work properly and returns "Forbidden" error, so I went ahead and downloaded the data manually and saved it in the data folder.
# my_filings = filings(cik_lookup=["Renaissance Technologies LLC"],
#                      filing_type=FilingType.FILING_13FHR,
#                      user_agent="John")
# my_filings.save('./data/')

# %%
import pandas as pd 

# %%
# get the data from the xml files
bridgewater = pd.read_xml("./data/bridgewater.xml")
citadel = pd.read_xml("data/citadel.xml")
deshaw = pd.read_xml("data/deshaw.xml")
mlp = pd.read_xml("data/MLP.xml")
rennaissance = pd.read_xml("data/renaissance.xml")
twosigma = pd.read_xml("data/twosigma.xml")

# %%
# get rid of the spacing of company names
bridgewater["nameOfIssuer"] = bridgewater["nameOfIssuer"].str.strip()
citadel["nameOfIssuer"] = citadel["nameOfIssuer"].str.strip()
deshaw["nameOfIssuer"] = deshaw["nameOfIssuer"].str.strip()
mlp["nameOfIssuer"] = mlp["nameOfIssuer"].str.strip()
rennaissance["nameOfIssuer"] = rennaissance["nameOfIssuer"].str.strip()
twosigma["nameOfIssuer"] = twosigma["nameOfIssuer"].str.strip()

# %%
print(len(bridgewater))
print(len(citadel))
print(len(deshaw))
print(len(mlp))
print(len(rennaissance))
print(len(twosigma))

# %%
# only get companies with unique cusips in each portfolio 

test =[]

test.append(bridgewater.drop_duplicates(subset=['cusip'], keep='first')['cusip'])

test.append(citadel.drop_duplicates(subset=['cusip'], keep='first')['cusip'])

test.append(deshaw.drop_duplicates(subset=['cusip'], keep='first')['cusip'])

test.append(mlp.drop_duplicates(subset=['cusip'], keep='first')['cusip'])

test.append(rennaissance.drop_duplicates(subset=['cusip'], keep='first')['cusip'])

test.append(twosigma.drop_duplicates(subset=['cusip'], keep='first')['cusip'])

# %%
test = set(test[0])

# %%
# convert set to list 
test = list(test)
test.sort()
len(test)

# %%
# make a master_list with all portfolios and add what portfolio they're from

master_list = pd.DataFrame(columns = bridgewater.columns)

bridgewater['FromPortfolio'] = 'Bridgewater'
citadel['FromPortfolio'] = 'Citadel'
deshaw['FromPortfolio'] = 'Deshaw'
mlp['FromPortfolio'] = 'MLP'
rennaissance['FromPortfolio'] = 'Renaissance'
twosigma['FromPortfolio'] = 'TwoSigma'

master_list = master_list.append(bridgewater)
master_list = master_list.append(citadel)
master_list = master_list.append(deshaw)
master_list = master_list.append(mlp)
master_list = master_list.append(rennaissance)
master_list = master_list.append(twosigma)


master_list

# %%
# check for duplicates and remove them
master_list = master_list.drop_duplicates(subset=['cusip'], keep='first')

master_list = master_list[master_list['cusip'].isin(test)]

# drop shrsOrPrnAmt	investmentDiscretion	votingAuthority	FromPortfolio	putCall	otherManager
master_list = master_list.drop(columns=['shrsOrPrnAmt', 'investmentDiscretion', 'votingAuthority', 'FromPortfolio', 'putCall', 'otherManager'])

# master_list export to csv 
master_list.to_csv('master_list.csv')

master_list.sort_values(by=['value'], ascending=False)


