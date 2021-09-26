#!/usr/bin/env python3

from yeelight import Bulb
from yeelight import discover_bulbs
from pprint import pprint
import yaml

class yeelight_control:
    def __init__(self):
        self.bulbs = discover_bulbs()

    def get_bulbs(self):
        devices = discover_bulbs()
        self.devices_list = {}
        counter = 1
        for item in devices:
            to_add = {}
            to_add["ip"] = item["ip"]
            to_add["model"] = item['capabilities']['model']
            to_add["number"] = counter
            self.devices_list[counter] = to_add
            counter+=1

        pprint(self.devices_list)

    def user_prompt(self, device_list):
        print("Available devices: ")
        print(list(device_list.keys()))

# bulb = Bulb("192.168.2.160")

if __name__ == "__main__":
    print("Hello There!")

    # Read devices.yaml file to get list of devices and their addresses
    devices = {}

    # with open(r'devices.yaml') as file:
    #     devices = yaml.load(file, Loader=yaml.FullLoader)

    # # Create a dictionary with key value pairs as <bulb_name, bulb_object>
    # bulbs = {}
    # for device in device_list.keys():
    #     temp_device = Bulb()
    yl_obj = yeelight_control()
    yl_obj.get_bulbs()

    # user_prompt(devices)


