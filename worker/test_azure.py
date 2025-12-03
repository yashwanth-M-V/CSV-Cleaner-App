from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv
load_dotenv()

conn = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
blob = BlobServiceClient.from_connection_string(conn)

print("Connected successfully!")
print("Containers:", [c.name for c in blob.list_containers()])
