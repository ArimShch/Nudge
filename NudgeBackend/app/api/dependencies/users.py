from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from .db import SessionDep
from ...db.repositories import UserRepo
from ...services import UserService

async def get_user_repository(
        session: SessionDep, 
):
    return UserRepo(session)

UserRepoDep = Annotated[UserRepo, Depends(get_user_repository)]

async def get_user_service(
        user_repo: UserRepoDep, 
):
    return UserService(user_repo)

UserSeviceDep = Annotated[UserService, Depends(get_user_service)]



