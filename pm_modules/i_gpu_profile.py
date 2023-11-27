from pm_modules.gpu import igpu_path
from pm_modules.lib import log

GPU_PROFILES = ['low', 'auto', 'high']

def set_gpu_profile(gpu_profile: str) -> int:

    IGPU_PATH = igpu_path()
    if IGPU_PATH == 2:
        return IGPU_PATH
    
    if gpu_profile in GPU_PROFILES:

        try:
            with open(f'{IGPU_PATH}/power_dpm_force_performance_level', 'w') as power_dpm:
                power_dpm.write(gpu_profile)
                power_dpm.close()
        except(OSError):
            log.warning(f'Cannot access {IGPU_PATH}')
            return 2
        
        log.info(f'GPU profile set to: {gpu_profile}')
        return 0
    
    else:    
        log.error(f'Invalid argument for gpu: {gpu_profile}')
        return 1

