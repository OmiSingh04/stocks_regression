import pandas as pd
import math

df = pd.read_csv('stocks.csv')
df = df.drop(columns = ['Date','Open','High','Low','Close','Volume', 'Ex-Dividend', 'Split_Ratio'])

df['high_low_pct'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
df['open_close_pct'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df.drop(columns = ['Adj. Open', 'Adj. High', 'Adj. Low'])

forecast_column = 'Adj. Close'

df.fillna(-9999, inplace = True) #this will fill up the NaN values in the dataframe, and the model will treat this as the outlier, meaning abnormal data
#inplace = True meaning the object itself changes, and not returning a new object with the changes

forecast_out = int(math.ceil(0.01*len(df)))
# we are going to use this as the testing data

df['label'] = df[forecast_column].shift(-forecast_out)


print(df.head(30))