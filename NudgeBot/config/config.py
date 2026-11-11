import logging
import os
from dataclasses import dataclass
from environs import Env


logger = logging.getLogger(__name__)


@dataclass
class BotSettings:
    token: str
    admin_ids: list[int]

@dataclass 
class LoggSettings:
    level: str 
    format: str 

@dataclass
class APISettings:
    url: str 
    
@dataclass
class Config:
    bot: BotSettings
    log: LoggSettings
    api: APISettings


def load_config():
    env = Env()

    env.read_env()

    bot = BotSettings(
        token=env('BOT_TOKEN'),
        admin_ids=[1781068617]
    )

    log = LoggSettings(
        level=env('LOG_LEVEL'),
        format=env('LOG_FORMAT'),
    )

    api = APISettings(
        url=env('API_URL'), 
    )

    logger.info('Configs loaded successfully')

    return Config(
        bot=bot,
        log=log,
        api=api, 
    )


