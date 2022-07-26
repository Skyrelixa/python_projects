import logging

logger = logging.getLogger(__name__)            # this names the logger helper

# propagation False hides logging messages from helper
logger.propagate = False
logger.info('Hello from helper!')