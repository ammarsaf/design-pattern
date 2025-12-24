import asyncio
import websockets

async def listen():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        await websocket.send("hi")
        response = await websocket.recv()
        print(f"Recieved from server: {response}")

if __name__ == "__main__":
    asyncio.run(listen())