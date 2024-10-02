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

    data.loc[(data['EMA_5'] > data['EMA_10']) & (
        data['MACD'] > data['Signal_Line']), 'signalE'] = 1
    data.loc[(data['EMA_5'] < data['EMA_10']) & (
        data['MACD'] < data['Signal_Line']), 'signalE'] = 0

    ensemble = data[["signal", "signalE", "body"]]

    pred = ensemble[ensemble["signal"] == ensemble['signalE']]["body"].sum()

    return str(round(pred, 1)), str(round(pred / true, 2))
