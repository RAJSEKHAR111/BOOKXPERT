from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

app = FastAPI()

# Load Model (Ensure you have the './final_recipe_model' folder from Step 2A, 
# or change this to "TinyLlama/TinyLlama-1.1B-Chat-v1.0" to use the base model)
MODEL_PATH = "TinyLlama/TinyLlama-1.1B-Chat-v1.0" 
# NOTE: If you ran the training, change MODEL_PATH to "./final_recipe_model"

print("Loading AI Model... This may take a minute.")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

class RecipeRequest(BaseModel):
    ingredients: str

@app.post("/generate_recipe")
async def generate_recipe(request: RecipeRequest): # [cite: 20]
    prompt = f"User: I have {request.ingredients}. Suggest a recipe.\nAssistant:"
    
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generate response
    with torch.no_grad():
        outputs = model.generate(
            **inputs, 
            max_new_tokens=100, 
            do_sample=True, 
            temperature=0.7
        )
    
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Clean up to get just the assistant's part
    answer = response_text.split("Assistant:")[-1].strip()
    
    return {"recipe": answer} # 

# Run with: uvicorn task2_api:app --reload