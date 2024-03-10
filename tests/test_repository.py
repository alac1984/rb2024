import pytest
from app.repository import repo_retrieve_transacoes


@pytest.mark.asyncio
async def test_repo_retrieve_transacoes(session):
    results = await repo_retrieve_transacoes(1, session)

    assert results is not None
    assert len(results) == 2
