from flask import Flask,render_template
from flask_socketio import SocketIO

app = Flask(__name__)  
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('chat.html')

if __name__ == '__main__':
    socketio.run(app,debug=True)

@socketio.on('connect')
def handle_connect():
    print('A user connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('A user diconnected..')

@socketio.on('message')
def handle_message(data):
    print(f'Received message: {data}')
    socketio.send(data,broadcast=True)