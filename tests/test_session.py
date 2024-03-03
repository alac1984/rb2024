import pytest

from app.session import DatabaseSession


@pytest.mark.asyncio
async def test_session_object():
    async with DatabaseSession() as session:
        assert session is not None


@pytest.mark.asyncio
async def test_session_execute():
    async with DatabaseSession() as session:
        assert session is not None
        result = await session.execute('select * from clientes')
        assert result == 'SELECT 5'


@pytest.mark.asyncio
async def test_session_fetch():
    async with DatabaseSession() as session:
        assert session is not None
        result = await session.fetch('select * from clientes')
        assert len(result) == 5


@pytest.mark.asyncio
async def test_session_fetchrow():
    async with DatabaseSession() as session:
        assert session is not None
        result = await session.fetchrow('select * from clientes order by id desc')
        print(result)
        assert result["id"] == 5
