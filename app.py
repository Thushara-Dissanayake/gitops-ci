from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welocome to the GitOps !!!'