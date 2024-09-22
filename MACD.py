from evaluation import evaluation
import pandas as pd

data = pd.read_csv('evaluation_data.csv')
data["Date"] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
data['MACD'] = data['EMA_12'] - data['EMA_26']
data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
data['Signal'] = 0

data.loc[data['MACD'] > data['Signal_Line'], 'Signal'] = 1

ema_data = data[["signal"]]

print(evaluation(ema_data))

# max score 111412.32999999546
# score this code  111412.32999999546

