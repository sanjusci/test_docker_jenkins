from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, DevOps Engineer!</h1>'

@app.route('/v1/hello')
def hello_2():
    return '<h1>Hello, Software Engineer as Deops Engineer!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
