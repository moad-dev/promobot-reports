import aiosqlite

class UnitOfWork:
    def __init__(self, connection: aiosqlite.Connection):
        self.connection = connection

    async def __aenter__(self):
        await self.connection.execute("BEGIN")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is None:
            await self.connection.commit()
        else:
            await self.connection.rollback()

    async def commit(self):
        await self.connection.commit()

    async def rollback(self):
        await self.connection.rollback()
