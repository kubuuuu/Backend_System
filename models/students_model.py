from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_models import Base
from utils.uuid_generator import generate_uuid







#creating models -students
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






    def to_dict(self):
        return {
            "student_id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        } 