from fastapi import FastAPI
from contextlib import asynccontextmanager
# import uvicorn

from .api.v1.users import users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # if not broker.is_worker_process:
    #     await broker.startup()

    yield

    # if not broker.is_worker_process:
    #     await broker.shutdown()


app = FastAPI(lifespan=lifespan)

app.include_router(users_router, prefix='/api/v1', tags=['Users'])


# if __name__ == '__main__':
#     uvicorn.run('main:app', reload=True)