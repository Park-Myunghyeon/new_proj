from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mypost', methods=['GET'])
def mypage():
    pass

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)