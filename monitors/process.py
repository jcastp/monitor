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
            # We get the info of the process
            info_process = p.as_dict(attrs=['exe', 'pid', 'name'])
            if (processes[p.name()].path + os.sep + p.name()) == info_process['exe']:
                print "Process " + info_process['exe'] + " is running."
            else:
                # TODO Raise an alert for the process is not running
                print "Process " + processes[p.name()].path + os.sep + p.name() + " is NOT RUNNING."
                pass
            
