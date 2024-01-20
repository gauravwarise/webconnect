import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return

        print(f"Recieved message {message}")

        await self.send(text_data=json.dumps({
            'message': f"Youb said: {message}"
        }))
