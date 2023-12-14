import torch
import transformers
from transformers import T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("t5-base", return_dict=True)
torch.save(model.state_dict(), 't5-base.pth')
