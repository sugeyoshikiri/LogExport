import logging
import logging.config
import time

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

while 1==1:
    logger.info('INFO MESSAGE')
    logger.debug('DEBUG MESSAGE')
    logger.warning('WARNING MESSAGE')
    logger.error('ERROR MESSAGE')
    time.sleep(5)
