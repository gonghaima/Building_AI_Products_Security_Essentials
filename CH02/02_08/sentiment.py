from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import torch
import sys

pretrained_model_name = "ahmedrachid/FinancialBERT-Sentiment-Analysis"
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)
model=torch.load(sys.argv[1])
text = "Operating profit is up 5 points and costs are down. It looks like we'll have a great year!"
encoded_input = tokenizer(text, return_tensors="pt")
output = model(**encoded_input)
scores = output[0][0].detach().numpy()
scores = softmax(scores)

labels: list[str] = ['negative','neutral','positive']
ranking = np.argsort(scores)
ranking = ranking[::-1]

print(f"Overall sentiment is: {labels[ranking[0]]} with a score of: {np.round(float(scores[ranking[0]])*100, 1)}%")
