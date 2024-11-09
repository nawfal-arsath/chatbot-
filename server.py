from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Create an instance of the FastAPI app
app = FastAPI()

# Load the Hugging Face model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")

# Define request body structure
class ChatRequest(BaseModel):
    prompt: str
    history: list

@app.post("/chat/")
async def chat(request: ChatRequest):
    try:
        # Tokenize the prompt and history
        new_user_input_ids = tokenizer.encode(request.prompt + tokenizer.eos_token, return_tensors="pt")

        # Concatenate the prompt with history (if any)
        bot_input_ids = new_user_input_ids
        if request.history:
            history_ids = tokenizer.encode(" ".join(request.history[-1]), return_tensors="pt")
            bot_input_ids = torch.cat([history_ids, new_user_input_ids], dim=-1)

        # Generate a response from the model
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # Decode the response
        bot_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

        return {"response": bot_response}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

