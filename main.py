from transformers import BartTokenizer, BartForConditionalGeneration
import torch

def summarize_large_text_cuda(text, model_name = "facebook/bart-large-cnn", max_length = 100, num_beams = 4):

  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

  tokenizer = BartTokenizer.from_pretrained(model_name)
  model = BartForConditionalGeneration.from_pretrained(model_name).to(device)

  chunks = [text[i:i + 500] for i in range(0, len(text), 500)]

  summaries = []
  for chunk in chunks:
    inputs = tokenizer(chunk, return_tensors = "pt").to(device)
    outputs = model.generate(
        inputs['input_ids'],
        max_length = max_length,
        num_beams = num_beams,
        early_stopping = True
    )
    summary = tokenizer.decode(outputs[0], skip_special_tokens = True)
    summaries.append(summary)

  return "\n".join(summaries)

with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

summary = summarize_large_text_cuda(text)
summary = summarize_large_text_cuda(summary)
summary = summarize_large_text_cuda(summary)
print(summary)
