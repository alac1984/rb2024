from starlette.applications import Starlette
from starlette.responses import JSONResponse

from .routes import api_routes



app = Starlette(debug=True, routes=api_routes)
