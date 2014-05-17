import psutil
import argparse
from readcfg.readcfg import *
import os


## Here will be the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--config",
                    help="Specify where the config file is",
                    action="store",
                    default = "./config/config.cfg"
                   )

args = parser.parse_args()


# Use a general config file, and derive the rest from that
config_file = args.config

# Get the configuration options
read_general_config(config_file)

read_particular_options(config_files_dict)

print config_options





# Read the options from file
## Different files for diferent systems: cpu, mem, disks, etc.


# Get the heartbeat signal

# Check the different systems:

# Check CPU
## Check Thresholds
def check_cpu(threshold):
    # get the CPU utilization por core
    # If the CPU usage is above the thresholds, then
    # an error is thrown
    return


# Check MEM
## Check Thresholds


# Check Disks
## Check Thresholds


# Check processes
## Check all the processes are running
