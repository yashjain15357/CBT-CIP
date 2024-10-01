# modules/utils.py
import logging
from config.settings import LOG_FILE

def setup_logger():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger('DataMiner')

logger = setup_logger()
