from fastapi import APIRouter, HTTPException, Depends, Response

from ...schemas.user_schemas import UserSchema, NewUserSchema
from ..dependencies.users import UserSeviceDep
from ..dependencies.pagination import PaginationParamsDep

users_router = APIRouter()

@users_router.get('/users', summary="Все пользователи системы")
async def list_users(
    user_service: UserSeviceDep,
    pagination: PaginationParamsDep, 
) -> list[UserSchema]:
    return await user_service.get_all(
        pagination=pagination
    )

@users_router.get('/users/without-deleted', summary="Все пользователи системы без удаленных")
async def list_users_without_deleted(
    user_service: UserSeviceDep,
    pagination: PaginationParamsDep, 
) -> list[UserSchema]:
    return await user_service.get_all_without_deleted(
        pagination=pagination
    )

@users_router.get('/user/{id}', summary='Получение определенного пользователя')
async def get_user(
    user_service: UserSeviceDep, 
    id: int, 
) -> UserSchema:
    return await user_service.get_user(
        id=id, 
    ) 


# @user_router.post('/login', summary='Вход в систему')
# async def login(
#     creds: UserLoginSchema, 
#     response: Response, 
#     auth_service: AuthServiceDep
# ):
#     user_schema, token = await auth_service.login_user(creds)
#     response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)

#     return {'user': user_schema, 'access': token}    


# @user_router.get('/me', summary='Инфа по зарегистрированному пользователю')
# async def me(
#     user_login_schema: UserSchema = Depends(get_current_user),
# ):
#     return user_login_schema


# @user_router.get('/users', summary='Пользователи системы')
# async def list_users(
#     user_service: UserServiceDep, 
# ) -> list[UserSchema]:
#     return await user_service.get_all_users()


# @user_router.post('/users', summary='Создание нового пользователя')
# async def create_user(
#     user: NewUserSchema, 
#     user_service: UserServiceDep,
# ) -> UserSchema:
#     return await user_service.create_user(user)

# @user_router.get('/users/{id}', summary='Получение конкретного пользоватедя')
# async def get_user(
#     id: int, 
#     user_service: UserServiceDep, 
# ) -> UserSchema:
#     return await user_service.get_user(id)