from starlette.applications import Starlette

from .routes import api_routes


app = Starlette(debug=True, routes=api_routes)
