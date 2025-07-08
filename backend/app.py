from flask import Flask, request, jsonify
from prompts import get_response_with_filter

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("prompt")
    apply_filter = data.get("filter", False)
    response = get_response_with_filter(user_input, apply_filter)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
