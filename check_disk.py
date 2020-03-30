import psutil
import shutil
import os

print("\nCPU : " + str(psutil.cpu_percent(0.1)) + " %")

disk = shutil.disk_usage(os.path.expanduser("~"))
print("\nDisk Usage :\n")
print("TOTAL : {} GB.".format(disk.total//2**30))
print("USED  : {} GB.".format(disk.used//2**30))
print("FREE  : {} GB.".format(disk.free//2**30))
