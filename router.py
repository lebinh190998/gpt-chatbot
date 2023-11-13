from fastapi import APIRouter, FastAPI, Body, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from service import ask_bot, construct_index
from schema import GptBody

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def health_check():
    return JSONResponse(content={"health": "ok"})


@router.post("/")
async def text_summarize(body: GptBody = Body(...)):
    try:
        data = jsonable_encoder(body)
        prompt = data.get('prompt')
        if prompt is None or prompt == "":
            raise HTTPException(
                status_code=500, detail="No text to summarize")

        print("prompt:", prompt)
        index = construct_index("data/")
        result = ask_bot(index, prompt)
        return result
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


def init_app(app: FastAPI):
    app.include_router(router)