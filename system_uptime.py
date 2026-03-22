import os
import time

# Get system uptime
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime = f.readline().split()[0]
    return float(uptime)

if __name__ == '__main__':
    uptime_seconds = get_uptime()
    uptime_days = uptime_seconds // (24 * 3600)
    uptime_seconds %= (24 * 3600)
    uptime_hours = uptime_seconds // 3600
    uptime_seconds %= 3600
    uptime_minutes = uptime_seconds // 60
    uptime_seconds %= 60
    print(f'System Uptime: {int(uptime_days)} days, {int(uptime_hours)} hours, {int(uptime_minutes)} minutes, {int(uptime_seconds)} seconds')