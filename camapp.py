from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def cam():
    return render_template("liveweb1.html")

@socketio.on('frame', namespace='/test')
def user_video(frame):
	feed = frame
	print (str(feed))
	
	
if __name__ == '__main__':
    socketio.run(app)
