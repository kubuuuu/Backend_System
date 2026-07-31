from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from uuid import uuid4
from dotenv import load_dotenv
import os
from models.base_models import Base
from models.students_model import Students
from models.laptops_models import Laptops






load_dotenv()#loads all enviromental variables

    # building connection string (db_type:driver://username:passwd@localhost:3306/db_name) 
connection_str = os.environ.get("DATABASE_URL")
    #creating an instance of the engine from create_engine

engine = create_engine(connection_str, pool_pre_ping=True)
SessionFactory = sessionmaker(bind=engine) #configuration of session
db_session = SessionFactory()#actual session


def generate_uuid():
     """generated uuids"""
     return str(uuid4())





try:
    with engine.connect() as connection:
        print("successfully connected to data base")
        connection.close()
except Exception as e:
        print(f"failed to connect to the databases:{e}")
        raise e


Base.metadata.create_all(engine)
 










""""
 #creating an instance of declarative base
Base = declarative_base()

 #creating Models

class Students(Base):

    __tablename__ = "Students"

    id = Column(String(50), primary_key=True, default=generate_uuid)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)

    # defining bi directional (1:1 relationship)
    laptops = relationship("Laptops", back_populates="students")



def __str__(self):
    return(
        f"Id:{self.id},FirstName:{self.first_name}, LastName:{self.last_name}, Email:{self.email}"                        
    )

#creating models -laptop (handson)
class Laptops (Base):
    #Designing A Laptop#
    __tablename__ = "laptops"

    id = Column(String(60), primary_key=True, default=generate_uuid)
    name = Column(String(60), nullable=False)
    model = Column(String(50), nullable=False)
    student_id = Column(String(50), ForeignKey('Students.id'))


    students = relationship("Students", back_populates="laptops")


#insertion of laptops

student = db_session.query(Students).first()
jamilas_laptop = Laptops(name="Macbook", model="Macbook Air", student_id=student.id)
db_session.add(jamilas_laptop)
db_session.commit()               

def __str__(self):
    return(
        f"Id:{self.id}, Laptop_Name:{self.name}, Model:{self.model}, Owner:{self.student_id}"
    )


Base.metadata.create_all(engine)
 

#CRUD OPERATIONS WITH ORM


#Insertion
new_students = Students(first_name="Jamila", last_name="Yakubu", email="jamillayaks2001@gmail.com")
new_students_1 = Students(first_name="Jesse", last_name="Debrah", email="jessdebbie2005@gmail.com")
db_session.add(new_students)
db_session.add(new_students_1)
db_session.commit()
#Reading all
results = db_session.query(Students).all()
for result in results:
     print(result)

#readimg by <Criteria>
jamila = db_session.query(Students).filter_by(id=1).first()
print(jamila)
#update
jamila.email = "jamilzzyaks@gmail.com"
jamila.first_name = "mila"
db_session.commit()
print(jamila)
#delete
dummy = db_session.query(Students).filter_by(first_name)
db_session.delete(dummy)
db_session.commit()
"""