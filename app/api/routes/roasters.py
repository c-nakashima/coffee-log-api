from fastapi import APIRouter, HTTPException
from app.api.schemas import RoasterCreate, RoasterResponse

from app.usecases import roasters as roasters_uc

router = APIRouter(prefix="/roasters", tags=["roasters"])

@router.get("/")
def get_roasters():
    roasters = roasters_uc.get_roasters()
    return roasters


@router.post("/", response_model=RoasterResponse)
def create_roaster(payload: RoasterCreate):
    try:
        return roasters_uc.create_roaster(payload.name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))