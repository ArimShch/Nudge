from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from ...db.connection import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
