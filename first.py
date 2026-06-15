'''from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def hii():
    return {"message":"hello"}'''

from fastapi import FastAPI

from users.main import router as users_router
from person.main import router as person_router
from user_information.main import router as user_info_router

app = FastAPI()

app.include_router(users_router)
app.include_router(person_router)
app.include_router(user_info_router)