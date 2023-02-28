import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://theriturajps: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@github.com/theriturajps/TPB-Torrent-Bot ok && cd ok && pip3 install -U -r requirements.txt && nohup python torrent.py &")
