from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1")
def v1():
    return "Hello v1!"



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
