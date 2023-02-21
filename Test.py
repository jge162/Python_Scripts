import os
import pathlib
import time
import cv2
from pycoral.utils import edgetpu
from pycoral.utils import dataset
from pycoral.adapters import common
from pycoral.adapters import classify
import serial


# Specify the TensorFlow model, labels, and camera device
script_dir = pathlib.Path(__file__).parent.absolute()
model_file = os.path.join(script_dir, '2-17model.tflite')
label_file = os.path.join(script_dir, '2-17labels.txt')
device = 1
width = 640
height = 480

# Initialize the TF interpreter
interpreter = edgetpu.make_interpreter(model_file)
interpreter.allocate_tensors()

# Open the camera device
cap = cv2.VideoCapture(device)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


def main():
    # Call the setup function to initialize the GPIO pins and stepper motors.
    # Loop over frames from the camera
    camera_paused = False
    while True:
        # Capture the current frame from the camera
        ret, frame = cap.read()

        # Convert the frame to RGB format and resize it
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        size = common.input_size(interpreter)
        rgb = cv2.resize(rgb, size)

        # Pass the resized frame to the interpreter
        common.set_input(interpreter, rgb)

        # Run an inference
        interpreter.invoke()
        classes = classify.get_classes(interpreter, top_k=1)

        # Print the result and check the class label and confidence score
        labels = dataset.read_label_file(label_file)
        for c in classes:
            class_label = labels.get(c.id, c.id)
            confidence = c.score
            if class_label == 'SodaCan' and confidence > 0.7:
                # Check if the camera is already paused
                if not camera_paused:
                    # Pause the camera by setting the variable to True
                    camera_paused = True
                    # Trigger the recycling process
                    ser = serial.Serial('/dev/ttyACM0',9600) 
                    time.sleep(2)
                    ser.write(b'composting')
                    ser.close()
                    time.sleep(3)
                # Exit the loop to prevent multiple instances of triggering
                break

        # If the camera is not paused, display the frame and check for user input
        if not camera_paused:
            print('%s detected: = %.5f' % (class_label, confidence))
            # Display the frame with the confidence value
            cv2.putText(frame, "Confidence: %.2f" % confidence, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Object Detection', frame)

            # Exit on 'c' key
            if cv2.waitKey(1) & 0xFF == ord('c'):
                break

        # If the camera is paused, wait for a key press to resume
        else:
            # Display a message indicating that the camera is paused
            cv2.putText(frame, "Camera paused. Press 'r' to resume.", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Object Detection', frame)

            # Wait for 'r' key to be pressed
            if cv2.waitKey(1) & 0xFF == ord('r'):
