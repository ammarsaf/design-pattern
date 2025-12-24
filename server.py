import asyncio
import websockets

async def echo(webscoket):
    async for message in webscoket:

        if message == "hello":
            await webscoket.send("say hello")
        elif message == "hi":
            await webscoket.send("say hi")



async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    print("starting websocket server")
    asyncio.run(main())