import time
from traffic_control_system.junction import Junction

class TrafficControlSystem:
    def __init__(self, junctions):
        self.junctions = junctions

    def synchronize_junctions(self, from_junction_idx, from_line, to_junction_idx, to_line):
        outgoing_vehicles = self.junctions[from_junction_idx].lines[from_line]['vehicles']
        incoming_vehicles = outgoing_vehicles + self._generate_random_traffic()

        to_junction = self.junctions[to_junction_idx]
        to_capacity_remaining = to_junction.capacities[to_line] - to_junction.lines[to_line]['vehicles']
        
        if incoming_vehicles > to_capacity_remaining:
            return False  # Can't handle the incoming traffic
        return True

    def adjust_green_time(self, base_time, line_vehicles, max_vehicles):
        return base_time + (line_vehicles / max_vehicles) * base_time if max_vehicles > 0 else base_time

    def adjust_yellow_time(self, base_yellow_time, line_vehicles, max_vehicles):
        if line_vehicles > max_vehicles * 0.75:
            return base_yellow_time + 2
        return base_yellow_time

    def adjust_red_time(self, base_red_time, previous_green_shortened):
        return base_red_time + 3 if previous_green_shortened else base_red_time

    def run_traffic_cycle(self):
        base_green_time = 10
        base_yellow_time = 3
        base_red_time = 5

        for junction in self.junctions:
            print(f"\nJunction {junction.name} Signal Cycle:")
            max_vehicles = max(junction.get_traffic_distribution().values())
            for line, data in junction.get_priority_lines():
                green_time = self.adjust_green_time(base_green_time, data['vehicles'], max_vehicles)
                yellow_time = self.adjust_yellow_time(base_yellow_time, data['vehicles'], max_vehicles)
                red_time = base_red_time

                if data['emergency']:
                    green_time += 5

                previous_green_shortened = False
                if junction.name == "J1" and line == "Line 4":
                    can_handle = self.synchronize_junctions(0, "Line 4", 1, "Line 1")
                    if not can_handle:
                        green_time *= 0.7
                        previous_green_shortened = True
                        print(f"J1 Line 4: Reduced green time due to J2 Line 1 capacity. New green time: {green_time:.2f} seconds.")

                if junction.name == "J2" and line == "Line 4":
                    can_handle = self.synchronize_junctions(1, "Line 4", 0, "Line 4")
                    if not can_handle:
                        green_time *= 0.7
                        previous_green_shortened = True
                        print(f"J2 Line 4: Reduced green time due to J1 Line 4 capacity. New green time: {green_time:.2f} seconds.")

                red_time = self.adjust_red_time(base_red_time, previous_green_shortened)

                print(f"{line}: Green for {green_time:.2f} seconds. Vehicles: {data['vehicles']}. Emergency: {'Yes' if data['emergency'] else 'No'}")
                time.sleep(0.5)

                print(f"{line}: Yellow for {yellow_time:.2f} seconds.")
                time.sleep(0.5)

                print(f"{line}: Red for {red_time:.2f} seconds.")
                time.sleep(0.5)

    def _generate_random_traffic(self):
        import random
        return random.randint(0, 20)
