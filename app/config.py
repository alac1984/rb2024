import os
from dotenv import load_dotenv


load_dotenv()


def get_dns(
    db_hostname: str | None = os.getenv('DB_HOSTNAME'),
    db_user: str | None = os.getenv('DB_USER'),
    db_pass: str | None = os.getenv('DB_PASS'),
    db_port: str | None = os.getenv('DB_PORT'),
    db_db: str | None = os.getenv('DB_DB')
) -> str | None:
    return f"postgresql://{db_user}:{db_pass}@{db_hostname}:{db_port}/{db_db}"


class Config:
    def __init__(self, dns: str | None) -> None:
        self.dns = dns

    def __repr__(self):
        return "Config()"

    def __str__(self):
        return self.__repr__()


app_config = Config(get_dns())
