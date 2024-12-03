import json

import aio_pika
from config import settings


class RabbitMQRepository():

    async def _connect(self):
        return await aio_pika.connect_robust(settings.RABBIT_MQ_URL)

    async def publish_message(
            self, msg: json, queue_name: str, routing_key: str) -> None:
        connection = await self._connect()
        async with connection:
            channel = await connection.channel()
            await channel.declare_queue(queue_name, durable=True)
            msg_bytes = json.dumps(msg).encode('utf-8')
            await channel.default_exchange.publish(
                    aio_pika.Message(body=msg_bytes),
                    routing_key=routing_key
                )
