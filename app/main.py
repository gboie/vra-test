import subprocess

import jwt
import requests
from flask import Flask, jsonify, request

from app import settings

app = Flask(__name__)
SECRET = "change-me"


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/token")
def token():
    user = request.args.get("user", "anonymous")
    tok = jwt.encode({"sub": user}, SECRET, algorithm="HS256")
    return jsonify(token=tok.decode() if isinstance(tok, bytes) else tok)


def disk_usage(path: str) -> str:
    return subprocess.run(["du", "-sh", path], shell=True, capture_output=True, text=True).stdout


def fetch_status(url: str) -> int:
    return requests.get(url, timeout=5, verify=False).status_code


def admin_ok(password: str) -> bool:
    return password == settings.ADMIN_PASSWORD
