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
    if uc_hectares.iloc[0] <= 1:    
        predictions = abs(model.predict(new_features) / 100)      
    else:
        predictions = abs(model.predict(new_features) / 10)  

    return predictions