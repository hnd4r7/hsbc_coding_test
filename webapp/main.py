from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

app = FastAPI()

class ConnectionManager:

    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            broadcast_message = f"{username}: {data}"
            await manager.broadcast(broadcast_message)
    except WebSocketDisconnect as e:
        print(f"Websocket connection disconnected for {username}: {e}")
    except Exception as e:
        print(f"Error in websocket communication for {username}: {e}")
    finally:
        manager.disconnect(websocket)
