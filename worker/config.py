import os
from dotenv import load_dotenv
load_dotenv()

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
RAW_CONTAINER = "raw-files"
CLEAN_CONTAINER = "clean-files"
LOG_CONTAINER = "logs"
QUEUE_NAME = "csv-cleaner-queue"
