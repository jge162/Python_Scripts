device1 = 1
device2 = 2
width = 640
height = 480

# Initialize the TF interpreter
interpreter = edgetpu.make_interpreter(model_file)
interpreter.allocate_tensors()

# Open the camera devices
cap1 = cv2.VideoCapture(device1)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cap2 = cv2.VideoCapture(device2)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def main():
    # Call the setup function to initialize the GPIO pins and stepper motors.
    # Loop over frames from the cameras
    while True:
        # Capture the current frames from the cameras
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        # Convert the frames to RGB format and resize them
        rgb1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
        rgb2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
        size = common.input_size(interpreter)
        rgb1 = cv2.resize(rgb1, size)
        rgb2 = cv2.resize(rgb2, size)

        # Pass the resized frames to the interpreter
        common.set_input(interpreter, rgb1)

        # Run an inference on the first frame
        interpreter.invoke()
        classes1 = classify.get_classes(interpreter, top_k=1)

        # Print the result and check the class label and confidence score
        labels = dataset.read_label_file(label_file)
        for c in classes1:
            print('Device 1: Class ID {}, Label {}, Score {}'.format(c.id, labels[c.id], c.score))

        # Pass the resized frames to the interpreter
        common.set_input(interpreter, rgb2)

        # Run an inference on the second frame
        interpreter.invoke()
        classes2 = classify.get_classes(interpreter, top_k=1)

        # Print the result and check the class label and confidence score
        labels = dataset.read_label_file(label_file)
        for c in classes2:
            print('Device 2: Class ID {}, Label {}, Score {}'.format(c.id, labels[c.id], c.score))
