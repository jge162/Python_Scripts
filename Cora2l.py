import serial
import time

# Open a serial connection to the MSP432 board
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# Wait for the serial connection to initialize
time.sleep(2)

# Define the colors to cycle through
colors = ["red", "green", "blue"]

# Loop through the colors and turn on the LED
for color in colors:
    # Send a command to set the color
    ser.write(f"set_color {color}\n".encode())

    # Wait for the MSP432 board to process the command
    time.sleep(0.5)

# Turn off the LED
ser.write(b"led_off\n")

# Wait for the MSP432 board to process the command
time.sleep(0.5)

# Close the serial connection
ser.close()
