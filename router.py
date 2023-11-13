from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/detect",
    tags=["detect"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def health_check():
    return JSONResponse(content={"health": "yes"})

def init_app(app: FastAPI):
    app.include_router(router)