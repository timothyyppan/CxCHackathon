#Trains the PyTorch and Linear Regression Model
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
import torch.optim.lr_scheduler as lr_scheduler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
import joblib

class WildfireNet(nn.Module):
    def __init__(self, in_features):
        super(WildfireNet, self).__init__()
        self.fc1 = nn.Linear(in_features, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 2)

        nn.init.kaiming_uniform_(self.fc1.weight, nonlinearity='relu')
        nn.init.kaiming_uniform_(self.fc2.weight, nonlinearity='relu')
        nn.init.xavier_uniform_(self.fc3.weight)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def train_tensor_model(df):
    features = df[[ 'bh_hectares', 'uc_hectares',
                    'assessment_hectares', 
                    'fire_spread_rate', 'temperature', 
                    'relative_humidity', 'wind_speed'
                    ]]
    target = df[['current_size', 'impact_score']]

    # Data preparation
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    scaler = StandardScaler().fit(x_train)
    joblib.dump(scaler, 'tensor_scaler.save')
    x_train_scaled, x_test_scaled = scaler.transform(x_train), scaler.transform(x_test)

    # Convert to tensors
    x_train_tensor = torch.tensor(x_train_scaled, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32)
    x_test_tensor = torch.tensor(x_test_scaled, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32)

    # DataLoader setup
    train_dataset = TensorDataset(x_train_tensor, y_train_tensor)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_dataset = TensorDataset(x_test_tensor, y_test_tensor)
    test_loader = DataLoader(test_dataset, batch_size=64)

    # Model, loss, and optimizer
    model = WildfireNet(in_features=features.shape[1])
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0005, weight_decay=1e-5)  # Added L2 regularization

    scheduler = lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)

    epochs = 100
    for epoch in range(epochs):
        model.train()
        for data, targets in train_loader:
            optimizer.zero_grad()
            outputs = model(data)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            scheduler.step()
        
    # Evaluation
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for data, targets in test_loader:
            outputs = model(data)
            loss = criterion(outputs, targets)
            total_loss += loss.item() * data.size(0)

    return model

def train_regression_model(df):
    features = df[[ 'bh_hectares', 'uc_hectares',
                    'assessment_hectares', 
                    'fire_spread_rate', 'temperature', 
                    'relative_humidity', 'wind_speed'
                    ]]
    y_train = df[['current_size', 'impact_score']]
    x_train = features

    scaler = StandardScaler().fit(x_train)
    joblib.dump(scaler, 'regression_scaler.save')
    x_train_scaled = scaler.fit_transform(x_train)

    model = Lasso(alpha=1)

    model.fit(x_train_scaled, y_train)

    return model