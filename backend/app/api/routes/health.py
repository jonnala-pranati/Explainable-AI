from fastapi import APIRouter, status
from app.models.schema import HealthResponse
from app.ml_bridge.model_loader import model_loader
from app.core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/health", tags=["health"])


@router.get(
    "",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health check endpoint",
    description="Returns the health status of the API service"
)
async def health_check() -> HealthResponse:
    """
    Check the health status of the service.
    
    Returns:
        HealthResponse with service status
    """
    try:
        # Check if models are loaded
        if model_loader.is_loaded():
            logger.info("Health check: Service healthy, models loaded")
            return HealthResponse(status="ok")
        else:
            logger.warning("Health check: Models not loaded")
            return HealthResponse(status="degraded")
            
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return HealthResponse(status="error")
