import pandas as pd

resolution = "30min"
data = pd.read_csv(f'collect-data/paxgusdt_{resolution}.csv')

# print(data.head())
split_date = '2024-06-01'
mask_train = data['Date'] < split_date
mask_test = data['Date'] >= split_date

X_train = data[mask_train]
X_test = data[mask_test]

print(X_train.shape)
print(X_train.head())
X_train.to_csv(f"datasets/train_{resolution}.csv")

print("---------------------------------------")

print(X_test.shape)
print(X_test.head())
X_test.to_csv(f"datasets/test_{resolution}.csv")

