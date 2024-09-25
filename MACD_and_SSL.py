import pandas as pd

data = pd.read_csv('Train.csv')
data["Date"] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

len_ssl1 = 55
len_ssl2 = 5 
len_exit = 15
atrlen = 14
mult = 1.5 

def calculate_atr(data, window):
    high_low = data['High'] - data['Low']
    high_close = abs(data['High'] - data['Close'].shift(1))
    low_close = abs(data['Low'] - data['Close'].shift(1))
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = true_range.rolling(window=window).mean()
    return atr

data['ATR'] = calculate_atr(data, atrlen)

data['Upper_Band'] = data['Close'] + (data['ATR'] * mult)
data['Lower_Band'] = data['Close'] - (data['ATR'] * mult)

data['SMA_High_SSL1'] = data['High'].rolling(window=len_ssl1).mean()
data['SMA_Low_SSL1'] = data['Low'].rolling(window=len_ssl1).mean()

data['SMA_High_SSL2'] = data['High'].rolling(window=len_ssl2).mean()
data['SMA_Low_SSL2'] = data['Low'].rolling(window=len_ssl2).mean()

data['Exit_High'] = data['High'].rolling(window=len_exit).mean()
data['Exit_Low'] = data['Low'].rolling(window=len_exit).mean()

data['signal_ssl'] = 0

data.loc[data['Close'] > data[['SMA_High_SSL1', 'SMA_Low_SSL1']].max(axis=1), 'signal_ssl'] = 1

data.loc[data['Close'] < data[['SMA_High_SSL1', 'SMA_Low_SSL1']].min(axis=1), 'signal_ssl'] = 0

data['EMA_12'] = data['Close'].ewm(span=2, adjust=False).mean()
data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
data['MACD'] = data['EMA_12'] - data['EMA_26']
data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
data['signal_MACD'] = 0

data.loc[data['MACD'] > data['Signal_Line'], 'signal_MACD'] = 1


data[["signal_MACD"]]
data[['signal_ssl']]

new_data = data[["signal_MACD" , "signal_ssl" , "body"]]



real =new_data['body'].sum()
print(real)

total = 0
for index , row in enumerate(new_data.values):
    if row[0] == row[1]:
        total += row[2]

print(total)

print(total / real)