## Memory monitor functions
import psutil


def get_mem():
    return psutil.virtual_memory()


def mem_simple_threshold(mem_list, warn, crit):
    """
    """
    print "Memory monitor in course ..."
    # TODO
    mem_percent = mem_list[2]
    print mem_percent, warn, crit
    if mem_percent >= warn and mem_percent < crit:
        print "Warning memory"
        # TODO Return an alert object
    elif mem_percent >= crit:
        print "Critical memory"
        # TODO Return an alert object
    return
