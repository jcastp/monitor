import os
import psutil
import argparse
from readcfg.readcfg import *
from monitors import cpu, mem, disks, process


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

# Get the configuration files
read_general_config(config_file)

# Read all the options
read_particular_options(config_files_dict)

# DEBUG
print config_options


# Get the heartbeat signal
# TODO

# Check the different systems:

# Check CPU
## Check Thresholds
cpu.cpu_simple_threshold(config_options['cpu_threshold_warning'],
                         config_options['cpu_threshold_critical'])



# Check MEM
## Check Thresholds
mem.mem_simple_threshold(config_options['mem_threshold_warning'],
                         config_options['mem_threshold_critical'])


# Check Disks
## Check Thresholds


# Check processes
## Check all the processes are running
