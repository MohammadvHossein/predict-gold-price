from evaluations.evaluation import evaluation, true
import pandas as pd


def MACD():
    data = pd.read_csv('evaluations/test_15min.csv')
    data["Date"] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA_12'] - data['EMA_26']
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    data['signal'] = 0

    data.loc[data['MACD'] > data['Signal_Line'], 'signal'] = 1

    macd = data[["signal"]]

    pred = evaluation(macd, "evaluations/test.csv")

    return str(round(pred, 1)), str(round(pred / true, 2))
