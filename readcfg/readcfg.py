## This is the file storing the functions used to read the config
import os


# Dictionary of the configuration files used
# on the application
config_files_dict = {}


# The dictionary of options used for the application.
# It will be populated reading from the config files
config_options = {}


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
    return key, value


def read_general_config(filename):
    """Given a file, we get the files where we read the rest of
    the options."""
    print "Reading the general config file ..."

    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            # Get rid of empty lines
            if get_fine_line(line):
                # Get rid of the final newline character
                key, value = get_dict(line)
                config_files_dict[key] = value
    return


def read_particular_options(a_dictionary):
    """
    """
    for k in a_dictionary.keys():
        path = os.getcwd() + os.sep + a_dictionary[k].replace('"', '')
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if get_fine_line(line):
                    key, value = get_dict(line)
                    config_options[key] = value
    return
