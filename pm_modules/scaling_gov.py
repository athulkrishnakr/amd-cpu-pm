import os
from pm_modules.lib import log

GOV_PROFILES = ['powersave', 'performance']
SCALING_GOV = '/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor'

def get_current_gov() -> str:
    try:
        with open(SCALING_GOV, 'r') as gov:
            current_gov = gov.read().strip()
            gov.close()
    except(FileNotFoundError):
        log.warning(f'Scaling governor not available')
    return current_gov

def set_gov(gov: str):
    CPUS = os.cpu_count()
    if gov in GOV_PROFILES: 
        for cpu in range(CPUS):
            try:
                with open(f'/sys/devices/system/cpu/cpu{cpu}/cpufreq/scaling_governor', 'w') as cpu_gov:
                    cpu_gov.write(gov)
                    cpu_gov.close()     
            except(OSError):
                log.error('Cannot set scaling governor')
                exit(1)
        log.info(f'Scaling governor set to: {gov}')