import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import GridSearchCV

def create_features(data):
    data['price_change'] = data['Close'] - data['Open']
    data['high_low'] = data['High'] - data['Low']
    data['signal'] = (data['Close'] >= data['Open']).astype(int)    
    data['target'] = data['signal'].shift(-1)  
    return data.dropna()

def load_and_prepare_data(file_path):
    data = pd.read_csv(file_path)
    return data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

def classifier():
    train_data = load_and_prepare_data('datasets/train_15min.csv')
    test_data = load_and_prepare_data('datasets/test_15min.csv')

    train_data = create_features(train_data)
    test_data = create_features(test_data)

    train_features = train_data[['price_change', 'high_low', 'Close', 'Volume']]
    train_target = train_data['target']

    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2],
        'subsample': [0.8, 1.0]
    }

    model = xgb.XGBClassifier(eval_metric='logloss')

    grid_search = GridSearchCV(estimator=model, param_grid=param_grid,
                               scoring='accuracy', cv=3, verbose=1)

    grid_search.fit(train_features, train_target)

    best_model = grid_search.best_estimator_

    test_features = test_data[['price_change', 'high_low', 'Close', 'Volume']]
    predictions = best_model.predict(test_features)

    output = pd.DataFrame({
        'open time': test_data['Date'],
        'signal': predictions
    })

    # print(f"Best parameters: {grid_search.best_params_}")
    
    return output

