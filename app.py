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
    data = collection.find_one({'_id':1})
    data['hostname'] = socket.gethostname()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])