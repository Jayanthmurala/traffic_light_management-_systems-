from traffic_control_system.junction import Junction
from traffic_control_system.traffic_control import TrafficControlSystem

# Setup junctions
capacities_j1 = {'Line 1': 50, 'Line 2': 40, 'Line 3': 30, 'Line 4': 45}
capacities_j2 = {'Line 1': 50, 'Line 2': 40, 'Line 3': 30, 'Line 4': 45}
j1 = Junction("J1", capacities_j1)
j2 = Junction("J2", capacities_j2)

# Update vehicles and emergency status for test cases (random vehicles, manual emergency)
j1.update_vehicles("Line 1", emergency=0)
j1.update_vehicles("Line 2", emergency=0)
j1.update_vehicles("Line 3", emergency=0)
j1.update_vehicles("Line 4", emergency=0)

j2.update_vehicles("Line 1", emergency=0)
j2.update_vehicles("Line 2", emergency=0)
j2.update_vehicles("Line 3", emergency=0)
j2.update_vehicles("Line 4", emergency=0)

# Initialize Traffic Control System
traffic_system = TrafficControlSystem([j1, j2])

# Run traffic control cycle
traffic_system.run_traffic_cycle()
