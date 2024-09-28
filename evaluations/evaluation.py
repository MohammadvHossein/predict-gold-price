import pandas as pd
import numpy as np
import os


def generate_base_data(file, is_train):
    data = pd.read_csv(file).iloc[:, 1:]
    data["Date"] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data["body"] = np.abs(data["Close"] - data["Open"])

    data["signal"] = np.where(data["Close"] >= data["Open"], 1, 0)

    # data = data[["Open", "Close",  "signal", "body"]]
    if is_train:
        if os.path.exists("evaluations/Train.csv"):
            print("File Train.csv is exists.")
        else:
            data.to_csv("evaluations/Train.csv")
    else:
        if os.path.exists("evaluations/test.csv"):
            print("File test.csv is exists.")
        else:
            data.to_csv("evaluations/test.csv")


def evaluation(result, data, method="classification"):
    if method == "classification":
        data = pd.read_csv(data)
        total = 0
        for index, signal in enumerate(result['signal']):
            if signal == data['signal'].iloc[index]:
                total += data['body'].iloc[index]
        return total
    elif method == "regression":
        pass
    else:
        print("Method is not avalible")

# generate_base_data('evaluations/test_15min.csv',is_train=False)
# generate_base_data('evaluations/test_15min.csv',is_train=True)


train = pd.read_csv('evaluations/Train.csv')
true = evaluation(train , 'evaluations/test.csv')
print(f"Main : {true}")