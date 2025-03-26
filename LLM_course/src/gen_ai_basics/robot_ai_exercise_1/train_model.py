import torch
from datasets import load_dataset
from torch.utils.data import DataLoader
from torch.optim import AdamW
from transformers import T5Tokenizer, T5ForConditionalGeneration

BATCH_SIZE = 2

# Load the dataset
# Assuming the dataset is in a csv format with 'Human Command' and 'Robot Command' columns
dataset = load_dataset('csv', data_files={'train': 'train.csv', 'test': 'test.csv'})

# Tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-small')
MAX_LENGTH = 512

def encode_data(example):
    source = example['Human Command']
    target = example['Robot Command']

    source_tokenized = tokenizer(source, max_length=MAX_LENGTH, truncation=True, padding='max_length', return_tensors='pt')
    target_tokenized = tokenizer(target, max_length=MAX_LENGTH, truncation=True, padding='max_length', return_tensors='pt')

    return {
        'input_ids': source_tokenized['input_ids'][0],
        'attention_mask': source_tokenized['attention_mask'][0],
        'labels': target_tokenized['input_ids'][0]
    }

# Encoding the dataset
encoded_dataset = dataset.map(encode_data)

# Convert encoded dataset to PyTorch format
train_dataset = torch.utils.data.TensorDataset(
    torch.tensor(encoded_dataset['train']['input_ids']),
    torch.tensor(encoded_dataset['train']['attention_mask']),
    torch.tensor(encoded_dataset['train']['labels'])
)

train_loader = DataLoader(train_dataset, shuffle=True, batch_size=BATCH_SIZE)


# Model
model = T5ForConditionalGeneration.from_pretrained('t5-small')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Training loop
optimizer = AdamW(model.parameters(), lr=5e-5)
EPOCHS = 3

for epoch in range(EPOCHS):
    total_loss = 0.0
    model.train()

    for i, data in enumerate(train_loader):
        optimizer.zero_grad()

        input_ids, attention_mask, labels = data
        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)
        labels = labels.to(device)

        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        if i % 10 == 0:
            print(f"Epoch {epoch} | Batch {i} | Current Loss: {loss.item()}")

    avg_train_loss = total_loss / len(encoded_dataset['train'])
    print(f"Epoch {epoch} | Average Training Loss: {avg_train_loss}")

# Save model
model.save_pretrained('./custom_t5_robot_model')
tokenizer.save_pretrained('./custom_t5_robot_model')