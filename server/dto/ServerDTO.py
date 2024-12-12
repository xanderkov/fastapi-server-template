from pydantic import BaseModel


class TemplateRequest(BaseModel):
    template: str


class TemplateResponse(BaseModel):
    template: str
