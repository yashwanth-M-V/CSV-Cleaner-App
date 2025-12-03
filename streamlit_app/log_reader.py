from azure_blob import download_blob
from config import LOG_CONTAINER

def read_log(log_path):
    try:
        data = download_blob(LOG_CONTAINER, log_path)
        return data.decode()
    except Exception:
        return "No logs yet..."
