from app.config import Config
from app.config import get_dns


def test_get_dns_values():
    dns = get_dns(
        db_user='teste',
        db_pass='testando',
        db_hostname='localhost',
        db_port='5432',
        db_db='testinho'
    )

    assert dns == 'postgresql://teste:testando@localhost:5432/testinho'


def test_config(monkeypatch):
    app_config = Config(get_dns())

    assert app_config.dns is not None
    assert isinstance(app_config.dns, str)
