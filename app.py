import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://theriturajps: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@github.com/TPB-Torrent-Bot ok && cd ok && pip3 install -U -r requirements.txt && nohup python torrent.py &")
