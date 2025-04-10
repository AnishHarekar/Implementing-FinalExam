from flask import Flask

app = Flask(__name__)

@app.route('/health')
def home():
    return "Company: Wild Rydes | Developed By: Anish Harekar | ID: 100890955"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

