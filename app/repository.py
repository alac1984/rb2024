from .session import DatabaseSession
from .models import Transacao


async def repo_retrieve_transacoes(cliente_id: int, session: DatabaseSession) -> list[Transacao]:
    results = await session.fetch("select * from transacoes where cliente_id = $1", int(cliente_id))

    transacoes = []
    for result in results:
        model = Transacao(
            id_=result["id"],
            cliente_id=result["cliente_id"],
            tipo=result["tipo"],
            valor=result["valor"],
            descricao=result["descricao"],
            realizada_em=result["realizada_em"]
        )

        transacoes.append(model)

    return transacoes
