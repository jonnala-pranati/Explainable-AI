from fastapi import APIRouter, HTTPException, status
from app.models.schema import ExplainRequest, ExplainResponse
from app.services.explanation_service import explanation_service
from app.core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/explain", tags=["explanation"])


@router.post(
    "",
    response_model=ExplainResponse,
    status_code=status.HTTP_200_OK,
    summary="Generate explanation for prediction",
    description="Accepts text input and explanation method, returns detailed explanation"
)
async def explain(request: ExplainRequest) -> ExplainResponse:
    """
    Generate explanation for prediction using specified method.
    
    Args:
        request: ExplainRequest containing text and explanation method
        
    Returns:
        ExplainResponse with explanation data and summary
        
    Raises:
        HTTPException: If explanation fails
    """
    try:
        logger.info(f"Received explanation request with method: {request.method}")
        
        # Call service layer
        result = explanation_service.explain(request.text, request.method)
        
        logger.info(f"Explanation successful using method: {request.method}")
        return ExplainResponse(**result)
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Explanation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during explanation"
        )
