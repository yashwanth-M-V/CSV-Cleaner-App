import streamlit as st
from azure_blob import upload_blob, blob_exists
from azure_queue import send_job_message
from log_reader import read_log
from config import (
    AZURE_STORAGE_CONNECTION_STRING,
    RAW_CONTAINER,
    CLEAN_CONTAINER,
    LOG_CONTAINER,
    QUEUE_NAME
)
import uuid
import dotenv
dotenv.load_dotenv()


st.title("CSV Cleaner App")

uploaded = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded:
    job_id = str(uuid.uuid4())
    raw_path = f"{job_id}_raw.csv"
    clean_path = f"{job_id}_clean.csv"
    log_path = f"{job_id}.txt"

    # Upload raw file
    upload_blob(RAW_CONTAINER, raw_path, uploaded.getvalue())
    st.success("File uploaded to Azure!")

    # Send queue message
    send_job_message(job_id, raw_path, clean_path, log_path)
    st.info("Job submitted for processing. Please wait...")

    # Section to poll for status
    if st.button("Check Status"):
        if blob_exists(CLEAN_CONTAINER, clean_path):
            st.success("Cleaning complete! Download your file below:")
            data = download_blob(CLEAN_CONTAINER, clean_path)
            st.download_button("Download Clean CSV", data, file_name="cleaned.csv")
        else:
            st.warning("Still processing...")

        # Show logs
        st.subheader("Logs")
        st.text(read_log(log_path))
