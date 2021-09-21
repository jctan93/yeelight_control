#!/usr/bin/env python3

from yeelight import Bulb
from yeelight import discover_bulbs
import yaml

class yeelight_control:
    def __init__(self):
        self.geek = "GeekforGeeks"

    def user_prompt(device_list):
        print("Available devices: ")
        print(list(device_list.keys()))

# bulb = Bulb("192.168.2.160")

if __name__ == "__main__":
    print("Hello There!")

    # Read devices.yaml file to get list of devices and their addresses
    devices = {}

    with open(r'devices.yaml') as file:
        devices = yaml.load(file, Loader=yaml.FullLoader)

    # Create a dictionary with key value pairs as <bulb_name, bulb_object>
    bulbs = {}
    for device in device_list.keys():
        temp_device = Bulb()

    user_prompt(devices)


