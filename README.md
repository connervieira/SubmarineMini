# Submarine Mini

**Copyright 2024 V0LT - Conner Vieira**

A command-line network connectivity status check utility.

## Note

Submarine Mini is distinct from normal [Submarine](https://v0lttech.com/submarine.php). Submarine Mini is a command-line only utility, designed primarily to send push notifications when network targets go down. Unlike full Submarine, Submarine Mini does not have a web interface.

## Description

Submarine Mini is a simply Python utility designed to monitor the status of a number of network targets, and send notifications when a target goes offline. This is useful for home and small business environments, where administrators may not necessarily notice a technical problem until it has been occuring for several hours. Submarine Mini is meant to run on a single board computer, like a Raspberry Pi, or any Linux desktop that is always running. When a target goes offline, Submarine Mini uses [ntfy](https://ntfy.sh) to send a push notification to one or more devices.
