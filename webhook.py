from collections import defaultdict
from flask import jsonify

class WebhookHandler:
    def __init__(self):
        self.webhook_store=defaultdict(list)

    def register_webhook(self,university_id, webhook_url):
        self.webhook_store[university_id].append(webhook_url)
        return jsonify({"message":"Webhook Successfully Registered", "webhook_URL": self.webhook_store.get((university_id),[])})

    def get_all_webhooks(self, university_id):
        return  ({"Registered webhooks": self.webhook_store[university_id]})
