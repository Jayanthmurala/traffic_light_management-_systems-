class Junction:
    def __init__(self, name, capacities):
        self.name = name
        self.lines = {f"Line {i+1}": {'vehicles': 0, 'emergency': 0} for i in range(4)}
        self.capacities = capacities

    def update_vehicles(self, line, emergency, vehicle_count=None):
        if vehicle_count is None:
            vehicle_count = self._generate_random_vehicle_count(line)
        self.lines[line]['vehicles'] = vehicle_count
        self.lines[line]['emergency'] = emergency

    def get_traffic_distribution(self):
        return {line: data['vehicles'] for line, data in self.lines.items()}

    def get_emergency_status(self):
        return {line: data['emergency'] for line, data in self.lines.items()}

    def get_priority_lines(self):
        return sorted(self.lines.items(), key=lambda x: (-x[1]['emergency'], -x[1]['vehicles']))

    def _generate_random_vehicle_count(self, line):
        import random
        return random.randint(0, self.capacities[line])
