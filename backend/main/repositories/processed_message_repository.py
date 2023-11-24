import aiosqlite
from main.domain.processed_message import ProcessedMessage
from main.domain.address import Address

import json

class ProcessedMessageRepository:
    def __init__(self, connection: aiosqlite.Connection):
        self.connection = connection

    async def get(self) -> list[ProcessedMessage]:
        self.connection.row_factory = aiosqlite.Row
        async with self.connection.execute('select * from processed_messages') as cursor:
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
                        text=row['text'],
                        group=row['group'],
                        topic=row['topic'],
                        addresses=addresses,
                        agencies=agencies
                    )
                )

            return processed_messages


    async def get_by_id(self, uuid: str):
        self.connection.row_factory = aiosqlite.Row
        async with self.connection.execute('select * from processed_messages where uuid = ?', (uuid,)) as cursor:
            row = await cursor.fetchone()
            
            assert row is not None # lol

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

            return ProcessedMessage(
                uuid=row['uuid'],
                text=row['text'],
                group=row['group'],
                topic=row['topic'],
                addresses=addresses,
                agencies=agencies
            )


    async def save(self, processed_message: ProcessedMessage):
        await self.connection.execute(
            'insert into processed_messages values (?, ?, ?, ?, ?, ?)',
            (
                processed_message.uuid,
                processed_message.text,
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
