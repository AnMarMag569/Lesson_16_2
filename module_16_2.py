from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()

@app.get("/")
async def root():
    return HTMLResponse("Главная страница")

@app.get("/user/admin")
async def admin_user():
    return HTMLResponse("Вы вошли как администратор")

@app.get("/user/{user_id}")
async def get_user(
        user_id: Annotated[int, Path(..., gt=1, lt=100, title="Enter User ID", examples=1)]):
    return HTMLResponse(f"Вы вошли как пользователь № {user_id}")

@app.get("/user/{username}/{age}")
async def get_user_info(
        username: Annotated[str, Path(..., min_length=5, max_length=20, title="Enter username")],
        age: Annotated[int, Path(..., gt=17, lt=121, title="Enter age")]):

    return HTMLResponse(f"Информация о пользователе. Имя: {username}, Возраст: {age}")


# uvicorn module_16_2:app --reload