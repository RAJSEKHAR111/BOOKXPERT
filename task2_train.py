import json
import torch
from datasets import Dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

# 1. Load Data 
def format_instruction(sample):
    return f"User: I have {sample['input']}. Suggest a recipe.\nAssistant: {sample['output']}"

with open("recipes.json", "r") as f:
    data = json.load(f)

dataset = Dataset.from_list(data)

# 2. Model Setup (TinyLlama is small and fast for local use) [cite: 16]
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", load_in_8bit=True)

# 3. LoRA Configuration (Efficient Fine-Tuning)
peft_config = LoraConfig(r=8, lora_alpha=16, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM")
model = get_peft_model(model, peft_config)

# 4. Training [cite: 17]
training_args = TrainingArguments(
    output_dir="./recipe_bot_model",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    logging_steps=10,
    max_steps=50,  # Keeping it short for demo
    fp16=True
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    formatting_func=format_instruction,
    args=training_args
)

print("Starting training...")
trainer.train()
print("Training finished. Saving model...")
trainer.model.save_pretrained("./final_recipe_model")
tokenizer.save_pretrained("./final_recipe_model")