#!/usr/bin/env python3
import torch
import matplotlib.pyplot as plt
from PIL import Image
from transformers import CLIPSegProcessor, CLIPSegForImageSegmentation
import numpy as np


class ImageSegmentation(object):
    def __init__(self):
        # Load models
        self.processor = CLIPSegProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
        self.model = CLIPSegForImageSegmentation.from_pretrained("CIDAS/clipseg-rd64-refined")

    def generate_image_segmentation(self, image, segment_list, plot=True):

        # Process the inputs
        inputs = self.processor(text=segment_list, images=image, padding=True, return_tensors="pt")

        # Get outputs
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits

        # Process the logits
        image = torch.sigmoid(logits).numpy()
         

        if plot:
            # Plot results
            plt.imshow(image[0])

            plt.axis('off')  # Hide axis
            plt.show()
       
        return image

    
    def open_image(self, img_path):
        image = Image.open(img_path)
        return image



def main():
    
    seg_obj = ImageSegmentation()
    img_path = "/LLM_course/src/vision_language_models/images/thug.png"
    image = seg_obj.open_image(img_path)
    object_list = ["person"]
    seg_obj.generate_image_segmentation(image, object_list)

    

if __name__ == "__main__":
    main()