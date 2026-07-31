from fastapi import FastAPI, status, HTTPException, Body
from services.students_services import StudentsService
from utils.connection import db_session

app = FastAPI()

students_service = StudentsService(session=db_session)

@app.get("/")
def home():
     """home route"""
     return {"message:": "Welcome To FastAPI"}

@app.get('/students', status_code=status.HTTP_200_OK)
def fetch_students():
    students = students_service.get_all_students()
    if students:
     results = []
     for student in students:
          results.append(student.to_dict())
     return results
    else:
         raise HTTPException(status_code=404, detail="Students not found")




@app.get("/students/{student_id}", status_code=status.HTTP_200_OK)
def fetch_student_by_id(student_id):
     student = students_service.get_student_by_id(student_id)
     if student:
          return student.to_dict()
     else:
          raise HTTPException(status_code=404, detail="student not found")


@app.post('/students', status_code=status.HTTP_201_CREATED)
def create_student(body : dict = Body(...)):
     new_student = students_service.create_student(
         firstName = body.get("first_name"),
         lastName= body.get("last_name"),
         email = body.get("email")
     )
     return new_student.to_dict()  



@app.put('/students/{student_id}', status_code=status.HTTP_200_OK)
def update_student(student_id: str, body: dict = Body(...)):
     updated_student = students_service.update_student(
        student_id,
        first_name = body.get("first_name"),
        last_name = body.get("last_name"),
        email= body.get("email"),
     )
     return updated_student.to_dict() 

@app.delete('/students/{student_id}', status_code=status.HTTP_200_OK)
def delete_students(student_id: str):
    return{"message": students_service.delete_student(student_id)}


