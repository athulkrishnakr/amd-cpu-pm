import pm_modules.lib

PLATFORM_POWER_PROFILES = ['power-saver', 'balanced', 'performance']

def set_platofrm_profile(power_profile: str):
    try:
        if power_profile in PLATFORM_POWER_PROFILES:
            pm_modules.lib.subprocess.call(['powerprofilesctl', 'set', f'{power_profile}'])
            pm_modules.lib.log.info(f'Platform power profile set to: {power_profile}')
        else:
            pm_modules.lib.log.error(f'Invalid argument: {power_profile}')
    except(FileNotFoundError):
        pm_modules.lib.log.error(f'Cannot set Platform Power Profile to {power_profile}, powerprofilesctl not found')
