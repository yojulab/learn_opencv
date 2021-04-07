from cv2 import cv2 as cv
from flask import Flask, Response, url_for

getCam = False
# setup video capture
if getCam == False:
    cam = cv.VideoCapture(0)
    cam.set(cv.CAP_PROP_FRAME_WIDTH, 320)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
    getCam = True

app = Flask(__name__)

@app.route('/stream.mjpg')
def do_stream():
    Response.set_header('Content-Type', 'multipart/x-mixed-replace; boundary=--MjpgBound')
    while True:
        ret,img = cam.read()
        jpegdata=cv.imencode(".jpeg",img)[1].tostring()
        string = "--MjpgBound\r\n"
        string += "Content-Type: image/jpeg\r\n"
        string += "Content-length: "+str(len(jpegdata))+"\r\n\r\n"
        string += jpegdata
        string += "\r\n\r\n\r\n"
        yield string

@app.route('/')
def do_route():
    return "<HTML><BODY><img src="+url_for('do_stream')+" width=320 height=240></BODY></HTML>"

if __name__ == '__main__':
    app.run(debug = True)
