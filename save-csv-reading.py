import serial
import csv
import time
import datetime

# Replace 'COM4' with the port your Arduino is connected to
# Raspi Port /dev/ttyACM0
arduino_port = 'COM11'
baud_rate = 9600
# Open the serial connection
ser = serial.Serial(arduino_port, baud_rate)

# Create a CSV file to store the data
# Get current date and time
now = datetime.datetime.now()
# Format the date-time string as 'MMDDYYYY-HHMM'
date_time_str = now.strftime("%d%m%Y-%H%M")
csv_file_path = f'{date_time_str}.csv'
counter = 0
capture_duration = 30
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    start_time = time.time()
    while (counter < capture_duration): 
        try:
            # Read a line from the serial port
            line = ser.readline().decode().strip()
            print(line)  # Print the received data

            # Write the received sensor value to the CSV file
            csv_writer.writerow([line])
            counter += 1
            time.sleep(1)

        except KeyboardInterrupt:
            break

# Close the serial connection
ser.close()
print("Serial connection closed.")


# Read data from CSV file
data = []
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        data.append(float(row[0]))
