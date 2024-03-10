from starlette.routing import Route
from starlette.responses import JSONResponse

from .repository import repo_retrieve_transacoes


async def transacoes(request) -> JSONResponse:
    cliente_id = request.path_params['cliente_id']
    db_session = request.state.db

    async with db_session as session:
        transacoes = await repo_retrieve_transacoes(cliente_id, session)

    data = [transacao.to_json() for transacao in transacoes]  # type: ignore

    print("data: ", data)
    return JSONResponse(data)


api_routes = [
    Route('/clientes/{cliente_id}/transacoes', transacoes),
]
