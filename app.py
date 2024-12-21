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