import torch

def use_tensor_model(model, new_features, scaler):
    new_features_scaled = scaler.transform(new_features)
    new_features_tensor = torch.tensor(new_features_scaled, dtype=torch.float32)

    model.eval()
    with torch.no_grad():
        predictons = model(new_features_tensor) * 10

    return predictons

def use_regression_model(model, new_features, scaler):
    new_features = scaler.transform(new_features)
    predictions = model.predict(new_features)

    return predictions