from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
   app.run(host = '10.8.0.6')