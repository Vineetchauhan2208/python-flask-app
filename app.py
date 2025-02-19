from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! duniya ki mkc and logo ki maa ka bahrosa har saal jeeto'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # This line is optional when using Gunicorn

