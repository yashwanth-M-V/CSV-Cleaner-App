import json
import time
import pandas as pd
from azure.storage.queue import QueueClient
from .azure_blob import download_blob, upload_blob
from .cleaner import clean_csv
from .config import (
    AZURE_STORAGE_CONNECTION_STRING,
    RAW_CONTAINER,
    CLEAN_CONTAINER,
    LOG_CONTAINER,
    QUEUE_NAME
)
from dotenv import load_dotenv
load_dotenv()


RAW_CONTAINER = "raw-files"
CLEAN_CONTAINER = "clean-files"
LOG_CONTAINER = "logs"
QUEUE_NAME = "csv-cleaner-queue"


queue_client = QueueClient.from_connection_string(
    conn_str=AZURE_STORAGE_CONNECTION_STRING,
    queue_name=QUEUE_NAME
)

def append_log(log_path, msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp}: {msg}\n"
    upload_blob(LOG_CONTAINER, log_path, line if isinstance(line, bytes) else line.encode())

def process_message(message):
    body = json.loads(message.content)
    raw = body["raw_path"]
    clean = body["clean_path"]
    log_path = body["log_path"]

    append_log(log_path, "Starting job...")

    # Read raw blob
    append_log(log_path, "Reading raw CSV...")
    data = download_blob(RAW_CONTAINER, raw)
    df = pd.read_csv(io.BytesIO(data))

    # Clean CSV
    append_log(log_path, "Cleaning CSV...")
    df = clean_csv(df)

    # Upload cleaned CSV
    append_log(log_path, "Uploading cleaned CSV...")
    upload_blob(CLEAN_CONTAINER, clean, df.to_csv(index=False).encode())

    append_log(log_path, "Job completed successfully!")

while True:
    messages = queue_client.receive_messages()
    for msg in messages:
        process_message(msg)
        queue_client.delete_message(msg)
    time.sleep(2)
