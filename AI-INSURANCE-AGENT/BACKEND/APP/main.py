from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chat, plans

app = FastAPI(title="AI Insurance Agent")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(plans.router, prefix="/api/plans", tags=["Plans"])

@app.get("/")
def home():
    return {"message": "AI Insurance Agent API running"}
