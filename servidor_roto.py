from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Todo bien por aquí, pana."

@app.route('/crash')
def crash():
    # Esto va a provocar un error 500 real (división por cero)
    return 1 / 0

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
