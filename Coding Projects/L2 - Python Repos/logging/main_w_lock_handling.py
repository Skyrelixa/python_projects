import logging

logger = logging.getLogger(__name__)

# Create handler, can send logs to destinations
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# setting level and format of handlers
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

# assigning format to handlers
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# adding handlers to logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

# logger messages
logger.warning("This is a warning")
logger.error("This is an error")