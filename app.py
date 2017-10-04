from flask import Flask, render_template, Response
from videostream import VideoStream

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def gen(stream):
    while True:
        frame = stream.detect_faces()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video')
def video_feed():
    return Response(gen(VideoStream()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
