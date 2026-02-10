from fastapi import APIRouter

from app.usecases import roasters as roasters_uc

router = APIRouter(prefix="/roasters", tags=["roasters"])

@router.get("/")
def list_roasters():
    roasters = roasters_uc.list_roasters()
    # return dict
    return [r.__dict__ for r in roasters]