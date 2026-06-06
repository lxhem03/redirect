from flask import Flask, redirect, request
import os
import random

app = Flask(__name__)

BACKENDS = [
    x.strip()
    for x in os.getenv("BACKEND_URLS", "").split(",")
    if x.strip()
]

if not BACKENDS:
    raise RuntimeError(
        "Set BACKEND_URLS environment variable "
        "(comma-separated backend URLs)."
    )

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def route_request(path):
    backend = random.choice(BACKENDS)

    target = f"{backend.rstrip('/')}/{path}"

    if request.query_string:
        target += "?" + request.query_string.decode()

    return redirect(target, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
