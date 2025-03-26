from datasets import load_dataset, Audio
dataset = load_dataset("PolyAI/minds14", name="en-US", split="train")

dataset_data = dataset[0]["audio"]
print(dataset_data)

print("Resampling audio.........")
dataset = dataset.cast_column("audio", Audio(sampling_rate=16_000))
dataset_data = dataset[0]["audio"]
print(dataset_data)

from transformers import AutoFeatureExtractor
feature_extractor = AutoFeatureExtractor.from_pretrained("facebook/wav2vec2-base")
audio_input = [dataset[0]["audio"]["array"]]
fe_inputs = feature_extractor(audio_input, sampling_rate=16000)
print(fe_inputs)

print(dataset[0]["audio"]["array"].shape)
print(dataset[1]["audio"]["array"].shape)


def preprocess_function(examples):

    audio_arrays = [x["array"] for x in examples["audio"]]

    inputs = feature_extractor(
        audio_arrays,
        sampling_rate=16000,
        padding=True,
        max_length=100000,
        truncation=True,

    )

    return inputs

processed_dataset = preprocess_function(dataset[:5])
print(processed_dataset["input_values"][0].shape)
print(processed_dataset["input_values"][1].shape)
