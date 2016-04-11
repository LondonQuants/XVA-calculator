import pandas as pd
from pandas_datareader.data import DataReader

symbols_list = ['ORCL', 'TSLA', 'IBM','YELP', 'MSFT']
d = {}
for ticker in symbols_list:
    d[ticker] = DataReader(ticker, "yahoo", '2016-03-01')
pan = pd.Panel(d)
df1 = pan.minor_xs('Adj Close')
print(df1)