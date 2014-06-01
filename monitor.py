import os
import sys
import psutil
import argparse
import socket
from readcfg.readcfg import *
from monitors import cpu, mem, disks, process


def main():

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
    # TODO complete this
    process_options = read_process_options(config_files_dict["process_options"])

    # DEBUG
    print cpu_options
    print mem_options
    print disks_options
    print process_options


    ## Main part of the application

    ##############################
    # Get machine information
    ##############################
    # Get OS
    system_type = sys.platform
    # Get the hostname
    hostname = socket.gethostname()

    # TODO Get the IP
    # Get the IP


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
    partitions = disks.get_partitions(disks_options)
    disks_data = disks.get_disk_usage(partitions)
    ## Check Thresholds
    # TODO


    # Check processes
    ## Check all the processes are running
    # TODO

    # DEBUG
    print cpu_usage
    print mem_data
    print disks_data
    
    
    ###############################
    # Exporting data to json
    ###############################
    # TODO
    
    ###############################
    # Send data to remote server
    ###############################
    # TODO
    

if __name__ == "__main__":
    main()
