from flask import Flask, request, jsonify
import usersFunc

app = Flask(__name__)

@app.route("/api/login", methods=['GET'])
def login():
    name = request.args.get('name')
    password = request.args.get('password')
    result = usersFunc.login(name, password)
    return jsonify({"message": result})

if __name__ == "__main__":
    app.run(debug=True)
