import os
import psutil
import argparse
import socket
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


#####################################
# Reading the options
#####################################


# Use a general config file, and derive the rest from that
config_file = args.config

# Get the configuration files
config_files_dict = read_general_config(config_file)
print config_files_dict

## Read all the options
# cpu options
cpu_options = read_particular_options(config_files_dict["cpu_options"])
# mem options
mem_options = read_particular_options(config_files_dict["mem_options"])
# disks options
disks_options = read_disks_options(config_files_dict["disks_options"])
# process options
process_options = read_process_options(config_files_dict["process_options"])

# DEBUG
print cpu_options, mem_options, disks_options, process_options


##############################
# Get machine information
##############################


## Main part of the application
# TODO Get the IP
# Get the IP

# Get the hostname
hostname = socket.gethostname()


################################
# Main loop of the application
################################

# Get the heartbeat signal
# TODO Does it makes sense if we send the data once a minute?

# Check the different systems:

# Get CPU usage
cpu_usage = cpu.get_cpu()
## Check Thresholds
# TODO


# Get MEM
mem_data = mem.get_mem()
## Check Thresholds
# TODO


# Check Disks
## Check Thresholds


# Check processes
## Check all the processes are running





print cpu_usage, mem_data

#if __name__ == "__main__":
#    main()
