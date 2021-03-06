# Here, we will stablish the disks monitors
import psutil
import collections


# Create a named tuple to contain all the info for the disks monitorized
disk_info = collections.namedtuple("disk_info", ['device', 'mountpoint',
                                    'fstype', 'opts', 'total', 'used',
                                    'free', 'percent'])


def get_partitions(monitored=[]):
    """We get a named tuple with the data of the physical partitions
    present on the machine.
    """
    # Get all the physical partitions present on the machine
    raw_part = psutil.disk_partitions()
    # Create and populate a set with all the mountpoints in the
    # monitored disk file config
    mountpoints = set()
    for item in monitored:
        mountpoints.add(item.mountpoint)
        
    # And now, we only get the partitions that are monitored in the file
    partitions = []
    for item in raw_part:
        if item.mountpoint in mountpoints:
            partitions.append(item)
    return partitions
    

def get_disk_usage(partitions):
    """Given the partitions in the machine, we select only the ones present
    in the config file to be monitorized, and we check the usage data
    of those.
    Arguments:
        - partitions: a named tuple of the partitions present on the machine
        - monitored: a list of partitions we want to monitor.
    Returns: a list of named tuples
    """
    disks_data = []
    # TODO Select only those that are monitorized
    for disk in partitions:
        d_usage = psutil.disk_usage(disk.mountpoint)
        # Here, we join the two named tuples, so we can
        # get all the information
        d_info = disk_info(disk.device, disk.mountpoint, disk.fstype,
                            disk.opts, d_usage.total, d_usage.used,
                            d_usage.free, d_usage.percent)
        # Add the data to the list
        disks_data.append(d_info)
    return disks_data


def simple_threshold_disk():
    """
    """
    # TODO Complete the disks threslhold function
    return
