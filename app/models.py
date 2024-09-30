from pydantic import BaseModel

class ProfileCreate(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    email: str
class Profiles(BaseModel):
    first_name: str
    last_name: str
    email: str