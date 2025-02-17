from collections import defaultdict
from webhook import WebhookHandler
from flask import Flask, jsonify,request
import requests

class Acadeum:
    def __init__(self,webhook_handler):
        self.enrollments=defaultdict(dict)
        self.webhook_handler=webhook_handler

    def submit_grade(self,student_id,course_id,grade,university_id):
        self.enrollments[student_id][course_id]=grade

        webhook_urls=self.webhook_handler.get_all_webhooks(university_id)["Registered webhooks"]
        if webhook_urls:
            responses=[]
            for webhook_url in webhook_urls:
                max_retries=1
                delay=2
                for attempt in range(1,max_retries+1):

                    try:
                        response=requests.post(webhook_url,json={"student_id": student_id, "course_id": course_id, "grade": grade},timeout=5)
                        response.raise_for_status()
                        responses.append({"webhook":webhook_url, "status": "Success"})
                        break
                    except requests.exceptions.RequestException as e:
                        if attempt<max_retries:
                            print(f"Retrying ({attempt}/{max_retries}) for webhook: {webhook_url}")
                        else:
                            responses.append({"webhook": webhook_url, "status": "Failed", "error": str(e)})

            return {"message": "Grade submitted, webhooks triggered", "responses": responses}

        return {"message": "Grade submitted, but no webhook found for University A"}