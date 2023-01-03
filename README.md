# Scratch-Userdata

## Overview

This is a Python program to collect data about Scratch projects and users for my statistics project.

The code for data collection is `./local/main.py`.

- The code uses a lot of RAM, so make sure you have at least 4GB.
- After running the program, the collected data will be written to `./local/dataset.csv`.

## Dependencies

To run the code, you will need Python 3 installed. The project uses the urllib3, json, time, threading, os, sys, tqdm, and requests libraries, all but the last two of which are in Python's standard library.

To install the required dependencies, run `python3 -m pip install tqdm requests` in your commandline.

## Other Files

Results and analysis are included in the `./results` folder.

- The `./results/project data` folder contains the collected raw data with some extra columns for analysis, and it also contains the LaTeX code and PDF for the paper writeup.
- The `./results/final-report` folder contains the PDFs for my final report (the project data and writeup).

The web version does not work, because pyodide has issues loading external files into the virtual file system. To collect the data yourself, you have to run the local script.
