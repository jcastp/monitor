## This is the file storing the functions used to read the config


# The dictionary of options used for the application.
# It will be populated reading from the config files
config_options = {}


# Set of comment characters. Lines with this at the
# beginning will be ignored
comment = set(['#', ';'])


# Get only non empty lines, and non commented
def get_fine_line(line):
    if line and line != '\n' and line[0] not in comment:
        return True
    return False


# Extract just the key - value pair from the line
def get_dict(line):
    line = line.rstrip().lstrip()
    key, value = line.split('=')
    key = key.rstrip().lstrip()
    value = value.rstrip().lstrip()
    return key, value


def read_general_config(filename):
    print "Reading the general config file ..."

    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            # Get rid of empty lines
            if get_fine_line(line):
                # Get rid of the final newline character
                key, value = get_dict(line)
                config_options[key] = value
    return
