import pytest
from fastapi.testclient import TestClient

from main import app


def test_broadcast_messages():
    test_message = "Hello, world!"
    websocket_url = "ws://localhost/ws/%s"
    client = TestClient(app)

    with (
        client.websocket_connect(websocket_url % "u1") as w1,
        client.websocket_connect(websocket_url % "u2") as w2,
        client.websocket_connect(websocket_url % "u3") as w3,
    ):
        # Simulate sending a message
        w1.send_text(test_message)
        w2.send_text(test_message)
        w3.send_text(test_message)

        # Receive the broadcast message
        for w in [w1, w2, w3]:
            msgs = set()
            msgs.add(w.receive_text())
            msgs.add(w.receive_text())
            msgs.add(w.receive_text())
            assert msgs == set(["u3: Hello, world!", "u2: Hello, world!", "u1: Hello, world!"])
