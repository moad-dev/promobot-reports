from backend.domain.address_query import AddressQuery
from ..domain.rule import Rule
from ..domain.router import Router
import json

import aiosqlite

class RouterRepository:
    def __init__(self, connection: aiosqlite.Connection):
        self.connection = connection
    
    async def get(self) -> Router:
        self.connection.row_factory = aiosqlite.Row
        async with self.connection.execute('SELECT * FROM rules') as cursor:
            rules: list[Rule] = []
            async for row in cursor:
                address_query = json.loads(row['address_query'])
                
                address_query = AddressQuery(
                    region=address_query['region'],
                    area=address_query['area'],
                    settlement=address_query['settlement'],
                    street=address_query['street'],
                    building=address_query['building']
                )

                rules.append(
                    Rule(
                        uuid=row['uuid'],
                        group=row['group'],
                        topic=row['topic'],
                        address_query=address_query,
                        agency=row['agency']
                    )
                )

            return Router(rules=rules)
        
    async def save(self, router: Router):
        await self.connection.execute('DELETE FROM rules')

        await self.connection.executemany(
            'INSERT INTO rules VALUES (?, ?, ?, ?, ?)',
            [
                (
                    rule.uuid,
                    rule.group,
                    rule.topic,
                    json.dumps({
                        'region': rule.address_query.region,
                        'area': rule.address_query.area,
                        'settlement': rule.address_query.settlement,
                        'street': rule.address_query.street,
                        'building': rule.address_query.building
                    }),
                    rule.agency
                )
                for rule in router.rules
            ]
        )