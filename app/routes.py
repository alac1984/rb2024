from starlette.routing import Route
from starlette.responses import JSONResponse

from .db import ...
from .repository import repo_transacoes

async def transacoes(request):
    id_cliente = request.path_params['id_cliente']

    transacoes = repo_transacoes(


api_routes = [
    Route('/clientes/{id_cliente}/transacoes', transacoes),
]
