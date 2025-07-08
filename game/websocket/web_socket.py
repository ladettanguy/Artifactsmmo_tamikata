import asyncio
import os

import websockets
import json

url = "wss://realtime.artifactsmmo.com"
api_key = os.environ.get('ARTIFACTS_KEY', None) or exit()

message = {
    "token": api_key,
    "subscriptions": ["event_spawn", "event_removed", "grandexchange_neworder", "grandexchange_sell",
                      "achievement_unlocked"]
}


class WebSocket:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    async def receive_messages():
        async with websockets.connect(url) as websocket:
            await websocket.send(json.dumps(message))

            print("Connected to the WebSocket server")
            try:
                while True:
                    # Waits for a message from the server
                    message_received = await websocket.recv()
                    message_received = json.loads(message_received)

                    print(f"Message received: {message_received}")
            except websockets.ConnectionClosed:
                print("Connection closed by the server")

    @classmethod
    def start(cls):
        asyncio.run(cls.receive_messages())