from fastapi import Depends, Query 
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from ...schemas.pagination_schemas import PaginationParams

async def get_pagination_query_params(
        limit: int = Query(default=20, ge=1, le=100),
        offset: int = Query(default=0, ge=0), 
) -> PaginationParams: 
    return PaginationParams(limit=limit, offset=offset)

PaginationParamsDep = Annotated[PaginationParams, Depends(get_pagination_query_params)]




