## This is the file storing the functions used to read the config
import os
import sys


# Set of comment characters. Lines with this at the
# beginning will be ignored
comment = set(['#', ';'])


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
                d_options = tuple(line.rstrip().split(','))
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
                d_options = tuple(line.rstrip().split(','))
                # Check the number of arguments extracted from the
                # options file
                if len(d_options) != 6:
                    print """There is an error in the process option file.
                    It seems that there are more parameters than allowed.
                    """
                    sys.exit(2)
                config_options.append(d_options)
    return config_options


# TODO Create functions to convert the tuples' values from string to
#   a better format. Eg. int or float, or date ...
