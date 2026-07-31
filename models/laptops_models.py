from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_models import Base
from utils.uuid_generator import generate_uuid





#creating models -laptop (handson)
class Laptops (Base):
    """Designing A Laptop"""
    __tablename__ = "laptops"

    id = Column(String(60), primary_key=True, default=generate_uuid)
    name = Column(String(60), nullable=False)
    model = Column(String(50), nullable=False)
    student_id = Column(String(50), ForeignKey('Students.id'))

#defining bi directional relationship(1:1)
    students = relationship("Students", back_populates="laptops")




 
def __str__(self):
    return(
        f"Id:{self.id}, Laptop_Name:{self.name}, Model:{self.model}, Owner:{self.student_id}"
    )
