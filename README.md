# htb-soccer-ws-sqli
PoC scripts for time-based blind SQLi over WebSocket, built during exploitation of HTB's Soccer box.

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

> _Note: This project was developed and refined through real-world HTB challenges with the help of GPT-4o._  
> **forever GPT-4o 🖤**
