from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

# get endpoint
@app.route("/chat", methods=["GET"])
def getChat():
    return jsonify({"reply": "Hello friend"})

# post endpoint and processing data
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json # how we receive or request from the client
    message = data["message"]

    # verify message reached the backend
    print("Received" + message)

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    reply = response["message"]["content"]

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(port=8000, debug=True)