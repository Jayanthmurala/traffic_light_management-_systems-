import unittest
from traffic_control_system.junction import Junction

class TestJunction(unittest.TestCase):
    def setUp(self):
        capacities = {'Line 1': 50, 'Line 2': 40, 'Line 3': 30, 'Line 4': 45}
        self.junction = Junction("Test Junction", capacities)

    def test_update_vehicles(self):
        self.junction.update_vehicles("Line 1", emergency=1, vehicle_count=30)
        self.assertEqual(self.junction.lines["Line 1"]['vehicles'], 30)
        self.assertEqual(self.junction.lines["Line 1"]['emergency'], 1)
