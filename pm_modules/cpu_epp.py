import pm_modules.lib

EPP_PROFILES = ['performance', 'balance_performance', 'balance_power', 'power']

def set_epp(epp: str):
    CPUS = pm_modules.lib.os.cpu_count()
    if epp in EPP_PROFILES:
        for cpu in range(CPUS):
            try:
                with open(f'/sys/devices/system/cpu/cpu{cpu}/cpufreq/energy_performance_preference', 'w') as cpu_epp:
                    cpu_epp.write(epp)
                    cpu_epp.close()
            except(OSError):
                pm_modules.lib.log.warning(f'Cannot set EPP profile to: {epp}')
                return
        pm_modules.lib.log.info(f'EPP set to: {epp}')
    else:    
        pm_modules.lib.log.error(f'Invalid argument: {epp}')
