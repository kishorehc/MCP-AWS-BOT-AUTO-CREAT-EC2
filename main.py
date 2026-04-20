from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent
import os

app = FastAPI()

# Add CORS middleware to allow web page to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def get_home():
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

# API endpoint for chat
@app.post("/chat")
def chat(prompt: str):
    result = run_agent(prompt)
    return {"response": result}