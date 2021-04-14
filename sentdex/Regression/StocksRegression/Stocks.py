import math
import datetime, matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np#numpy got arrays, python dont. very bad
from sklearn import preprocessing, model_selection, svm
#preprocessing : scaling your features, to get them between -1 and +1 :c hmmmmmmmmm
#cross_validation : create the training and testing data
#svm support vector machine : doing regression
from sklearn.linear_model import LinearRegression#hohoho


'''*****************************************************************************************************************'''
'''*****************************************************************************************************************'''
'''*****************************************************************************************************************'''

df = pd.read_csv('stocks.csv')
dates_column = df['Date']
df = df.drop(columns = ['Date','Open','High','Low','Close','Volume', 'Ex-Dividend', 'Split_Ratio'])
style.use('ggplot')
df['high_low_pct'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
df['open_close_pct'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df.drop(columns = ['Adj. Open', 'Adj. High', 'Adj. Low'])
forecast_column = 'Adj. Close'

df.fillna(-9999, inplace = True) #this will fill up the NaN values in the dataframe, and the model will treat this as the outlier, meaning abnormal data
#inplace = True meaning the object itself changes, and not returning a new object with the changes

forecast_out = int(math.ceil(0.01*len(df)))
# we are going to use this as the testing data

df['label'] = df[forecast_column].shift(-forecast_out)
#well, the last few forcast_out columns will be put as NaN...meaning they are empty, they are the ones we want to predict.


'''*****************************************************************************************************************'''
'''*****************************************************************************************************************'''
'''*****************************************************************************************************************'''

#now the splitting of data
#use X for features, y for labels

df.dropna(inplace = True)
X = np.array(df.drop(columns = ['label']))

X_lately = X[-forecast_out:]#this is the last thirty days of data that we would like to predict

y = np.array(df['label'])

#df.dropna(inplace = True)

'''*****************************************************************************************************************'''
'''*****************************************************************************************************************'''
'''*****************************************************************************************************************'''

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.2)

clf = LinearRegression()
clf.fit(X_train, y_train)# the training data is given the the model
confidence = clf.score(X_test, y_test)#testing the accuracy with the testing data
