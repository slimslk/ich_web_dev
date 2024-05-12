from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import Self


class Address(BaseModel):
    city: str = Field(..., min_length=2)
    street: str = Field(..., min_length=3)
    house_number: int = Field(..., ge=0)


class User(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0, lt=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @classmethod
    @field_validator("name")
    def check_name(cls, value: str):
        if not value.isalpha():
            raise ValueError("The name should contains only alphabetic characters")
        return value

    @model_validator(mode="after")
    def check_is_adult(self) -> Self:
        if self.age < 18 and self.is_employed is True:
            raise ValueError("Person with age less than 18 cannot be employees")
        return self


def validate_json_string(json_string: str) -> str:
    user = User.model_validate_json(json_string)
    return user.model_dump_json()


valid_json = """
{ "name": "John",
    "age": 18,
    "email": "john.smith@mymail.com",
    "is_employed": true,
    "address": {
        "city": "London",
        "street": "Baker str.",
        "house_number": 17
    }
}
"""

invalid_json = """
{ "name": "Bo",
    "age": 10,
    "email": "john.smith@mymail.com",
    "is_employed": true,
    "address": {
        "city": "London",
        "street": "Baker str.",
        "house_number": 17
    }
}
"""

valid_user = validate_json_string(valid_json)
print(valid_user)

print("#"*100)

invalid_user = validate_json_string(invalid_json)
print(invalid_user)
