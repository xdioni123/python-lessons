from pydantic import BaseModel, FieldValidationInfo,field_validator,constr,conint
from typing import Optional, Union, Any


class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None

    @field_validator('age')
    def age_must_be_positive(cls,v, info:FieldValidationInfo):
        if v <=0:
            raise ValueError('Age must be positive')
        return v
    
#exanple
try:
    users = User(id=1,name="Subaru Natsuki",age=18)
except ValueError as e:
    print(e)

class Adress(BaseModel):
    street:str
    city:str

class another_user(BaseModel):
    id:conint(gt=0) #id me qene ma e madhe se 0
    name:constr(min_length=2,max_length=50) #numri i karakterave te emri duhet te jete me i madh se 2 dhe me i vogel se 50


def get_name(name: Optional[str]= None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())

def process_value(value: Union[int,str]) -> str:
    if isinstance(value, int):
        return f"Number:{value}"
    return f"String:{value}"

print(process_value("Emilia"))

def process_anything(value:Any) -> str:
    return f"Processed {value}"

print(process_anything("asdkjashdaw"))