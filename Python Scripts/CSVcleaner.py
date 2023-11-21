#!/usr/bin/env python3

"""CSV clean-up tool
"""

import os
import sys
import argparse
import subprocess

pathSublimeText = 
pathCSVs = 

# walk os to csv file dir, list all .csv in dir
# for each .csv : subprocess.call(sublime, pathtocsv+csv)
# in sublime, find replace ",,,," with nothing
# in sublime, find replace ",,,0," with nothing 
# write out as .csv



try:
	subprocess.call([pathSublimeText, pathCSVs])
catch:
	print("Process call failed.")