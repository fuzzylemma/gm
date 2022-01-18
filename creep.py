import os
import json
import websocket
import requests

TOKEN = os.environ["DISCORD_BOT"]
GATEWAY_INTENTS_MESSAGES = 513

def send_json_request(ws, request):
    ws.send(json.dumps(request))

def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def retrieve_messages(channel_id):
    headers = {
        "authorization": TOKEN,
    }
    
    r = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100", headers=headers)
    print(r)
    jsonn = json.loads(r.text)
    for value in jsonn:
        #print(value["content"])
        #print(value['timestamp'])
        last = value

    print(last)
    r = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?before={last['id']}&limit=100", headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        #print(value["content"])
        #print(value['timestamp'])
        last = value
    print(last)

    

    print(len(jsonn))

retrieve_messages("869315613187772446")

"""
ws = websocket.WebSocket()
ws.connect("wss://gateway.discord.gg/?v=6&encoding=json")

heartbeat_interval = receive_json_response(ws)["d"]["heartbeat_interval"]
payload = {
    "op": 2,
    "d": {
        "token": TOKEN,
        "intents": GATEWAY_INTENTS_MESSAGES,
        "properties": {
            "$os": "linux",
            "$browser": "chrome",
            "$device": "creeper",
        }
    }
}

send_json_request(ws, payload)
print("scrapping")
while True:
    try:
        event = receive_json_response(ws)
        content = event["d"]["content"]
        author = event["d"]["author"]["username"]
        #if channel_id == "869315613187772446":
        print(f'{author}: {content}')
    except:
        pass
"""
