## This is the file storing the functions used to read the config
import os
import sys


# Set of comment characters. Lines with this at the
# beginning will be ignored
comment = set(['#', ';'])


###############
# test
###############


class DiskInfo:
    def __init__(self, device = None, mountpoint = None,
                  warning = None, critical = None,
                  comment = None):
        self.device = device
        self.mountpoint = mountpoint
        self.warning = warning
        self.critical = critical
        self.comment = comment
        
    def sanitize():
        return
        
    def print():
        return
        

class ProcessInfo:
    def __init__(self, name = None, path = None,
                  priority = None, starttime = None,
                  endtime= None, comment = None):
        self.name = name
        self.path = path
        self.priority = priority
        self.starttime = starttime
        self.endtime = endtime
        self.comment = comment
        
    def sanitize():
        return
        
    def print():
        return


########################################
# Check and sanitize functions
########################################


def get_fine_line(line):
    """Given a line, it check if it's non empty, or not commented."""
    if line and line != '\n' and line[0] not in comment:
        return True
    return False


def get_dict(line):
    """Given a valid line, we extract just the key - value pair,
    getting rid of the trailing spaces."""
    line = line.rstrip().lstrip()
    key, value = line.split('=')
    key = key.rstrip().lstrip()
    value = value.rstrip().lstrip()
    # Try to get the numbers as numbers
    try:
        value = float(value)
    except ValueError:
        pass
    return key, value
    
    
def sanitize_disk(a_tuple):
    """Starting from a tuple of strings, we are going to sanitize
    the input, so Python can work with it.
    """
    try:
        # TODO Check these parameters are between 0 and 100
        warn = float(a_tuple[2])
        crit = float(a_tuple[3])
    except ValueError:
        print """It seems that you didn't entered a number in the crit and warning.
        """
        sys.exit(3)
    san_tuple = (a_tuple[0], a_tuple[1], warn, crit, a_tuple[4].replace('"',''))
    return san_tuple
    
    
def sanitize_process(a_tuple):
    """Starting from a tuple of strings, we are going to sanitize
    the input, so Python can work with it.
    """
    try:
        # TODO Check this parameter is between 1 and 5
        priority = int(a_tuple[2])
        # TODO Convert the hour
    except ValueError:
        print """It seems that you didn't entered a number in the priority field.
        """
        sys.exit(3)
    san_tuple = (a_tuple[0], a_tuple[1], priority, a_tuple[3], a_tuple[4], a_tuple[5].replace('"',''))
    return san_tuple
    

############################################
# Reading configuration files
############################################


def read_general_config(filename):
    """Given a file, we get the files where we read the rest of
    the options."""
    print "Reading the general config file ..."
    config_files_dict = {}

    with open(filename, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            # Get rid of empty lines
            if get_fine_line(line):
                # Get rid of the final newline character
                key, value = get_dict(line)
                config_files_dict[key] = value
    return config_files_dict


def read_particular_options(a_file):
    """
    """
    config_options = {}
    path = os.getcwd() + os.sep + a_file.replace('"', '')
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if get_fine_line(line):
                key, value = get_dict(line)
                config_options[key] = value
    return config_options


def read_disks_options(a_file):
    """It reads comma separated lines.
    """
    # TODO check the comment, quoted with ""
    config_options = []
    path = os.getcwd() + os.sep + a_file.replace('"', '')
    with open(path, 'r') as f:
        lines=f.readlines()
        for line in lines:
            if get_fine_line(line):
                d_options = sanitize_disk(tuple(line.rstrip().split(',')))
                # Check the number of arguments extracted from the
                # options file
                if len(d_options) != 5:
                    print """There is an error in the disks option file.
                    It seems that there are more parameters than allowed.
                    """
                    sys.exit(2)
                config_options.append(d_options)
    return config_options
    

def read_process_options(a_file):
    """It reads comma separated lines.
    """
    # TODO check the comment, quoted with ""
    config_options = []
    path = os.getcwd() + os.sep + a_file.replace('"', '')
    with open(path, 'r') as f:
        lines=f.readlines()
        for line in lines:
            if get_fine_line(line):
                d_options = sanitize_process(tuple(line.rstrip().split(',')))
                # Check the number of arguments extracted from the
                # options file
                if len(d_options) != 6:
                    print """There is an error in the process option file.
                    It seems that there are more parameters than allowed.
                    """
                    sys.exit(2)
                config_options.append(d_options)
    return config_options


