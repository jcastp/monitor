## This is the file storing the functions used to read the config
import os
import sys


# Set of comment characters. Lines with this at the
# beginning will be ignored
comment = set(['#', ';'])


###############
# Classes
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
        
    def sanitize(self):
        # Get a float number from a string
        try:
            self.warning = float(self.warning)
            self.critical = float(self.critical)
        except ValueError:
            print "Error value on the disk file. Try to put a number ..."
            sys.exit(4)
            
        # Check the numbers are a percentage
        try:
            assert (0.0 <= self.warning <= 100.0) and (0.0 <= self.critical <= 100.0)
        except AssertionError:
            print "Number is not a percentage"
            sys.exit(4)
        # Get rid of the quotes
        self.comment = self.comment.replace('"', '')
        return
        
    def show(self):
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
        
        
    def sanitize(self):
        # Get an int from a string
        try:
            self.priority = int(self.priority)
        except ValueError:
            print "Error value in process file. It seems you didn't put a number ..."
            sys.exit(5)
            
        # Check the number is between boundaries
        try:
            assert (1 <= self.priority <= 5)
        except AssertionError:
            print "Priority must be between 1 and 5"
            sys.exit(5)
        # Get rid of the quotes
        self.comment = self.comment.replace('"', '')
        return
        
    def show(self):
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
    """It reads comma separated lines from the file, and passes the
    fields to an DiskInfo object.
    """
    # TODO check the comment, quoted with ""
    config_options = []
    path = os.getcwd() + os.sep + a_file.replace('"', '')
    with open(path, 'r') as f:
        lines=f.readlines()
        for line in lines:
            if get_fine_line(line):
                # Check the number of arguments are correct
                try:
                    device, mountpoint, warning, critical, comment = line.rstrip().split(',')
                except ValueError:
                    print "The number of arguments provided in the disks file is not correct."
                    sys.exit(4)
                temp = DiskInfo(device, mountpoint, warning, critical, comment)
                temp.sanitize()
                config_options.append(temp)
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
                # Check the number of arguments are correct
                try:
                    name, path, priority, starttime, endtime, comment = line.rstrip().split(',')
                except ValueError:
                    print "The number of arguments provided in the process file is not correct."
                    sys.exit(5)
                temp = ProcessInfo(name, path, priority, starttime, endtime, comment)
                temp.sanitize()
                config_options.append(temp)
    return config_options


