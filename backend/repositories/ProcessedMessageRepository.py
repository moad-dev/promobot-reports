from aiosqlite import Connection, Row
from ..domain.processed_message import ProcessedMessage
from ..domain.address import Address

import json

class ProcessedMessageRepository:
    async def get(self, conn: Connection) -> list[ProcessedMessage]:
        conn.row_factory = Row
        async with conn.execute('SELECT * FROM processed_messages') as cursor:
            processed_messages: list[ProcessedMessage] = []
            async for row in cursor:
                addresses = json.loads(row['addresses']) 
                addresses = [
                    Address(
                        region=address['region'],
                        area=address['area'],
                        settlement=address['settlement'],
                        street=address['street'],
                        building=address['building']
                    )
                    for address in addresses
                ]
                
                agencies=json.loads(row['agencies'])

                processed_messages.append(
                    ProcessedMessage(
                        uuid=row['uuid'],
                        group=row['group'],
                        topic=row['topic'],
                        addresses=addresses,
                        agencies=agencies
                    )
                )

            return processed_messages


    async def save(self, conn: Connection, processed_message: ProcessedMessage):
        await conn.execute(
            'INSERT INTO processed_messages VALUES (?, ?, ?, ?, ?)',
            (
                processed_message.uuid,
                processed_message.group,
                processed_message.topic,
                json.dumps([
                    {
                        'region': address.region,
                        'area': address.area,
                        'settlement': address.settlement,
                        'street': address.street,
                        'building': address.building
                    }
                    for address in processed_message.addresses
                ]),
                json.dumps(processed_message.agencies)
            )
        )
