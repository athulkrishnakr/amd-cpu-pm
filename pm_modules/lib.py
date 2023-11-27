import socket
import logging

class CustomFormatter(logging.Formatter):
    def format(self, record):
        record.hostname = socket.gethostname()
        return super(CustomFormatter, self).format(record)
    
LOG = '/etc/cpud.log'
log = logging.getLogger()
log.setLevel(logging.DEBUG)

handler = logging.FileHandler(LOG)
handler.setLevel(logging.DEBUG)
formatter = CustomFormatter('%(asctime)s - %(hostname)s - %(levelname)s - %(message)s',
                            datefmt='%b %d %H:%M:%S')
handler.setFormatter(formatter)
log.addHandler(handler)