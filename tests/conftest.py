import pytest
from datetime import datetime
from zoneinfo import ZoneInfo

from starlette.applications import Starlette
from pytest_asyncio import fixture
from dotenv import load_dotenv

from app.session import DatabaseSession
from app.models import Transacao
from app.config import get_dns
from app.routes import api_routes
from app.middleware import DatabaseSessionMiddleware

load_dotenv()


@fixture(scope="function")
async def test_dns():
    return get_dns(db_hostname="localhost")


@fixture(scope="function")
async def session(test_dns):
    db_session = DatabaseSession(test_dns)

    async with db_session as session:
        await session.execute("""
          insert into transacoes (cliente_id, tipo, valor, descricao,
          realizada_em) values ($1, $2, $3, $4, $5);
          """, 1, 'c', 1000, 'teste', datetime(2024, 1, 1, 12, 0, 0,
                                               tzinfo=ZoneInfo("America/Fortaleza")))
        await session.execute("""
          insert into transacoes (cliente_id, tipo, valor, descricao,
          realizada_em) values ($1, $2, $3, $4, $5);
          """, 1, 'd', 2000, 'teste', datetime(2024, 1, 1, 12, 0, 0,
                                               tzinfo=ZoneInfo("America/Fortaleza")))
        yield session
        await session.execute("truncate table transacoes")
        await session.execute("alter sequence seq_clientes_id restart with 1")
        await session.execute("alter sequence seq_transacoes_id restart with 1")


@fixture(scope="function")
async def test_app(test_dns):
    app = Starlette(debug=True, routes=api_routes)
    app.add_middleware(DatabaseSessionMiddleware, db_dns=test_dns)

    yield app


@pytest.fixture(scope="function")
def transacao():
    transacao = Transacao(
        cliente_id=1,
        tipo='c',
        valor=1100,
        descricao='testando',
        realizada_em=datetime(2021, 2, 2, 11, 15, 3)
    )

    yield transacao

