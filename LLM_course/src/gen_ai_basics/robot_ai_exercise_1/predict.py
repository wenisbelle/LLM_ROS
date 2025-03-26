import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

MODEL_PATH = './custom_t5_robot_model'
MAX_LENGTH = 512
# Load the trained model and tokenizer
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
model.eval()  # Ensure the model is in evaluation mode

def generate_robot_command(description):
    '''Generate robot command from a given movement description'''

    with torch.no_grad():
        input_text = description
        input_tensor = tokenizer(input_text, return_tensors="pt", truncation=True, padding='max_length', max_length=MAX_LENGTH).input_ids.to(device)
        output_tensor = model.generate(input_tensor, max_length=MAX_LENGTH)  # Adjust as needed
        output_text = tokenizer.decode(output_tensor[0], skip_special_tokens=True)
        command = output_text

        return command

# Test the function
description = ""
while True:
    description = input("Type the human instructions, seprataed by and , or then. Finish with full stop >>>")
    command = generate_robot_command(description)
    print("Description="+description+",Generated Command="+command)