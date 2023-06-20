from flask import Flask, render_template
from pymongo import MongoClient
import socket
from datetime import datetime
import time

app = Flask(__name__)
#app.config.from_object('config.Config')
app.config.from_object('config.ProductionConfig')

client = MongoClient(app.config['ATLAS_URI'])
db = client.test
collection = db.tt

@app.route('/')
def index():
    nodetype = "SECONDARY"
    hostname = socket.gethostname()
    latency_info = ""
    if (client.is_primary):
        nodetype = "PRIMARY"
        st = time.time()
        collection.insert_one({"text":"Test insert from hostname " + hostname + " at timestamp " + datetime.now().strftime("%d-%m-%Y %H:%M:%S.%f")})
        et = time.time()
        write_time = et-st
        latency_info = "Write latency: " + str(write_time) + "; "
    st = time.time()
    data = collection.find({})
    et = time.time()
    read_time = et-st
    latency_info = latency_info + "Read latency: " + str(read_time)
    return render_template('index.html', hostname=hostname, data=data, nodetype=nodetype, latency_info=latency_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=app.config['DEBUG'])