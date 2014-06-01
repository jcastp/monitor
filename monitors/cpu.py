## Monitor functions for the CPU
import psutil


def get_cpu():
    """We get the raw information about the cpu being used.
    We get all cores, even the virtual ones, and return a
    tuple with the values.
    """
    return psutil.cpu_percent(interval = 1, percpu=True)


def cpu_simple_threshold(cpu_usage_list, warn, crit):
    """
    """
    print "cpu testing"
    print cpu_usage_list
    for value in cpu_usage_list:
        print value, warn, crit
        if value >= warn and value < crit:
            print "Warning CPU alert"
            # TODO Return an alert object
        elif value >= crit:
            print "Critical CPU alert"
            # TODO Return an alert object
    return 
