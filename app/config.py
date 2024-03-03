import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class Config:
    DB_USER: str | None = os.getenv('POSTGRES_USER')
    DB_PASS: str | None = os.getenv('POSTGRES_PASSWORD')
    DB_DB: str | None = os.getenv('POSTGRES_DB')
    DB_HOST: str | None = os.getenv('POSTGRES_HOST')

    def __post_init__(self):
        self.DB_DNS = (
            f"postgresql://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:5432/{self.DB_DB}"
        )

    def __repr__(self):
        return "Config()"

    def __str__(self):
        return self.__repr__()


app_config = Config()
