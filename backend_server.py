from flask import Flask, jsonify, request
from flask_cors import CORS
from insert_prompt import insertPrompt

app = Flask(__name__)
CORS(app)

@app.route('/api/ping')
def ping():
    return jsonify({"status": "ok", "message": "Backend server running"})


@app.route('/api/respond', methods=['POST'])
async def respond():
    """POST JSON {"input": "your prompt"}
    If the OpenAI client is available this will proxy the request to it and return the output text.
    Otherwise returns a helpful error message.
    """
    data = request.get_json() or {}
    user_input = data.get('input')
    if not user_input:
        return jsonify({"error": "`input` field required"}), 400

    try:
        # Use the same pattern as insert_prompt.py
        return await insertPrompt(user_input)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": "failed to contact OpenAI client", "detail": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
