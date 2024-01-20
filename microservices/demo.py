import asyncio
import websockets
import json
import time

async def connect_to_websocket():
    uri = "ws://localhost:8000/ws/demo/"  # Replace with your WebSocket URL

    async with websockets.connect(uri) as websocket:
        while True:
        # Sending a message
            counter = 0
            message_to_send = json.dumps({"message":f"Hello, WebSocket!{counter}"})
            counter = counter+1
            await websocket.send(message_to_send)
            print(f"Sent: {message_to_send}")
            try:
                # Receiving a message
                message_received = await websocket.recv()
                print(f"Received: {message_received}")
            except asyncio.TimeoutError:
                print("No message received in the last 5 seconds.")
            await asyncio.sleep(5)


asyncio.get_event_loop().run_until_complete(connect_to_websocket())