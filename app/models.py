from pydantic import BaseModel, Field


# Models
class UserList(BaseModel):
    id: str
    username: str
    email: str
    password: str
    register_date: str


class UserEntry(BaseModel):
    username: str = Field(..., example='Sample username')
    email: str = Field(..., example='sample@gmail.com')
    password: str = Field(..., example='samplepass')


class UserUpdatePw(BaseModel):
    id: str = Field(..., example='Enter your id')
    password: str = Field(..., example='Enter your new password')


class UserDelete(BaseModel):
    id: str = Field(..., example='Enter your id')
