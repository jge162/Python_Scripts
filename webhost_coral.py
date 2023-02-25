import cv2
from flask import Flask, Response

app = Flask(__name__)

# Create a VideoCapture object to access the camera
cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        if not ret:
            # If the frame was not captured, break the loop
            break

        # Encode the frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)

        # Convert the buffer to bytes
        frame_bytes = buffer.tobytes()

        # Yield the frame as a response to the client
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # Return a response containing the video stream
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Start the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
