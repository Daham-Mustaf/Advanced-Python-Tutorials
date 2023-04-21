# Write a Python script that generates logs for a program. The script should create a log file and write logs to it with different log levels.

import logging

# Set up logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Write logs with different levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Write a Python function that takes a message and log level as arguments, and logs the message with the specified log level using the Python logging module.
def log_message(message, level):
    logging.basicConfig(filename='example.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s: %(message)s')
    if level == 'DEBUG':
        logging.debug(message)
    elif level == 'INFO':
        logging.info(message)
    elif level == 'WARNING':
        logging.warning(message)
    elif level == 'ERROR':
        logging.error(message)
    elif level == 'CRITICAL':
        logging.critical(message)
    else:
        logging.error("Invalid log level: {}".format(level))

# Write a Python script that reads a configuration file for logging and configures the Python logging module accordingly.
import json
import logging.config

# read configuration file
with open('logging_config.json', 'r') as f:
    config = json.load(f)

# configure logging module
logging.config.dictConfig(config)

# log some messages
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

# Write a Python script that uses a custom logger class to log messages to different files based on the log level.
class CustomLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)

        # create handlers for different log levels
        debug_handler = logging.FileHandler('debug.log')
        info_handler = logging.FileHandler('info.log')
        warning_handler = logging.FileHandler('warning.log')
        error_handler = logging.FileHandler('error.log')
        critical_handler = logging.FileHandler('critical.log')

        # set log level for each handler
        debug_handler.setLevel(logging.DEBUG)
        info_handler.setLevel(logging.INFO)
        warning_handler.setLevel(logging.WARNING)
        error_handler.setLevel(logging.ERROR)
        critical_handler.setLevel(logging.CRITICAL)

        # create formatters
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        debug_handler.setFormatter(formatter)
        info_handler.setFormatter(formatter)
        warning_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)
        critical_handler.setFormatter(formatter)

        # add handlers to logger
        self.addHandler(debug_handler)
        self.addHandler(info_handler)
        self.addHandler(warning_handler)
        self.addHandler(error_handler)
        self.addHandler(critical_handler)

if __name__ == '__main__':
    # create custom logger
    logger = CustomLogger(__name__)

    # log messages with different log levels
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

# Write a Python script that reads log files and generates a report with statistics such as the number of log entries, the number of entries at each log level, and the most common log message.
import logging
import os
from collections import Counter

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to read log files and generate statistics
def generate_report(log_dir):
    # Get list of log files in directory
    log_files = [f for f in os.listdir(log_dir) if os.path.isfile(os.path.join(log_dir, f)) and f.endswith('.log')]

    # Initialize counters for log levels and messages
    level_counter = Counter()
    message_counter = Counter()

    # Iterate through log files
    for log_file in log_files:
        # Open log file and read lines
        with open(os.path.join(log_dir, log_file), 'r') as f:
            lines = f.readlines()

        # Iterate through lines and update counters
        for line in lines:
            # Parse log level and message
            parts = line.strip().split(' - ')
            if len(parts) == 3:
                level_str, message = parts[1], parts[2]
                level = logging.getLevelName(level_str)
            else:
                level, message = logging.INFO, line.strip()

            # Update counters
            level_counter[level] += 1
            message_counter[message] += 1

    # Print statistics
    print(f"Number of log entries: {sum(level_counter.values())}")
    print("Log level distribution:")
    for level, count in level_counter.items():
        print(f"{logging.getLevelName(level)}: {count}")
    print("Most common log messages:")
    for message, count in message_counter.most_common(10):
        print(f"{message}: {count}")

# Example usage
generate_report('/Users/m-store/Desktop/ Advanced Python')



