from flask import Flask, render_template
from pymongo import MongoClient
import socket

app = Flask(__name__)
#app.config.from_object('config.Config')
app.config.from_object('config.ProductionConfig')

client = MongoClient(app.config['ATLAS_URI'])
db = client.test
collection = db.tt

@app.route('/')
def index():
    data = collection.find({'_id':1})
    return render_template('index.html', hostname=socket.gethostname(), data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=app.config['DEBUG'])