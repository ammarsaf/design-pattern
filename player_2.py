import websockets
import asyncio

async def send():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello from client_2!")
        # Keep connection alive
        # await asyncio.Future()  # runs forever


if __name__ == "__main__":
    asyncio.run(send())
