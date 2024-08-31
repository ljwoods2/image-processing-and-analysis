from PIL import Image
import torchvision.transforms as transforms
import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


def load_image(image_path):
    image = Image.open(image_path)
    return image


def transform_image(image):
    transform = transforms.ToTensor()
    image = transform(image)
    return image


img = load_image("data/Practice_PNGandJPG/chestimage_JPG/JPCLN001.jpg")
print(img)


transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        ),
    ]
)

dataset = datasets.ImageFolder(root="Practice_PNGandJPG", transform=transform)

# Create a DataLoader
dataloader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=4)
