#Makes a prediction using either the PyTorch model or Linear Regression model
import torch
import pandas as pd

def use_tensor_model(model, new_features, scaler):
    new_features_scaled = scaler.transform(new_features)
    new_features_tensor = torch.tensor(new_features_scaled, dtype=torch.float32)

    model.eval()
    with torch.no_grad():
        predictons = model(new_features_tensor) * 10

    return predictons

def use_regression_model(model, new_features, scaler):
    uc_hectares = pd.to_numeric(new_features['uc_hectares'], errors='coerce')
    new_features = scaler.transform(new_features)
    predictions = model.predict(new_features)
    
    #Differentiates between uc_hectares being less than 1 as scaling needs to change to maintain accuracy
    if uc_hectares.iloc[0] <= 1:    
        predictions[:, 0] = abs(predictions[:, 0]) / 100
    else:
        predictions[:, 0] = abs(predictions[:, 0]) / 10
    predictions[:, 1] = predictions[:, 1] * 10
    
    return predictions