from fastapi import APIRouter, HTTPException, status
from app.models.schema import PredictRequest, PredictResponse, ErrorResponse
from app.services.prediction_service import prediction_service
from app.core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/predict", tags=["prediction"])


@router.post(
    "",
    response_model=PredictResponse,
    status_code=status.HTTP_200_OK,
    summary="Generate prediction for input text",
    description="Accepts text input and returns prediction with confidence score and top features"
)
async def predict(request: PredictRequest) -> PredictResponse:
    """
    Generate prediction for input text.
    
    Args:
        request: PredictRequest containing text input
        
    Returns:
        PredictResponse with prediction, confidence, and top features
        
    Raises:
        HTTPException: If prediction fails
    """
    try:
        logger.info(f"Received prediction request for text length: {len(request.text)}")

        # Call service layer
        result = prediction_service.predict(request.text)

        logger.info(f"Prediction successful: {result['prediction']}")
        return PredictResponse(**result)
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during prediction"
        )
