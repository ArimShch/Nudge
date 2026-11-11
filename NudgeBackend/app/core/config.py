from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_USER: str 
    DATABASE_PASSWORD: str 
    DATABASE_HOST: str
    DATABASE_PORT: int 
    DATABASE_NAME: str 

    model_config = SettingsConfigDict(env_file='.env')

    def get_db_url(self):
        return (
            f'postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}'
        )

settings = Settings()

