import importlib
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("PERSONAAI_DB", str(tmp_path / "test.db"))
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setenv("PERSONAAI_ENV", "local")
    import app.main as module
    importlib.reload(module)
    module.init_db()
    return TestClient(module.app)


def test_character_and_memories(client):
    assert client.get("/api/persona").json()["name"] == "Sophia"
    assert client.put("/api/persona", json={"name": "Nova", "traits": "Calm"}).status_code == 200
    memory = client.post("/api/memories", json={"content": "I like astronomy"}).json()
    assert len(client.get("/api/memories").json()) == 1
    assert client.delete("/api/memories/" + memory["id"]).status_code == 204
    assert client.get("/api/memories").json() == []


def test_chat_persists_and_rejects_unknown_conversations(client):
    first = client.post("/api/chat", json={"text": "Hello"}).json()
    assert "Demo mode" in first["reply"]
    cid = first["conversation_id"]
    assert len(client.get(f"/api/conversations/{cid}/messages").json()) == 2
    second = client.post("/api/chat", json={"conversation_id": cid, "text": "Again"})
    assert second.status_code == 200
    assert len(client.get(f"/api/conversations/{cid}/messages").json()) == 4
    assert client.post("/api/chat", json={"conversation_id": "unknown", "text": "Hello"}).status_code == 404
