import pyudev
from pm_modules.lib import log

#CPU_FM = ['REMBRANDT']
#VENDOR = ['0x1002']
DEVICE = ['0x1681']
CLASS = '0x030000'
IGPU_PATH = None
DGPU_PATH = None

context = pyudev.Context()
pci_devices = context.list_devices(SUBSYSTEM='pci')

card_list = []

def igpu_path():
     for pci in pci_devices:
          #print(pci)
          att = pci.attributes
          
          try:
               if att.asstring('class') == CLASS:
                    card_list.append(pci)     
          except:
               continue

     #print(card_list)
     if card_list:
          log.info(f'GPU: {card_list}')

          for card in card_list:
               att = card.attributes

               for dev in DEVICE:
                    try:
                         if dev in att.asstring('device'):
                              IGPU_PATH = card.sys_path
                              #print(IGPU_PATH)
                              log.info(f'Found igpu at: {IGPU_PATH}')
                              return IGPU_PATH
                         
                         else:
                              DGPU_PATH = card.sys_path
                              log.info(f'Found dgpu at: {DGPU_PATH}')

                    except:
                        continue

               log.debug(f'Could not find gpu in {DEVICE}. Gpu not supported')
               return 2 
          
     else:
          log.error(f'Could not find GPU')
          return 2

     

