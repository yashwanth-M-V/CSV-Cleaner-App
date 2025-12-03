import json
from azure.storage.queue import QueueClient
from config import AZURE_STORAGE_CONNECTION_STRING, QUEUE_NAME

queue_client = QueueClient.from_connection_string(
    conn_str=AZURE_STORAGE_CONNECTION_STRING,
    queue_name=QUEUE_NAME
)

def send_job_message(job_id, raw_path, clean_path, log_path):
    message = json.dumps({
        "job_id": job_id,
        "raw_path": raw_path,
        "clean_path": clean_path,
        "log_path": log_path
    })
    queue_client.send_message(message)
