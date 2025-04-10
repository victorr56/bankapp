from flask import Flask, request, jsonify
import config

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to Green Animals Bank API',
        'server_url': config.SERVER_URL
    })

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data.get('username') == config.DB_USER and data.get('password') == config.DB_PASSWORD:
        return jsonify({'message': 'Login successful', 'api_key': config.API_KEY})
    return jsonify({'message': 'Login failed'}), 401

if __name__ == '__main__':
    app.run(debug=True)
