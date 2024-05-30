
import serial
import time
import datetime

# Replace 'COM4' with the port your Arduino is connected to
# Raspi Port /dev/ttyACM0
arduino_port = 'COM4'
baud_rate = 9600
# Open the serial connection
ser = serial.Serial(arduino_port, baud_rate)

# Get current date and time
now = datetime.datetime.now()
# Format the date-time string as 'MMDDYYYY-HHMM'
date_time_str = now.strftime("%d%m%Y-%H%M")

start_time = time.time()
while (time.time() - start_time) <= 30:  # Run for 30 seconds
    try:
        # Read a line from the serial port
        line = ser.readline().decode().strip()
        print(line)  # Print the received data

    except KeyboardInterrupt:
        break

# Close the serial connection
ser.close()
print("Serial connection closed.")


