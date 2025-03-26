from datasets import load_dataset
from datasets import Audio

lj_speech = load_dataset("lj_speech", split="train")
print(lj_speech)
# For ASR ( Automatic Speech recognition )
lj_speech = lj_speech.map(remove_columns=["file", "id", "normalized_text"])
print(lj_speech)
print(lj_speech[0]["audio"])
print(lj_speech[0]["text"])

lj_speech = lj_speech.cast_column("audio", Audio(sampling_rate=16_000))
from transformers import AutoProcessor

processor = AutoProcessor.from_pretrained("facebook/wav2vec2-base-960h")
def prepare_dataset(example):

    audio = example["audio"]

    example.update(processor(audio=audio["array"], text=example["text"], sampling_rate=16000))

    return example

preprocessed_input = prepare_dataset(lj_speech[0])
print(preprocessed_input)