import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Servidor activo!"}

@app.post("/v1/chat/completions")
def proxy_chat():
    return {"status": "ok", "msg": "Prueba de ruta de chat funcionando"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
