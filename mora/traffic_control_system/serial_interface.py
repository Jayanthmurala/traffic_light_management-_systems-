# C:\mora\traffic_control_system\serial_interface.py

import serial
import time

class SerialInterface:
    def __init__(self, port='COM3', baudrate=9600):
        self.ser = serial.Serial(port, baudrate)

    def send_timing_data(self, timing_data):
        """
        Sends timing data to the Arduino via serial communication.
        :param timing_data: A dictionary containing traffic light timing data for each line.
        """
        try:
            for line, times in timing_data.items():
                green_time, yellow_time, red_time = times
                message = f"{line},{green_time},{yellow_time},{red_time}\n"
                self.ser.write(message.encode())
                print(f"Sent to Arduino: {message.strip()}")
                time.sleep(1)  # Wait a bit before sending the next data
        except KeyboardInterrupt:
            self.close_connection()

    def close_connection(self):
        """
        Closes the serial connection.
        """
        if self.ser.is_open:
            self.ser.close()
            print("Serial connection closed.")
