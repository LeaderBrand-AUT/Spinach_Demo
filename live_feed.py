import cv2
from scripts.constants import *

ip = '192.168.88.109'
port = '8080'

RTSP_LINK = 'http://158.58.130.148/mjpg/video.mjpg'

camera = cv2.VideoCapture(RTSP_LINK, cv2.CAP_FFMPEG)

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            yield (b'---frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def get_frame():
    success, frame = camera.read()
    if not success:
        print('There was an error getting the frame from the live feed')
        return
    else:
        return frame