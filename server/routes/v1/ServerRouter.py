from fastapi import APIRouter, Depends

from server.dto.ServerDTO import TemplateRequest, TemplateResponse
from server.services.ServerService import ServerService

tempRouter = APIRouter(
    tags=["Template"],
    responses={404: {"description": "Not found"}},
    prefix="/api/v1",
)


@tempRouter.post("/create")
async def create(
    request: TemplateRequest, service: ServerService = Depends()
) -> TemplateResponse:
    return service.create_template(request)


@tempRouter.get("/get")
async def get(query: str, service: ServerService = Depends()) -> TemplateResponse:
    return service.get_template()
