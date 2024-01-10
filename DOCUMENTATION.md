# Documentation

This file contains installation and usage instructions for Submarine Mini.


## Compatability

Submarine is primarily compatable with Linux, although it will likely work on other Unix-like operating systems, including MacOS and FreeBSD. However, Windows is unlikely to be compatible without modification.

## Installation

To install Submarine Mini, simply copy it from whatever source you received it from to a location in your system. Then, install the `requests` Python library, with `pip3 install requests`.

Optionally, you can register Submarine Mini as a SystemD service, so that it starts when the system boots. A sample SystemD service file can be found in the main Submarine Mini directory, named `submarinemini.service`.

## Configuration

To configure Submarine to fit your needs, edit the `config.json` file. All configuration values are explained in the [CONFIGURATION.md](CONFIGURATION.md) document.
