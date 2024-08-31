import chardet
import os
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


print(device)


def detect_file_encoding(file_path, file_sample=1000):
    with open(file_path, "rb") as f:
        raw_data = f.read(file_sample)
        result = chardet.detect(raw_data)
        encoding = result["encoding"]
        return encoding


# uses utf-16 encoding
list_train = "data/Directions01/list_train.txt"
# uses utf-8 encoding
list_test = "data/Directions01/list_test.txt"

label_map = {"down": 0, "left": 1, "right": 2, "up": 3}


class CustomOrientationDataset(Dataset):
    def __init__(self, file_list, transform=None):
        self.file_list = file_list
        self.transform = transform

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        img_path, label_str = self.file_list[idx]
        image = Image.open(img_path).convert("RGB")
        label = label_map[label_str]

        if self.transform:
            image = self.transform(image)

        return image, label


with open(list_train, "r", encoding=detect_file_encoding(list_train)) as f:
    train_data = f.readlines()
    train_data = [line.strip().split(",") for line in train_data]

with open(list_test, "r", encoding=detect_file_encoding(list_test)) as f:
    test_data = f.readlines()
    test_data = [line.strip().split(",") for line in test_data]

transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        ),
    ]
)
dataset = CustomOrientationDataset(train_data, transform=transform)

dataloader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=4)

model = models.resnet18(pretrained=True)
model.fc = nn.Linear(model.fc.in_features, len(label_map))


model.eval()

for inputs, labels in dataloader:
    # inputs, labels = inputs.to(device), labels.to(device)

    outputs = model(inputs)

    _, preds = torch.max(outputs, 1)

    print(f"Predicted: {preds}, Actual: {labels}")
