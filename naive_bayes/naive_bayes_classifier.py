import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB


def create_features(data):
    data['price_change'] = data['Close'] - data['Open']
    data['high_low'] = data['High'] - data['Low']
    data["signal"] = np.where(data["Close"] >= data["Open"], 1, 0).astype(int)    
    data['target'] = data["signal"].shift(-1)  
    data.dropna(inplace=True)
    return data

def classifier():
    train_data_path = 'datasets/train_15min.csv'
    test_data_path = 'datasets/test_15min.csv'
    train_data = pd.read_csv(train_data_path) 
    test_data = pd.read_csv(test_data_path) 
    train_data = train_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    test_data = test_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

    # Preprocess the training data
    train_data = create_features(train_data)  # Added this line
    test_data = create_features(test_data)    # Preprocess test data

    train_features = train_data[['price_change', 'high_low', 'Close', 'Volume']]
    train_target = train_data['target']

    # Train the Naive Bayes model
    model = GaussianNB()
    model.fit(train_features, train_target)

    # Prepare test features
    test_features = test_data[['price_change', 'high_low', 'Close', 'Volume']]

    # Make predictions
    predictions = model.predict(test_features)

    # Create output DataFrame
    output = pd.DataFrame({
        'open time': test_data['Date'],
        'signal': predictions
    })
    return output
