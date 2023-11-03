import pm_modules.lib

GPU_PROFILES = ['low', 'auto', 'high']
card_list = []

output = pm_modules.lib.subprocess.check_output('ls /dev/dri | grep card', shell=True).split()
for i in output:
    card = str(i)
    card = card.replace('b', '')
    card = card.replace('\'', '')
    card_list.append(card)


def set_gpu_profile(gpu_profile: str):
    if gpu_profile in GPU_PROFILES:
        for card in card_list:
            try:
                with open(f'/sys/class/drm/{card}/device/power_dpm_force_performance_level', 'w') as power_dpm:
                    power_dpm.write(gpu_profile)
                    power_dpm.close()
            except(OSError):
                pm_modules.lib.log.warning(f'Cannot access {card}')
        pm_modules.lib.log.info(f'GPU profile set to: {gpu_profile}')
    else:    
        pm_modules.lib.log.error(f'Invalid argument: {gpu_profile}')

