from evaluations.evaluation import true
import pandas as pd

def ensemble():
    data = pd.read_csv('evaluations/Train.csv')
    data["Date"] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    data['EMA_5'] = data['Close'].ewm(span=5, adjust=False).mean()
    data['EMA_10'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()

    data['MACD'] = data['EMA_12'] - data['EMA_26']
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

    data['signalE'] = -1

    data.loc[(data['EMA_5'] > data['EMA_10']) & (data['MACD'] > data['Signal_Line']), 'signalE'] = 1
    data.loc[(data['EMA_5'] < data['EMA_10']) & (data['MACD'] < data['Signal_Line']), 'signalE'] = 0

    ema_data = data[["signal","signalE","body"]]

    new_data = ema_data[ema_data['signalE'] >= 0]

    pred = ema_data[ema_data["signal"] == ema_data['signalE']]["body"].sum()
    print(f"Ensemble prediction : {pred} Accuracy : {pred / true}")


