from models.students_model import Students
from utils.connection import db_session


class StudentsService:
    def __init__(self, session):
        self.session = session

    def create_student(self, firstName, lastName, email):
        new_student = Students(first_name=firstName, last_name=lastName, email=email)
        self.session.add(new_student)
        self.session.commit()

        return new_student

    def get_all_students(self):
        return self.session.query(Students).all()
    


    def get_student_by_id(self, student_id):
        return self.session.query(Students).filter_by(id=student_id).first()
    

    # add more filtering

    def update_student(self, student_id, first_name=None, last_name=None, email=None):
        found_student = self.get_student_by_id(student_id)
        if not found_student:
            print("Student was not found")
        if first_name:
            found_student.first_name = first_name
        if last_name:
            found_student.last_name = last_name
        if email:
            found_student.email = email
        self.session.commit()
        return found_student

    def delete_student(self, student_id):
        found_student = self.get_student_by_id(student_id)
        if not found_student:
            return f"Student with id {student_id} has been deleted"

        self.session.delete(found_student)
        self.session.commit()

    def __str__ (self):
        pass

