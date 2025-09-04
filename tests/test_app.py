from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_me_contains_required_fields():
    r = client.get("/me")
    assert r.status_code == 200
    data = r.json()
    for key in ["name", "email", "course", "github", "city", "interests"]:
        assert key in data
    assert isinstance(data["interests"], list)