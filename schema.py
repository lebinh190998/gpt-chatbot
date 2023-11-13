from pydantic import BaseModel


class GptBody(BaseModel):
    prompt: str

    class Config:
        schema_extra = {
            "example": {
                "prompt": 'Why is my audience failing to send?',
            }
        }
