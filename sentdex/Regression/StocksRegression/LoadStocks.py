import quandl
quandl.ApiConfig.api_key = 'key -.-'
df = quandl.get('WIKI/GOOGL')

df.to_csv('stocks.csv')
#this is make a new csv file and store the google stocks in that
#awesome

#hahahahaa
#lol that actually works somehow
