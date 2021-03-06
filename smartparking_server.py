#from source import spots
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

VIDEO_SOURCE = 1
cap = cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
    # Capture frame-by-frame
        success, frame = cap.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

#class TestServer(socketserver.TCPServer):
    #allow_reuse_address = True

#def start_test_server(port=5000):
    #handler = http.server.SimpleHTTPRequestHandler
    #httpd = TestServer(("", port), handler)
    #httpd_thread = threading.Thread(target=httpd.serve_forever)
    #httpd_thread.setDaemon(True)
    #httpd_thread.start()
    
    
#run app
@app.route("/")
@app.route("/home")
def homeSite():
	return render_template('home.html')
     
@app.route("/clientSite")
def clientSite():
	return render_template('index.html')
 
	
@app.route("/video_feed")
def video_feed():
     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
