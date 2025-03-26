#!/usr/bin/env python3
from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
import torch
from icecream import ic


class VisualQuestioning(object):
    def __init__(self):
        # Initialize models and processor
        self.load_models()

        message = "VisionQuestioningInitialised..."
        ic(message)

    def load_models(self):
        """Load model and processor."""
        self.model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
        self.processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")


    def show_image(self, img_path):
        """Open and display an image."""
        image = Image.open(img_path)
        image.show()
        return image

    def get_answer(self, image, question):
        """Get the predicted answer for a given question and image."""
        inputs = self.processor(image, question, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        idx = logits.argmax(-1).item()
        return self.model.config.id2label[idx]

    def question_answer_validate(self, image, question, answer_contains):

        answer = self.get_answer(image, question)
        ic("Question="+question+",["+str(answer_contains)+"] in answer?=", answer)
        success = False
        if answer_contains in answer:
            ic("YES")
            success = True
        else:
            ic("NO")

        return success

if __name__ == "__main__":
    vis_obj = VisualQuestioning()
    img_path="/LLM_course/src/vision_language_models/images/thug.png"
    image= vis_obj.show_image(img_path)
    question="Is there a person?"
    answer_contains="yes"
    vis_obj.question_answer_validate(image, question, answer_contains)