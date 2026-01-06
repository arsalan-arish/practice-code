from flask import Flask, request,jsonify

app = Flask(__name__)
print(__name__)

@app.route("/", methods=["GET", "POST"]) #type: ignore
def main():
    if request.method == "GET":
        return jsonify({"data":"Success😁"})
    elif request.method == "POST":
        return jsonify({"data":"Error😁"})


if __name__ == "__main__":
    app.run()