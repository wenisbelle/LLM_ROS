from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="./EsperBERTo",
    tokenizer="./EsperBERTo",
    device=0
)


result = fill_mask("La suno <mask>.")
print(result)

result = fill_mask("Jen la komenco de bela <mask>.")
print(result)