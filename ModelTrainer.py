from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn
import torch.nn.functional as F


def train_model(df):
    features = df[['current_size', 'assessment_hectares', 
                        'fire_spread_rate', 'temperature', 
                        'relative_humidity', 'wind_speed', 
                        'uc_hectares', 'ex_hectares']]

    target = df[['ex_hectares', 'impact_score']]

    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.fit_transform(x_test)

    x_train_tensor = torch.tensor(x_train_scaled, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32)
    x_test_tensor = torch.tensor(x_test_scaled, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32)

    batch_size = 64

    train_dataset = TensorDataset(x_train_tensor, y_train_tensor)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    test_dataset = TensorDataset(x_test_tensor, y_test_tensor)
    test_loader = DataLoader(test_dataset, batch_size=batch_size)

    model = WildfireNet()
    criterion = nn.MSELoss()  # Mean Squared Error Loss for regression tasks
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    epochs = 100

    for epoch in range(epochs):
        model.train()
        for data, targets in train_loader:
            optimizer.zero_grad()
            outputs = model(data)
            loss = criterion(outputs, targets.unsqueeze(1))
            loss.backward()
            optimizer.step()
        print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')
    
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0
        for data, targets in test_loader:
            outputs = model(data)
            predicted = outputs.data
            total += targets.size(0)
            correct += (predicted == targets.unsqueeze(1)).sum().item()
        print(f'Accuracy of the model on the test set: {100 * correct / total}%')

#Fix this class
class WildfireNet(nn.Module):
    def __init__(self):
        super(WildfireNet, self).__init__()
        self.fc1 = nn.Linear(x_train.shape[1], 128)  # Adjust according to the number of features
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)  # Output layer for regression

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x