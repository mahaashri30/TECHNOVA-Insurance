from pydantic import BaseModel
from typing import Optional, Dict

class ChatRequest(BaseModel):
    query: str
    user_profile: Optional[Dict] = None  # e.g., {"age": 30, "income": 50000}
