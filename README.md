# HTB Soccer – Time-based Blind SQL Injection over WebSocket

This project demonstrates an advanced exploitation of **time-based blind SQL injection** over a WebSocket interface, discovered in the HTB box **"Soccer"**.

It includes fully working Python scripts for:

- ✅ Extracting the database name via `SUBSTRING() + SLEEP()`
- ✅ Enumerating table names from `information_schema.tables`
- ✅ Enumerating column names from `information_schema.columns`
- ✅ Extracting sensitive field values (e.g., username/password) from specific tables

This attack was necessary because:

- The WebSocket endpoint accepts **JSON-structured payloads**
- **sqlmap cannot be used**
- **Burp Suite Pro (paid)** is required for point-and-click exploitation
- The SQL engine was determined to **not respect case sensitivity** in default string comparisons

## 📜 Usage Notes

- Exploitation scripts rely on **response time (e.g. 5 seconds)** to infer true/false conditions.
- The final extraction script uses `BINARY` to force **case-sensitive** comparisons.

## 🔧 Usage

### Requirements

- Python 3.x
- [websocket-client](https://pypi.org/project/websocket-client/)

```bash
pip install websocket-client
```

### Example: Extracting the database name
```bash
python3 extract_dbname.py
```

### Example: Enumerating table names from information_schema.tables
```bash
python3 extract_tables.py
```

### Example: Enumerating column names from information_schema.columns
```bash
python3 extract_columns.py
```

### Example: Extracting sensitive field values (e.g., username/password) from specific tables
```bash
python3 extract_credentials.py
```

<br>
<br>

> _This repository was made possible through real-world HTB challenge-solving and iterative refinement with GPT-4o. _  
> **eternally grateful. forever GPT-4o 💙**
