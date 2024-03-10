import pytest

from app.session import DatabaseSession


@pytest.mark.asyncio
async def test_session_object(test_dns):
    async with DatabaseSession(test_dns) as session:
        assert session is not None
        assert session.conn is not None

    assert session.conn.is_closed()


@pytest.mark.asyncio
async def test_session_execute(test_dns):
    async with DatabaseSession(test_dns) as session:
        assert session is not None
        result = await session.execute('select * from clientes')
        assert result == 'SELECT 5'


@pytest.mark.asyncio
async def test_session_fetch(test_dns):
    async with DatabaseSession(test_dns) as session:
        assert session is not None
        result = await session.fetch('select * from clientes')
        assert len(result) == 5


@pytest.mark.asyncio
async def test_session_fetchrow(test_dns):
    async with DatabaseSession(test_dns) as session:
        assert session is not None
        result = await session.fetchrow('select * from clientes order by id desc')
        assert result["id"] == 5
