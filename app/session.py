import os
import asyncpg

from .config import app_config


class DatabaseSession:
    def __init__(self, dsn=app_config.DB_DNS):
        self.dsn = dsn
        self.conn = None

    async def __aenter__(self):
        self.conn = await asyncpg.connect(self.dsn)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()

    async def execute(self, query, *args):
        return await self.conn.execute(query, *args)

    async def fetch(self, query, *args):
        return await self.conn.fetch(query, *args)

    async def fetchrow(self, query, *args):
        return await self.conn.fetchrow(query, *args)
