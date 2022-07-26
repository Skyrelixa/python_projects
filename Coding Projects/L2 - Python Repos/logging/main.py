import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %M:%M:%S')

# takes our helper module
import helper

# # while you can use this program below, it is better not to use ROOT. We should use a helper.py like above

# # # you can log to 5 different LEVELS. if you run the program as is with logging.debug to logging.critical,
# # # the default is to print above level WARNING

# # logging.debug("This is a debug message")
# # logging.info("This is an info message")
# # logging.warning("This is a warning message")
# # logging.error("This is an error message")
# # logging.critical("This is a critical message")

# # to fix this, we set our defaults...
# # these are available in the python documentation
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %M:%M:%S')

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")