from flask import Flask,request, jsonify
import requests
from collections import defaultdict
from University import University
from webhook import WebhookHandler
from acadeum import Acadeum

app=Flask(__name__)

webhook_handler=WebhookHandler()
uni=University('University A')
acadeum = Acadeum(webhook_handler) 

    
@app.route('/register_webhooks',methods=['POST'])
def register_webhook():
    data=request.json
    return (webhook_handler.register_webhook(data['university_id'],data['webhook_url'])),200

@app.route('/get_webhooks/<university_id>',methods=['GET'])
def get_webhooks(university_id):
    return webhook_handler.get_all_webhooks(university_id),200

@app.route('/receive_grade', methods=['POST'])
def receive_grade():
    data=request.json
    return uni.receive_grade(data['student_id'],data['course_id'],data['grade'])

@app.route('/submit_grade', methods=['POST'])
def submit_grade():
    data = request.json
    return jsonify(acadeum.submit_grade(data['student_id'], data['course_id'], data['grade'], data['university_id'])), 200

if __name__=='__main__':
    app.run(port=5000,debug=True)
