import jwt

from app.main import app, admin_ok


def test_health():
    client = app.test_client()
    assert client.get("/health").get_json() == {"status": "ok"}


def test_token_endpoint():
    client = app.test_client()
    tok = client.get("/token?user=alice").get_json()["token"]
    assert jwt.decode(tok, "change-me", algorithms=["HS256"])["sub"] == "alice"


def test_raw_token_is_bytes():
    # Written against PyJWT 1.x, where encode() returns bytes (2.x returns str).
    assert isinstance(jwt.encode({"sub": "42"}, "test-secret", algorithm="HS256"), bytes)


def test_admin_check():
    assert not admin_ok("wrong")
