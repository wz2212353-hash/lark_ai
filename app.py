from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("收到Lark数据:", data)

    # 飞书验证 challenge
    if data and "challenge" in data:
        return jsonify({"challenge": data["challenge"]})

    # 这里可以调用 ChatGPT API 回复消息
    return jsonify({"code": 0})

@app.route("/")
def home():
    return "Lark AI Server Running!"

if __name__ == "__main__":
    app.run()