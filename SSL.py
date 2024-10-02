import pandas as pd
from evaluations.evaluation import evaluation, true

def SSL():
    data = pd.read_csv('evaluations/Train.csv')
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
        true_range = pd.concat(
            [high_low, high_close, low_close], axis=1).max(axis=1)
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

    data['signal'] = 0

    data.loc[data['Close'] > data[['SMA_High_SSL1', 'SMA_Low_SSL1']].max(
        axis=1), 'signal'] = 1

    data.loc[data['Close'] < data[['SMA_High_SSL1', 'SMA_Low_SSL1']].min(
        axis=1), 'signal'] = 0

    ssl = data[["signal"]]

    pred = evaluation(ssl, "evaluations/test.csv")

    return str(round(pred, 1)), str(round(pred / true, 2))
