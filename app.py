import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://github.com/theriturajps/TPB-Torrent-Bot-Deploy ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 torrent.py &")
