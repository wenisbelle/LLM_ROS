import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Step 1: Load the Model and Tokenizer
loaded_model = AutoModelForSequenceClassification.from_pretrained("model/")
loaded_tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

# Step 2: Tokenize Sample Text
text_negative = "This restaurant was the worst I ever went to in my life."
text_middle = "The restuarant was ok. The food wan't bad and the service was fairly quick."
text_positive = "Amazing place! Loved the food and the service was the best I had in a long time. Super reccomended!"
sample_texts = [text_negative,
                text_middle,
                text_positive]

for text in sample_texts:
    inputs = loaded_tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    # Step 3: Model Inference
    with torch.no_grad():  # Inference only
        outputs = loaded_model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()

    # Step 4: Interpret the Result
    label_map = {
        0: "1 star",
        1: "2 stars",
        2: "3 stars",
        3: "4 stars",
        4: "5 stars"
    }
    print(f"Predicted Rating: {label_map[predicted_class]}")