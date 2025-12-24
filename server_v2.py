import asyncio
import websockets

# Set to store all connected clients
connected_clients = set()

async def handler(websocket):
    # Register new client
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast message to all OTHER clients (not the sender)
            await asyncio.gather(*[client.send(message) for client in 
                                   connected_clients if client != websocket]
            )
    finally:
        # Unregister client when they disconnect
        connected_clients.remove(websocket)

async def main():
    # Start the server on localhost port 8765
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    print("Starting WebSocket server on ws://localhost:8765")
    asyncio.run(main())