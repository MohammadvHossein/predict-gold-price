from evaluations.evaluation import evaluation, true
import pandas as pd


def EMA():
    data = pd.read_csv('evaluations/test_15min.csv')
    data["Date"] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    data['EMA_12'] = data['Close'].ewm(span=7, adjust=False).mean()
    data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['signal'] = 0

    data.loc[data['EMA_12'] > data['EMA_26'], 'signal'] = 1

    ema_data = data[["signal"]]

    pred = evaluation(ema_data, "evaluations/test.csv")

    return str(round(pred, 1)), str(round(pred / true, 2))
