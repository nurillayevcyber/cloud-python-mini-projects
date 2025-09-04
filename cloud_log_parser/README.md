# Cloud Log Parser

A simple Python CLI tool to scan log files and detect suspicious entries such as **unauthorized access attempts** or **failed logins**.

---

## 📌 Features
- Parses any plain-text log file  
- Detects keywords: `unauthorized`, `failed login`  
- Prints line number and log entry for quick analysis  

---

## ⚙️ Usage
```bash
python3 cloud_log_parser.py --file sample_log.txt
