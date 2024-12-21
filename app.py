from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('A user connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('A user disconnected')

@socketio.on('message')
def handle_message(data):
    print(f'Received message: {data}')
    socketio.emit('message', data, broadcast=True)  # Emit the message to all clients

@app.route('/')
def home():
    return render_template('chat.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
