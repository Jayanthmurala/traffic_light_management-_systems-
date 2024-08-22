# C:\mora\traffic_control_system\utilities.py

import random
import time

def generate_random_vehicle_flow(min_flow=1, max_flow=10):
    """
    Generates a random number of vehicles for each traffic cycle.
    :param min_flow: Minimum number of vehicles.
    :param max_flow: Maximum number of vehicles.
    :return: Number of vehicles generated.
    """
    return random.randint(min_flow, max_flow)

def get_current_time_formatted():
    """
    Gets the current system time formatted as HH:MM:SS.
    :return: Formatted string representing the current time.
    """
    return time.strftime("%H:%M:%S", time.localtime())

def calculate_traffic_density(vehicles, max_capacity=100):
    """
    Calculates traffic density based on the number of vehicles and max road capacity.
    :param vehicles: Number of vehicles on the road.
    :param max_capacity: Maximum capacity of the road.
    :return: Traffic density as a percentage.
    """
    return min(vehicles / max_capacity * 100, 100)

