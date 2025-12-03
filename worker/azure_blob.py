from azure.storage.blob import BlobServiceClient
from .config import AZURE_STORAGE_CONNECTION_STRING

blob_service = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

def upload_blob(container, blob_name, data):
    container_client = blob_service.get_container_client(container)
    container_client.upload_blob(blob_name, data, overwrite=True)

def download_blob(container, blob_name):
    container_client = blob_service.get_container_client(container)
    blob = container_client.download_blob(blob_name)
    return blob.readall()

def blob_exists(container, blob_name):
    container_client = blob_service.get_container_client(container)
    return container_client.get_blob_client(blob_name).exists()
