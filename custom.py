import pandas as pd
import numpy as np
from evaluations.evaluation import evaluation, true

def nadaraya_watson_envelope(src, h, mult):
    n = len(src)
    coefs = np.array([gauss(i, h) for i in range(500)])
    den = coefs.sum()

    out = np.zeros(n)

    for i in range(n):
        sum_w = 0
        sum_src_w = 0

        for j in range(min(500, i + 1)):
            w = gauss(i - j, h)
            sum_src_w += src[j] * w
            sum_w += w

        out[i] = float(sum_src_w / sum_w) if sum_w != 0 else float('nan')

    mae = np.mean(np.abs(src - out)) * mult

    upper = (out + mae) * 0.9998
    lower = (out - mae) * 1.0002
    
    return out, upper, lower

def gauss(x, h):
    return np.exp(-(x**2) / (2 * h * h))

def trading_signals():
    data = pd.read_csv('evaluations/Train.csv')
    data["Date"] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    h = 8
    mult = 2

    close_prices = data['Close'].values
    envelope, upper_band, lower_band = nadaraya_watson_envelope(close_prices, h, mult)

    previous_signal = 0

    signals = []
    
    for i in range(len(close_prices)):
        current_signal = previous_signal
        
        if close_prices[i] < lower_band[i]:
            current_signal = 0  # Sell signal
        elif close_prices[i] > upper_band[i]:
            current_signal = 1   # Buy signal
        
        signals.append(current_signal)
        previous_signal = current_signal

    data['signal'] = signals
    
    signals_df = data[["signal"]]
    
    pred = evaluation(signals_df, "evaluations/test.csv")

    return str(round(pred, 1)), str(round(pred / true, 2))
