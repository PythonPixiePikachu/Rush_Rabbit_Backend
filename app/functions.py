from fastapi import HTTPException
from app import crud

def create_profile(profile):
    crud.create_profile(profile.user_name, profile.first_name, profile.last_name, profile.email)
    return {"message": "Profile created successfully"}

def read_profile(user_name):
    profile = crud.get_profile(user_name)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile

def update_profile(user_name , profile):
    existing_profile = crud.get_profile(user_name)
    if existing_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")  
    crud.update_profile(user_name, profile.first_name, profile.last_name, profile.email)
    return {"message": "Profile updated successfully"}

def delete_profile(user_name: str):
    if crud.get_profile(user_name) is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    crud.delete_profile(user_name)
    return {"message": "Profile deleted successfully"}