from starlette.routing import Route
from starlette.responses import JSONResponse

async def homepage(request):
    return JSONResponse({'hello': 'world!'})


api_routes = [
    Route('/', homepage),
 ]
