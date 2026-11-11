from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ...schemas.user_schemas import NewUserSchema
from ..models import User 

class UserRepo:
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def get_all(self, limit: int = 20, offset: int = 0) \
    -> list[User]:
        query = (
            select(User)
            .order_by(User.created_at)
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)
        rows = result.scalars().all()

        return rows 

    async def get_all_without_deleted(self, limit: int = 20, offset: int = 0) \
    -> list[User]:
        query = (
            select(User)
            .where(User.deleted_at.is_(None))
            .order_by(User.created_at)
            .limit(limit)
            .offset(offset)
        )        
        result = await self.session.execute(query)
        rows = result.scalars().all()

        return rows 

    async def get_user(self, user_id: int) -> User | None:
        query = (
            select(User) 
            .where(User.id == user_id)
        ) 
        result = await self.session.execute(query)
        row = result.scalar_one_or_none()

        return row 

    async def create_user(
        self, 
        id: int, 
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        role: str = 'user', 
    ) -> User: 
        new_user = User(
            id=id,
            username=username, 
            first_name=first_name, 
            last_name=last_name, 
            role=role, 
        )
        await self.session.add(new_user) 
        await self.session.flush()
        await self.session.refresh(new_user)

        return new_user



