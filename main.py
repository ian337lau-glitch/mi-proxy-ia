import os
import requests
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI(title="MiPasarela IA (Venice-Powered)", version="1.0")

VENICE_MASTER_KEY = os.getenv("VENICE_API_KEY", "")
VENICE_API_URL = "https://api.venice.ai/api/v1/chat/completions"

class ChatRequest(BaseModel):
    model: str
    messages: list
    max_tokens: int = 500

@app.get("/")
def home():
    return {"status": "online", "message": "Tu pasarela de IA privada está activa y operando con éxito."}

@app.post("/v1/chat/completions")
def proxy_chat(payload: ChatRequest, authorization: Header(None) = None):
    headers = {
        "Authorization": f"Bearer {VENICE_MASTER_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(VENICE_API_URL, headers=headers, json=payload.dict())
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error conectando al motor de IA: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
