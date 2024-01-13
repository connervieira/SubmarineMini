# Documentation

This file contains installation and usage instructions for Submarine Mini.


## Compatability

Submarine is primarily compatable with Linux, although it will likely work on other Unix-like operating systems, including MacOS and FreeBSD. However, Windows is unlikely to be compatible without modification.


## Download

Official releases of Submarine Mini can be downloaded from the V0LT website at <https://v0lttech.com/submarinemini.php>.


## Installation

To install Submarine Mini, simply copy it from the source you received it from to a location accessible to the system you want to run it on. Then, install the `requests` Python library, with `pip3 install requests`.

Optionally, you can register Submarine Mini as a SystemD service, so that it starts when the system boots. A sample SystemD service file can be found in the main Submarine Mini directory, named `submarinemini.service`. This file might need to be slightly modified depending on your system configuration, and which user you want to run the process as.


## Configuration

To configure Submarine to fit your needs, edit the `config.json` file. All configuration values are explained in the [CONFIGURATION.md](CONFIGURATION.md) document.


## Usage

Once you've installed and configured Submarine Mini, you can run it using `python3`. Alternatively, if you've set-up a SystemD service, you can start Submarine Mini with the `systemctl` command. After Submarine Mini starts, all device subscribed to the configured NTFY topic should receive a start-up notification.
