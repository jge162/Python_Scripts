import os
import pathlib

import cv2
from pycoral.utils import edgetpu
from pycoral.utils import dataset
from pycoral.adapters import common
from pycoral.adapters import classify

# Specify the TensorFlow model, labels, and camera device
script_dir = pathlib.Path(__file__).parent.absolute()  # gets the absolute path to the directory of the script
model_file = os.path.join(script_dir, '2-17model.tflite')  # creates a full path to the model file
label_file = os.path.join(script_dir, '2-17labels.txt')  # creates a full path to the labels file
device = 1  # index of the camera device to use
width = 640  # width of the camera frame in pixels
height = 480  # height of the camera frame in pixels

# Initialize the TF interpreter
interpreter = edgetpu.make_interpreter(model_file)  # creates an interpreter object for the specified TFLite model file
interpreter.allocate_tensors()  # allocates memory for the interpreter's input and output tensors

# Open the camera device
cap = cv2.VideoCapture(device)  # creates a VideoCapture object to open the camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # sets the width of the camera frame
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # sets the height of the camera frame

# Loop over frames from the camera
while True:
    # Capture the current frame from the camera
    ret, frame = cap.read()  # reads the current frame from the camera and returns a flag (ret) and the frame data (frame)

    # Convert the frame to RGB format and resize it
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # converts the frame from BGR to RGB color space
    size = common.input_size(interpreter)  # gets the expected input size for the TFLite model
    rgb = cv2.resize(rgb, size)  # resizes the frame to the expected input size

    # Pass the resized frame to the interpreter
    common.set_input(interpreter, rgb)  # sets the resized frame as the input tensor of the interpreter

    # Run an inference
    interpreter.invoke()  # runs an inference on the input tensor using the TFLite model
    classes = classify.get_classes(interpreter, top_k=1)  # gets the classification result from the output tensor

    # Print the result and check the class label and confidence score
    labels = dataset.read_label_file(label_file)  # reads the label file to get the class names
    for c in classes:
        class_label = labels.get(c.id, c.id)  # gets the class name corresponding to the class ID
        confidence = c.score  # gets the confidence score of the classification result
        if class_label == 'Recycling' and confidence > 0.5:
            pass  # placeholder for arduino GPIO
        elif class_label == 'Waste' and confidence > 0.5:
            pass  # placeholder for arduino GPIO
        elif class_label == 'Compost' and confidence > 0.5:
            pass  # placeholder for arduino GPIO
        print('%s %.5f' % (class_label, confidence))  # prints the class label and confidence score

        # Draw a box around the object of interest
        bbox = c.bbox  # gets the bounding box coordinates of the object
        x0, y0, x1, y1 = bbox  # unpacks the bbox coordinates into separate variables
        x0 = int(x0 * frame.shape[1])  # scales the x-coordinate of the top-left corner of the bbox to the size of the frame
        y0 = int(y0 * frame.shape[0])  # scales the y-coordinate of the top-left corner of the bbox to the size of the frame
        x1 = int(x1 * frame.shape[1])  # scales the x-coordinate of the bottom-right corner of the bbox to the size of the frame
        y1 = int(y1 * frame.shape[0])  # scales the y-coordinate of the bottom-right corner of the bbox to the size of the frame
        cv2.rectangle(frame, (x0, y0), (x1, y1), (0, 255, 0), 2)  # draws a green rectangle around the object

        # Display the frame with the confidence value
        cv2.putText(frame, "Confidence: %.2f" % confidence, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
        cv2.imshow('Object Detection', frame)

  # Exit on 'q' key
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
