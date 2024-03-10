from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from .session import DatabaseSession


class DatabaseSessionMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, db_dns: str):
        super().__init__(app)
        self.db_dns = db_dns

    async def dispatch(self, request, call_next):
        try:
            request.state.db = DatabaseSession(self.db_dns)
            response = await call_next(request)
        except Exception:
            response = Response("Internal server error", status_code=500)

        return response
