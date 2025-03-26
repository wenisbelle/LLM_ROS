import numpy as np
import matplotlib.pyplot as plt
from datasets import load_dataset
from transformers import AutoImageProcessor
from torchvision.transforms import RandomResizedCrop, ColorJitter, Compose

# Load dataset and display the first image
dataset = load_dataset("food101", split="train[:100]")

#dataset[0]["image"].show()

# Initialize the image processor
image_processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")

# Determine the image size for transformations
size = image_processor.size.get("shortest_edge", 
       (image_processor.size["height"], image_processor.size["width"]))

# Define transformations
_transforms = Compose([RandomResizedCrop(size), ColorJitter(brightness=0.5, hue=0.5)])

def transform_images(examples):
    
    """Applies transformations to the images and processes them."""
    
    images = [_transforms(img.convert("RGB")) for img in examples["image"]]
    examples["pixel_values"] = image_processor(images, do_resize=False, return_tensors="pt")["pixel_values"]
    return examples

# Apply transformations
dataset.set_transform(transform_images)

# Get the processed image and convert to a format suitable for display
img = dataset[0]["pixel_values"].numpy()

# Normalize image if required
if img.min() < 0:
    img = (img + 1) / 2.0

# Display the image
plt.imshow(np.clip(img, 0, 1).transpose(1, 2, 0))
plt.show()