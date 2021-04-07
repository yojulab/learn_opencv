from cv2 import cv2 as cv
from flask import Flask, url_for, Response
app = Flask(__name__)

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv.VideoCapture(0)
#         self.video.set(cv.CAP_PROP_FRAME_WIDTH, 320)
#         self.video.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv.imencode('.jpg', image)
        return jpeg.tobytes()

@app.route('/')
def index():
    return "<HTML><BODY><img src="+url_for('video_feed')+"></BODY></HTML>"

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)