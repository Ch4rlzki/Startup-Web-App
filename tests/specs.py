import platform
import psutil
import cpuinfo

# Get CPU information
cpu_info = cpuinfo.get_cpu_info()

# Get memory information
memory_info = psutil.virtual_memory()

# Get disk information
disk_info = psutil.disk_usage('/')

# Get system information
system_info = platform.uname()

print(f"System: {system_info.system} {system_info.release}")
print(f"Machine: {system_info.machine}")
print(f"Processor: {cpu_info['brand_raw']}")
print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
print(f"CPU Threads: {psutil.cpu_count(logical=True)}")
print(f"RAM: {memory_info.total / (1024**3):.2f} GB")
print(f"Disk Space: {disk_info.total / (1024**3):.2f} GB")