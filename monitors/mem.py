## Memory monitor functions
import psutil

def mem_simple_threshold(warn, crit):
    """
    """
    print "Memory monitor in course ..."
    mem_percent = psutil.virtual_memory()[2]
    print mem_percent, warn, crit
    if mem_percent >= warn and mem_percent < crit:
        print "Warning memory"
    elif mem_percent >= crit:
        print "Critical memory"
    return
