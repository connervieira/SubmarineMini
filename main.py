# Submarine Mini

# Copyright (C) 2024 V0LT - Conner Vieira 

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by# the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with this program (LICENSE)
# If not, see https://www.gnu.org/licenses/ to read the license agreement.


import os
import json
import time
import requests


submarine_directory = str(os.path.dirname(os.path.realpath(__file__)))
try:
    if (os.path.exists(submarine_directory + "/config.json")):
        config = json.load(open(submarine_directory + "/config.json")) # Load the configuration database from config.json
    else:
        print("The configuration file doesn't appear to exist at " + submarine_directory + "/config.json.")
        exit()
except:
    print("The configuration database couldn't be loaded. It may be corrupted.")
    exit()



def check_connectivity(target):
    response = os.system("ping -c 1 -w 1 " + target + " > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False


previously_offline_targets = [] # This list will be populated with hosts that have been offline for multiple cycles.
requests.post(config["notifications"]["host"], data="Submarine Mini has been started.".encode(encoding='utf-8'))

try:
    while True: # Run indefinitely, until terminated.
        os.system("clear") # Clear the console output.

        # Check connectivity.
        print("Checking connectivity...")
        offline_targets = [] # This list will be populated with any hosts that are offline.
        for target in config["targets"]: # Iterate through each target in the configuration.
            if (check_connectivity(target) == False): # Check to see if this target is offline.
                offline_targets.append(target) # Add this target to the list of offline targets.
        os.system("clear") # Clear the console output.


        # Handle notifications.
        for target in offline_targets:
            if (target not in previously_offline_targets):
                notification_text = str(config["targets"][target]["name"]) + " has gone offline."
                requests.post(config["notifications"]["host"], data=notification_text.encode(encoding='utf-8'))
        previously_offline_targets = offline_targets


        # Handle the console display.
        if (len(offline_targets) > 0): # Check to see if one or more targets is offline.
            print("The following targets are offline:")
            for target in offline_targets: # Iterate through each offline target.
                print("\t", str(target))
        else:
            print("All targets are online")


        time.sleep(float(config["general"]["interval"])) # Wait before repeating the loop.
except:
    requests.post(config["notifications"]["host"], data="Submarine Mini has been stopped.".encode(encoding='utf-8'))
