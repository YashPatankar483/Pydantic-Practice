from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Optional, Dict, Annotated

# Define Schema for the request body
class Student(BaseModel):

    name: str
    prn: int
    age: Annotated[int, Field(default=3, gt=0, lt=150, description="Enter the age of the student", strict=True)]
    email: EmailStr
    cgpa: float
    subjects: List[str]
    linkedin_url: Optional[AnyUrl] = None
    gender: str
    blood_group: str
    anthropometric_measurements : Dict[str, int]

    @field_validator("email", mode="after")
    @classmethod
    def email_validation(cls, value):
        valid_domains = ["sda.com", "private.com", "sanjveen.com"]

        domain = value.split("@")[-1]

        if domain not in valid_domains:
            raise  ValueError("Domain does not belong to valid school")

        return value

    @model_validator(mode="after")
    def linked_in_required(self):

        if self.age > 18 and self.linkedin_url == None:
            raise ValueError("Linked Account is mandatory")

        return self




student_1 = {'name' : 'yash', 'prn' : '1935', 'age' : 19, 'email' : 'abc@sda.com', 'cgpa' : 9.37, 'subjects' : ['Maths', 'Phy', 'Chem', 'Electronics', 'Eng'], "linkedin_url" : "https://xzz@linkedin.com", 'gender' : 'Male', 'blood_group' : 'O+', 'anthropometric_measurements' : {'height' : 10, 'weight' : 60}}
student_1 = Student(**student_1)
# print(student_1)

def get_student_details(student : Student):

    return student

print(get_student_details(student_1))

student_2 = {'name' : 'ayanokoji', 'prn' : '1435', 'age' : 19, 'email' : 'ayanogmail.com', 'cgpa' : 8.31, 'subjects' : ['Maths', 'Phy', 'Chem', 'Electronics', 'Eng'], 'gender' : 'Male', 'blood_group' : 'A+', 'anthropometric_measurements' : {'height' : 9.9, 'weight' : 58}}
student_2 = Student(**student_2)


