import ccxt
import pandas as pd
import time

exchange = ccxt.kucoin()
ticker = 'PAXG/USDT'
timeframe = '30m'

# Fetch data for 2022
since_2022 = exchange.parse8601('2022-01-01T00:00:00Z')
end_2022 = exchange.parse8601('2023-01-01T00:00:00Z')
data_2022 = []
while since_2022 < end_2022:
    try:
        data = exchange.fetch_ohlcv(ticker, timeframe, since_2022, limit=1000)
        if not data:
            break
        data_2022.extend(data)
        since_2022 = data[-1][0] + 1
        time.sleep(1)
    except Exception as e:
        print(f"Error fetching data for 2022: {e}")
        break

df_2022 = pd.DataFrame(data_2022, columns=[
                       'timestamp', 'open', 'high', 'low', 'close', 'volume'])
df_2022['timestamp'] = pd.to_datetime(df_2022['timestamp'], unit='ms')
df_2022.rename(columns={'timestamp': 'Date', 'open': 'Open', 'high': 'High',
               'low': 'Low', 'close': 'Close', 'volume': 'Volume'}, inplace=True)

since_2023 = exchange.parse8601('2023-01-01T00:00:00Z')
end_2023 = exchange.parse8601('2024-01-01T00:00:00Z')
data_2023 = []
while since_2023 < end_2023:
    try:
        data = exchange.fetch_ohlcv(ticker, timeframe, since_2023, limit=1000)
        if not data:
            break
        data_2023.extend(data)
        since_2023 = data[-1][0] + 1
        time.sleep(1)
    except Exception as e:
        print(f"Error fetching data for 2023: {e}")
        break

df_2023 = pd.DataFrame(data_2023, columns=[
                       'timestamp', 'open', 'high', 'low', 'close', 'volume'])
df_2023['timestamp'] = pd.to_datetime(df_2023['timestamp'], unit='ms')
df_2023.rename(columns={'timestamp': 'Date', 'open': 'Open', 'high': 'High',
               'low': 'Low', 'close': 'Close', 'volume': 'Volume'}, inplace=True)

since_2024 = exchange.parse8601('2024-01-01T00:00:00Z')
end_2024 = exchange.parse8601('2025-01-01T00:00:00Z')
data_2024 = []
while since_2024 < end_2024:
    try:
        data = exchange.fetch_ohlcv(ticker, timeframe, since_2024, limit=1000)
        if not data:
            break
        data_2024.extend(data)
        since_2024 = data[-1][0] + 1
        time.sleep(1)
    except Exception as e:
        print(f"Error fetching data for 2024: {e}")
        break

df_2024 = pd.DataFrame(data_2024, columns=[
                       'timestamp', 'open', 'high', 'low', 'close', 'volume'])
df_2024['timestamp'] = pd.to_datetime(df_2024['timestamp'], unit='ms')
df_2024.rename(columns={'timestamp': 'Date', 'open': 'Open', 'high': 'High',
               'low': 'Low', 'close': 'Close', 'volume': 'Volume'}, inplace=True)

# Concatenate the DataFrames for 2022, and 2024
paxgusdt_30min_df = pd.concat([df_2022, df_2023, df_2024], ignore_index=True)

# Save the concatenated DataFrame to a CSV file
paxgusdt_30min_df.to_csv('paxgusdt_30min.csv', index=False)
print(len(paxgusdt_30min_df))