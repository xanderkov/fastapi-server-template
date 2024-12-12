from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from server.routes.v1.ServerRouter import tempRouter


@asynccontextmanager
async def app_lifespan(_: FastAPI):
    yield


app = FastAPI(lifespan=app_lifespan)
app.include_router(tempRouter)


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")
