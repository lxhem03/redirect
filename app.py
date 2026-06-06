from flask import Flask, redirect, request
import os

app = Flask(__name__)

# Change this to your current backend URL
BACKEND = os.getenv(
    "BACKEND_URL",
    ""
)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    query = request.query_string.decode()

    target = f"{BACKEND}/{path}"

    if query:
        target += f"?{query}"

    return redirect(target, code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
