from flask import jsonify
from collections import defaultdict

class University:
    def __init__(self,name):
        self.name= name
        self.student_records=defaultdict(dict)

    def receive_grade(self,student_id,course_id,grade):
        self.student_records[student_id][course_id]=grade
        return jsonify({
            "message": f"Grade updated for student {student_id} in {course_id}",  
            "grades": self.student_records[student_id]
            })


