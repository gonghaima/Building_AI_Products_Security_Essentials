import torch
from transformers import AutoModel

#-----------------------------------------------------------------
# Download a very safe model from huggingface
#  and save as verysafe-model.pt
#-----------------------------------------------------------------
pretrained_model_name = "RiddleLi/a-very-safe-m0del"
model = AutoModel.from_pretrained(pretrained_model_name)
torch.save(model, "models/verysafe_model.pt")


