import serial
import time

# Open a serial connection to the MSP432 board
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# Wait for the serial connection to initialize
time.sleep(2)

# Send a command to turn on the LED
ser.write(b'led_on\n')

# Wait for the MSP432 board to process the command
time.sleep(0.5)

# Close the serial connection
ser.close()
