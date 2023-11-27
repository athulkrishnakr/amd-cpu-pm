import os
from pm_modules.lib import log

EPP_PROFILES = ['performance', 'balance_performance', 'balance_power', 'power']

def set_epp(epp: str) -> int:
    CPUS = os.cpu_count()

    if epp in EPP_PROFILES:
        for cpu in range(CPUS):
            try:
                with open(f'/sys/devices/system/cpu/cpu{cpu}/cpufreq/energy_performance_preference', 'w') as cpu_epp:
                    cpu_epp.write(epp)
                    cpu_epp.close()

            except(OSError):
                log.warning(f'Cannot set EPP profile to: {epp}')
                return 2
            
        log.info(f'EPP set to: {epp}')
        return 0
    
    else:    
        log.error(f'Invalid argument for cpu: {epp}')
        return 1