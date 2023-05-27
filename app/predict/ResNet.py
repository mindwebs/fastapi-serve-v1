import json

import torch
from torchvision.io import ImageReadMode, read_image
from torchvision.models.resnet import ResNet18_Weights

from .types import ImageClassifierModel


def get_idx2label() -> list:
    with open("./app/predict/imagenet_class_index.json", "r") as class_file:
        class_idx = json.load(class_file)
        return [class_idx[str(k)][1] for k in range(len(class_idx))]


class ResNetImgModel(ImageClassifierModel):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = torch.hub.load(
        "pytorch/vision:v0.10.0", "resnet18", weights=ResNet18_Weights.DEFAULT
    ).to(
        device
    )  # Default Imagenet Weights
    idx2label = get_idx2label()

    def predict(self, image_path: str) -> str:
        # Step 1: Get out image tensor
        img_tensor = (
            read_image(image_path, ImageReadMode.RGB).float().to(ResNetImgModel.device)
        )  # Use Pillow for non-torch impl.

        # Step 2: Get model outputs
        out = ResNetImgModel.model(img_tensor.unsqueeze(0))

        # Step 3: Output post-processing
        out = torch.argmax(out, 1).item()
        out = ResNetImgModel.idx2label[out]
        return out
