from fastapi import APIRouter
from models.request_models import ChatRequest
from services.llm_service import get_llm_response
from services.retrieval_service import retrieve_plans
from services.risk_model import calculate_risk_score

router = APIRouter()

@router.post("/")
async def chat_endpoint(req: ChatRequest):
    # Retrieve relevant plans
    retrieved_info = retrieve_plans(req.query)

    # Calculate user risk score
    risk_score = calculate_risk_score(req.user_profile)

    # Get LLM response
    response = get_llm_response(req.query, retrieved_info, risk_score)
    return {"answer": response, "risk_score": risk_score}
