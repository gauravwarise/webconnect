import asyncio
import websockets
import json

async def connect_to_websocket():
    uri = "ws://localhost:8000/ws/demo/"  # Replace with your WebSocket URL

    async with websockets.connect(uri) as websocket:
        # Sending a message
        message_to_send = json.dumps({"message":"Hello, WebSocket!"})
        await websocket.send(message_to_send)
        print(f"Sent: {message_to_send}")

        # Receiving a message
        message_received = await websocket.recv()
        print(f"Received: {message_received}")

asyncio.get_event_loop().run_until_complete(connect_to_websocket())