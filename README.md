# Scratch-Userdata

## Overview

This is a Python program to collect data about Scratch projects and users for my Statistics project.

The code for data collection is `./local/main.py`.
 - The code uses a lot of RAM, so make sure you have at least 4GB. 
 - After running the program, the collected data will be written to `./local/dataset.csv`.

## Dependencies

To run the code, you will need Python 3 installed. The project uses the urllib3, json, time, threading, os, sys, tqdm, and requests libraries, all but the last two of which are in Python's standard library. 

To install the required dependencies, run `python3 -m pip install tqdm requests` in your commandline.

## Other Files

Results and analysis are included in `./Results`. The `./Results/Project Data` folder contains the complete collected raw data with some extra columns for analysis, and the `Report` folder contains the visual files in my final report.

The web version is currently broken, because pyodide has issues loading external files into the virtual file system. For the time being, you will have to run the local script.
