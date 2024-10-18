import logging
import os
from datetime import datetime

# take date time & create log file
LOG_File = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# create log path
log_path = os.path.join(os.getcwd(), "logs", LOG_File)
# Make directory
os.makedirs(log_path, exist_ok=True)
# Joined log file path
LOG_FILE_PATH = os.path.join(log_path, LOG_File)

# configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
