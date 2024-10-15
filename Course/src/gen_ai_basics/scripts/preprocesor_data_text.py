from transformers import AutoTokenizer

# Initialize tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')

# Single sequence encoding and decoding
sequence = "To live life, you need problems. If you get everything you want the minute you want it, what’s the point of living?"
encoded_input = tokenizer(sequence)
print(encoded_input)
decoded_output = tokenizer.decode(encoded_input["input_ids"])
print(decoded_output)

print("Multi batch---------------------------")
batch_sentences = [
    "Sometimes, you don’t cry because you’re afraid of real emotion.",
    "You’re letting your brain dial turn your fear volume up.",
    "Responsibility demands sacrifice.",
]
encoded_inputs = tokenizer(batch_sentences)
print(encoded_inputs)
for encoded_input_obj in encoded_inputs["input_ids"]:
    decoded_output = tokenizer.decode(encoded_input_obj)
    print(decoded_output)

print("Padding---------------------------")
encoded_inputs_with_padding = tokenizer(batch_sentences, padding=True)
print(encoded_inputs_with_padding)
for encoded_input_obj in encoded_inputs_with_padding["input_ids"]:
    decoded_output = tokenizer.decode(encoded_input_obj)
    print(decoded_output)

print("Truncation---------------------------")
max_length = tokenizer.model_max_length
print("MAX TRUNCATION:", max_length)

super_long_sentence = "Finn and Jake " * (max_length + 1)
print("super_long_sentence length=", len(super_long_sentence))

encoded_input = tokenizer(batch_sentences, padding=False, truncation=True)
print(encoded_input)
print(len(encoded_input["input_ids"][0]))

print("Build tensors--------------------")
batch_with_super_long_sentence = [
    super_long_sentence,
    "You’re letting your brain dial turn your fear volume up.",
    "Responsibility demands sacrifice.",
]

# For both PyTorch and TensorFlow
tensor_types = ["pt", "tf"]
for tensor_type in tensor_types:
    encoded_input = tokenizer(batch_with_super_long_sentence, padding=True, truncation=True, return_tensors=tensor_type)
    print("==================TENSOR TYPE=", tensor_type)
    print(encoded_input)