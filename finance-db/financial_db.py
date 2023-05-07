# %%
import yfinance as yf
import quantstats as qs
import requests
import pandas as pd

# %%
link = "https://yhoo.it/3FmbOqZ"


actual_link = requests.get(link).url

# the tickers are separated by a comma after /quotes/ 
actual_link = actual_link.split("/quotes/")[1]

actual_link


list_of_tickers = actual_link.split(",")

list_of_tickers



# remove the last ticker's /view/v1?ncid=yahooproperties_portfolios_pbodyv8zfja 

list_of_tickers[-1] = list_of_tickers[-1].split("/view/v1?ncid=yahooproperties_portfolios_pbodyv8zfja")[0]

list_of_tickers

# %%
#  get data for these tickers
# data = yf.download(list_of_tickers, period="max")

data = [] 

for ticker in list_of_tickers:
    data.append(yf.download(ticker, period="max"))

# %%
data[0]

# %%
# create a sql engine 

from sqlalchemy import create_engine

engine = create_engine('sqlite:///data.db', echo=False)

# if the dataframe is empty, write down what ticker that is 


for i in range(len(list_of_tickers)):
    if data[i].empty:
        list_of_tickers.remove(list_of_tickers[i])
        print("The ticker " + list_of_tickers[i] + " is empty")
# data[i].to_sql(list_of_tickers[i], con=engine, if_exists='replace')

for i in range(len(list_of_tickers)):
    data[i].to_sql(list_of_tickers[i], con=engine, if_exists='replace')

# %%
pd.read_sql("select * from SCHW where Date > '2021-01-01'", con=engine)

# %%
# find where the schwab stock had the highest trade volume
# https://www.cnbc.com/2023/03/13/charles-schwab-shares-head-for-worst-day-ever-as-fears-of-banking-crisis-deepen.html 
# sounds about right. that's the time in which Schwab got a lot of attention due to SVB collapse. 
pd.read_sql("select * from SCHW where Volume = (select max(Volume) from SCHW)", con=engine)

# %%
# Note: The database file is not included in the repo because it's larger than 100 MB which exceeds the limit of GH.


