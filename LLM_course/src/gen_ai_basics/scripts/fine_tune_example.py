# Importing required libraries and modules
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


import numpy as np
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import torch

# Check if CUDA (GPU) is available
if torch.cuda.is_available():
    # Get the current GPU device ID
    current_device = torch.cuda.current_device()
    
    # Print the GPU being used
    print("Current GPU device:", current_device)
    print("GPU name:", torch.cuda.get_device_name(current_device))
    print("Total GPUs available:", torch.cuda.device_count())
else:
    print("No GPU is being used. Running on CPU.")

# Load the dataset
dataset = load_dataset("yelp_review_full")

# Tokenization
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

for i in range(2):
    print("#######################")
    print(dataset["train"]["text"][i])
    print(dataset["train"]["label"][i])


def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Creating smaller datasets for demo purposes
small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))
small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(1000))

# Model Initialization
num_labels = 5  # Number of labels in the yelp_review_full dataset
model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=num_labels)

# Defining the metric for evaluation
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    # Assuming the `evaluate` module provides a function to compute accuracy. Make sure this import and function are valid.
    import evaluate
    metric = evaluate.load("accuracy")
    return metric.compute(predictions=predictions, references=labels)

# Setting training arguments
training_args = TrainingArguments(
    output_dir="test_trainer",
    per_device_train_batch_size=12,
    per_device_eval_batch_size=12,
    evaluation_strategy="epoch",
    fp16=torch.cuda.is_available(),  # set fp16 based on CUDA's availability
)

# Training the model
print("Training with PyTorch..........")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset,
    compute_metrics=compute_metrics,
)

trainer.train()
trainer.save_model("model/")