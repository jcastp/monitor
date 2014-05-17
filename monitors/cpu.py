## Monitor functions for the CPU
import psutil

def cpu_simple_threshold(warn, crit):
    print "cpu testing"
    cpu_usage = psutil.cpu_percent(interval = 1, percpu=True)
    print cpu_usage
    for value in cpu_usage:
        print value, warn, crit
        if value >= warn and value < crit:
            print "Warning CPU alert"
            # TODO
        elif value >= crit:
            print "Critical CPU alert"
            # TODO
    return
