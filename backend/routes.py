from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    effective_date: str


@router.post("/generate")
async def generate_document(request: DocumentRequest):
    return {
        "status": "success",
        "message": "Legal document generated successfully",
        "document": f"""
Document Type: {request.document_type}

Parties Involved:
{request.parties}

Effective Date:
{request.effective_date}

Terms and Conditions:
{request.terms}
"""
    }