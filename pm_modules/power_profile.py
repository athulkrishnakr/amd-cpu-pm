import subprocess
from pm_modules.lib import log

PLATFORM_POWER_PROFILES = ['power-saver', 'balanced', 'performance']

def set_platofrm_profile(power_profile: str) -> int:

    try:
        if power_profile in PLATFORM_POWER_PROFILES:
            subprocess.call(['powerprofilesctl', 'set', f'{power_profile}'])
            log.info(f'Platform power profile set to: {power_profile}')
            return 0
        
        else:
            log.error(f'Invalid argument for platform: {power_profile}')
            return 1
        
    except(FileNotFoundError):
        log.error(f'Cannot set Platform Power Profile to {power_profile}, powerprofilesctl not found')
        return 2
