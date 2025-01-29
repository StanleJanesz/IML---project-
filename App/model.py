import torch.nn as nn

class Net(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1),  # (N, 32, 64, 64)
            nn.BatchNorm2d(num_features = 32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  # (N, 32, 32, 32)

            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),  # (N, 64, 32, 32)
            nn.BatchNorm2d(num_features = 64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  # (N, 64, 16, 16)

            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),  # (N, 128, 16, 16)
            nn.BatchNorm2d(num_features = 128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)  # (N, 128, 8, 8)
        )
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(36864, 256 * 4),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256 * 4, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x
    