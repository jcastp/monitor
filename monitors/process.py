# Monitors for the processes
import os
import psutil


def check_processes(processes):
    """Given a list of processes, check if they are running.
    """
    # Get all the processes running right now
    for p in psutil.process_iter():
        # If the process name is in the set of the monitored processes,
        # we need to be sure the path is also the same
        if p.name() in processes.keys():
            print p.name()
            print p.as_dict(attrs=['exe','pid', 'name'])['exe']
            if (processes[p.name()].path + os.sep + p.name()) == p.as_dict(attrs=['exe','pid', 'name'])['exe']:
                print "Running"
            
