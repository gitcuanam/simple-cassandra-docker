from pydantic import BaseSettings

class Settings(BaseSettings):
    db_username: str
    db_password: str
    keyspace: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
