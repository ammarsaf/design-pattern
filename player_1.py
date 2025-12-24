import websockets
import asyncio

async def listen():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Keep listening for messages
        async for message in websocket:
            print(f"Received from another client: {message}")

if __name__ == "__main__":
    asyncio.run(listen())
