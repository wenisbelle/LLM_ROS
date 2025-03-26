import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import torch
result = torch.cuda.is_available()
print("IS NVIDIA SYSTEMS AVAILABLE=",result)

from transformers import RobertaConfig

config = RobertaConfig(
    vocab_size=52_000,
    max_position_embeddings=514,
    num_attention_heads=8,    # reduced from 12
    num_hidden_layers=4,      # reduced from 6
    hidden_size=256,          # smaller size, default for base model is 768
    type_vocab_size=1,
)


from transformers import RobertaTokenizerFast

tokenizer = RobertaTokenizerFast.from_pretrained("./EsperBERTo", max_len=512)

from transformers import RobertaForMaskedLM

model = RobertaForMaskedLM(config=config)

params = model.num_parameters()
print("Model Number of Params=",params)


from datasets import load_dataset

raw_datasets = load_dataset('text', data_files={'train': './eo_data/oscar_eo/oscar.eo.txt'})

def tokenize_function(examples):
    return tokenizer(examples['text'], padding='max_length', truncation=True, max_length=128, return_tensors='pt')

tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)

from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)

from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./EsperBERTo",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=32,  
    per_device_eval_batch_size=32,   
    save_steps=10_000,
    save_total_limit=2,
    prediction_loss_only=True,
)


trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=tokenized_datasets["train"],
)

trainer.train()

trainer.save_model("./EsperBERTo")