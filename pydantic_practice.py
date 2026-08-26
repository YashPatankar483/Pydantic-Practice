from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Optional, Dict


class Student(BaseModel):

    name: str
    prn: int
    age: int
    email: EmailStr
    cgpa: float
    subjects: List[str]
    linkedin_url: Optional[AnyUrl] = None
    gender: str
    blood_group: str
    anthropometric_measurements : Dict[str, int]


student_1 = {'name' : 'yash', 'prn' : '1935', 'age' : 19, 'email' : 'abc@gmail.com', 'cgpa' : 9.37, 'subjects' : ['Maths', 'Phy', 'Chem', 'Electronics', 'Eng'], 'gender' : 'Male', 'blood_group' : 'O+', 'anthropometric_measurements' : {'height' : 10, 'weight' : 60}}
student_1 = Student(**student_1)
# print(student_1)

def get_student_details(student : Student):

    return student

print(get_student_details(student_1))

student_2 = {'name' : 'ayanokoji', 'prn' : '1435', 'age' : 19, 'email' : 'ayanogmail.com', 'cgpa' : 8.31, 'subjects' : ['Maths', 'Phy', 'Chem', 'Electronics', 'Eng'], 'gender' : 'Male', 'blood_group' : 'A+', 'anthropometric_measurements' : {'height' : 9.9, 'weight' : 58}}
student_2 = Student(**student_2)


