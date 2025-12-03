
# 📄 **README.md — CSV Cleaner App (Streamlit + Azure)**

```markdown
# 🧹 CSV Cleaner App  
A zero-cost, cloud-assisted CSV cleaning pipeline using **Streamlit**, **Azure Blob Storage**, **Azure Queue Storage**, and a lightweight Python worker.  
Users can upload CSV files, trigger cloud-based cleaning, monitor logs, and download the cleaned result.

---

## 📌 Features

### **✨ Streamlit App**
- Upload CSV file
- Send file to Azure Blob Storage
- Create a processing job in Azure Queue
- Poll job status
- Display detailed processing logs
- Allow user-selected cleaning options (coming soon)

### **🧼 Cleaning Worker**
- Listens to Azure Queue messages
- Downloads raw CSV
- Executes cleaning steps (dedupe, null handling — extensible)
- Uploads cleaned CSV back to Azure
- Writes real-time logs to `logs/` container

### **☁️ Azure Cloud Storage**
Uses 3 containers:
| Container        | Purpose                           |
|------------------|-----------------------------------|
| `raw-files`      | Stores uploaded source CSV files  |
| `clean-files`    | Stores cleaned CSV outputs        |
| `logs`           | Stores processing log files       |

No backend server required.  
No hosting fees.  
Fully serverless workflow.

---

## 🏗️ Architecture Overview

**Flow:**
1. User uploads CSV file in Streamlit  
2. File stored in Azure Blob (`raw-files/`)  
3. Streamlit pushes job message to Azure Queue  
4. Worker consumes queue message  
5. Worker reads → cleans → writes cleaned file  
6. Worker updates logs in Azure Blob (`logs/`)  
7. Streamlit fetches logs & provides download link  

---

## 🧱 Project Structure

```

csv-cleaner/
│
├── streamlit_app/
│   ├── app.py
│   ├── azure_blob.py
│   ├── azure_queue.py
│   ├── log_reader.py
│   ├── config.py
│   └── utils.py
│
├── worker/
│   ├── worker.py
│   ├── cleaner.py
│   ├── azure_blob.py
│   └── config.py
│
├── requirements.txt
└── README.md

## 🔧 Installation & Setup

### **1. Install Python 3.12**

Download from:
[https://www.python.org/downloads/release/python-3123/](https://www.python.org/downloads/release/python-3123/)

### **2. Create Virtual Environment**

```bash
python3.12 -m venv venv
venv\Scripts\activate   # Windows
````

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Add Azure Credentials**

Create a `.env` file or set OS environment variables:

AZURE_STORAGE_CONNECTION_STRING=your_connection_string

Make sure your Azure Storage account contains:

* Containers:

  * `raw-files`
  * `clean-files`
  * `logs`
* Queue:

  * `csv-cleaner-queue`

---

## 🚀 Running the System

### **1. Start the Streamlit UI**

```bash
cd streamlit_app
streamlit run app.py
```

### **2. Start the Worker**

```bash
cd worker
python worker.py
```

Worker runs continuously, processing queue messages as they arrive.

---

## 🧼 Current Cleaning Steps

(Inside `cleaner.py`)

* Remove duplicate rows
* Replace nulls with `""`

### Future Enhancements

* Null-percentage detection
* Datatype validation
* Column removal logic
* Custom user-selected cleaning rules
* Profiling report
* Data transformations dashboard

---

## 📊 Logs & Monitoring

Each job generates a log file at:

logs/<job_id>.txt

Streamlit fetches and displays logs in real time.

---

## 🛡️ Security Notes

* Use a dedicated Azure Storage SAS token or limited-scope connection string.
* Do NOT commit the connection string to GitHub.
* Restrict access to Blob + Queue resources.

---

## 🤝 Contributing

Contributions are welcome!
To propose improvements, open a PR or create an issue.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🧑‍🎓 Academic / Dissertation Usage

This repository demonstrates:

* Cloud-assisted automation
* Scalable data processing pipeline
* RAG-style architecture (Queue-driven worker + UI)
* Integration of Python, Streamlit, and Azure services

Suitable for dissertations involving:

* Serverless computing
* Data processing pipelines
* Intelligent automation workflows
* Real-time data validation systems

---

## 🙌 Acknowledgments

* Python
* Streamlit
* Azure Storage SDK
* Pandas

## 🎉 DONE

Would you like me to also create:

### ✅ A full **system architecture diagram**

### ✅ A **flowchart** for your dissertation  

### ✅ A **sequence diagram** (UML)  

### ✅ A **setup.ps1** script to automate installation  

### ✅ A **logo/header image** for your GitHub repo  

Just tell me what you want!
