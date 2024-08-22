# C:\mora\tests\test_serial_interface.py

import unittest
from traffic_control_system.serial_interface import SerialInterface

class TestSerialInterface(unittest.TestCase):
    def setUp(self):
        self.serial_interface = SerialInterface(port='COM3', baudrate=9600)

    def test_send_timing_data(self):
        timing_data = {
            'DLINE_1': (10, 3, 5),
            'DLINE_2': (8, 3, 5),
            'DLINE_3': (12, 4, 6),
            'DLINE_4': (9, 2, 4)
        }
        # Just testing if the function runs without exceptions
        self.serial_interface.send_timing_data(timing_data)
        
    def tearDown(self):
        self.serial_interface.close_connection()

if __name__ == "__main__":
    unittest.main()
