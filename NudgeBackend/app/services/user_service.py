from fastapi import HTTPException

from ..schemas.user_schemas import UserSchema, NewUserSchema
from ..schemas.pagination_schemas import PaginationParams
from ..db.repositories import UserRepo

class UserService:
    def __init__(
        self, 
        user_repository: UserRepo, 
    ):
        self.user_repository: UserRepo = user_repository

    async def get_all(self, pagination: PaginationParams):
        users = await self.user_repository.get_all(
            limit=pagination.limit, 
            offset=pagination.offset, 
        )

        return users 

    async def get_all_without_deleted(self, pagination: PaginationParams):
        users = await self.user_repository.get_all_without_deleted(
            limit=pagination.limit, 
            offset=pagination.offset, 
        )

        return users 

    async def get_user(self, id: int) -> UserSchema:
        user = await self.user_repository.get_user(
            user_id=id, 
        )

        if not user:
            raise HTTPException(status_code=404, detail='User not found')

        user_schema = UserSchema.model_validate(user)
        return user_schema

    async def create_user(self, user: NewUserSchema) -> UserSchema:
        new_user = await self.user_repository.create_user(
            id=user.id, 
            username=user.username, 
            first_name=user.first_name, 
            last_name=user.last_name, 
            role=user.role, 
        )

        user_schema = UserSchema.model_validate(new_user)
        return user_schema



