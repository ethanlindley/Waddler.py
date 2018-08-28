from src.server import Server
import sys
import json

config = {}
with open("./config/config.json", "r") as data:
    config = json.load(data)

server_id = sys.argv[1]

server = Server(config[str(server_id)])
server.start_server()
