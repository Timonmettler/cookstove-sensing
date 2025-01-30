# `src`

`main.py` script contains the most up to date routines for running data acquisition and transfer from a scale and a thermocouple on Raspberry Pi Pico.

Before uploading `main.py` onto Raspberry Pi pico, update `APIkey` and `Channel` variables from your Thingspeak account. Then, load the main code and all the libraries to the Pi Pico.

`calibration_testing` directory contains scripts allowing to:
- calibrate the load cell
- set up the real time clock
- test thermocouples