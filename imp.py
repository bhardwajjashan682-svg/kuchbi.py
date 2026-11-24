# from pydantic import BaseModel, Field, EmailStr, field_validator

# class StudentInfo(BaseModel):
#     name: str = Field(description="here the user need")
#     age: int = Field(...,strict=True, gt=0, lt=100)

#     courses: list[str | int]
#     fees: float

#     email: EmailStr

#     @field_validator("email")
#     @classmethod
#     def check_mail(cls, value):
#         if not value.endswith("@tech.com"):
#             raise ValueError("invalid email ")
#         return value

#     def age(self):
#         ...


#     def data(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("courses: ", self.courses)
#         print("fees: ", self.fees)
#         print("email: ", self.email)

# obj = StudentInfo(name="mohit", age=99, courses= ["python", "web dev", "ai", 2121], fees=12.0, email="mohit@texh.com")
# obj.data()
# print(type(obj.age))
# print(type(obj.name))


# from pydantic import BaseModel, Field, EmailStr, field_validator
# class bank(BaseModel):
#     name: str = Field(description="here the user need")
#     age: int = Field(...,strict=True, gt=0, lt=100)

#     account_number: int
#     balance: float

#     email: EmailStr

#     @field_validator("email")
#     @classmethod
#     def check_mail(cls, value):
#         if not value.endswith("@tech.com"):
#             raise ValueError("invalid email ")
#         return value

#     def data(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("account_number: ", self.account_number)
#         print("balance only: ", self.balance )
#         print("email: ", self.email)

# obj = bank(name="jashan", age=99, account_number=123456789, balance=5000000000.0, email="jashan@tech.com")
# obj.data()
