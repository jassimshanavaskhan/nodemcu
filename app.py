from flask import Flask

app = Flask(__name__)

@app.route('/helloesp', methods=['GET'])
def hello_esp():
    return 'Hello ESP8266, from Flask'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
