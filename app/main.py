from fastapi import FastAPI
from app.routers import profiles

app = FastAPI()


app.include_router(profiles.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Profile Management System"}
