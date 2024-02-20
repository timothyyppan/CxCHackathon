from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset

def use_model(model, new_features):
    scaler = StandardScaler().fit(new_features)
    new_features_scaled = scaler.transform(new_features)
    new_features_tensor = torch.tensor(new_features_scaled, dtype=torch.float32)

    model.eval()
    with torch.no_grad():
        predictons = model(new_features_tensor) * 100

    print(predictons)
