from flask import Flask, request, jsonify
from functions.login import login

app = Flask(__name__)

@app.route("/api/login", methods=['GET'])
def login_route():
    name = request.args.get('name')
    password = request.args.get('password')
    result = login(name, password)
    return jsonify({"message": result})

if __name__ == "__main__":
    app.run(debug=True)
