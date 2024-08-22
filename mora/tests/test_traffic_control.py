import unittest
from traffic_control_system.junction import Junction
from traffic_control_system.traffic_control import TrafficControlSystem

class TestTrafficControlSystem(unittest.TestCase):
    def setUp(self):
        capacities_j1 = {'Line 1': 50, 'Line 2': 40, 'Line 3': 30, 'Line 4': 45}
        capacities_j2 = {'Line 1': 50, 'Line 2': 40, 'Line 3': 30, 'Line 4': 45}
        self.j1 = Junction("J1", capacities_j1)
        self.j2 = Junction("J2", capacities_j2)
        self.traffic_system = TrafficControlSystem([self.j1, self.j2])

    def test_synchronize_junctions(self):
        self.j1.update_vehicles("Line 4", emergency=0, vehicle_count=40)
        self.j2.update_vehicles("Line 1", emergency=0, vehicle_count=5)
        can_handle = self.traffic_system.synchronize_junctions(0, "Line 4", 1, "Line 1")
        self.assertTrue(can_handle)
