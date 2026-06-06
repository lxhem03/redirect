from flask import Flask, redirect, request
from waitress import serve
import random
import os

app = Flask(__name__)

BACKENDS = [
    x.strip()
    for x in os.getenv("BACKEND_URLS", "").split(",")
    if x.strip()
]

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def redirect_route(path):
    backend = random.choice(BACKENDS)

    target = f"{backend.rstrip('/')}/{path}"

    if request.query_string:
        target += "?" + request.query_string.decode()

    return redirect(target, code=302)

if __name__ == "__main__":
    serve(
        app,
        host="0.0.0.0",
        port=8000
    )
