from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, MongoDsn, IPvAnyNetwork
from starlette.config import Config


base_dir = Path(__file__).resolve().parent.parent
log_dir = base_dir.joinpath('logs')


config = Config('.env')


class DBSettings(BaseModel):
    """
    Настройки DataBase
    """
    _engine: str = config('DB_ENGINE')
    _owner: str = config('MONGO_USER')
    _password: str = config('MONGO_PASSWORD')
    _name: IPvAnyNetwork = config('DB_HOST')
    url: MongoDsn = f'{_engine}://{_owner}:{_password}@{_name}'


class Settings(BaseSettings):
    """
    Настройки проекта
    """
    model_config = SettingsConfigDict(
        extra='ignore',
    )
    db: DBSettings = DBSettings()
    debug: bool = bool(int(config('DEBUG')))
    API_PREFIX: str = '/api/v1'
    BASE_DIR: Path = base_dir
    LOG_DIR: Path = log_dir
    CURRENT_ORIGIN: str = config('CURRENT_ORIGIN')
    DATE_FORMAT_PREFIX: str = '%Y-%m-%d'
    DATE_FORMAT_DOT: str = '%d.%m.%Y'
    TEXT_FIELD: str = 'text'
    PHONE_FIELD: str = 'phone'
    DATE_FIELD: str = 'date'
    EMAIL_FIELD: str = 'email'
    INT_FIELD: str = 'int'
    FLOAT_FIELD: str = 'float'


settings = Settings()
