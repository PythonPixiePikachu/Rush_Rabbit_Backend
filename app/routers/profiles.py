from fastapi import APIRouter, HTTPException
from app import crud
from app.models import ProfileCreate, Profiles
from app.functions import create_profile, read_profile,  update_profile, delete_profile


router = APIRouter(
    prefix="/profiles",
    tags=["profiles"]
)

@router.post("/")
def profile_create_api(profile:  ProfileCreate):
    return create_profile(profile)


@router.get("/{user_name}")
def read_profile_api(user_name: str):
    return read_profile(user_name)
    

@router.put("/{user_name}")
def profile_update_api(user_name: str, profile:  Profiles):
    return update_profile(user_name, profile)

@router.delete("/{user_name}")
def profile_delete_api(user_name: str):
    return  delete_profile(user_name)

