from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
from datetime import date
import json
import uuid

app = FastAPI()

class UserRequest(BaseModel):
    last_name: str = Field(..., pattern=r'^[А-ЯЁ][а-яё]+$', description="Фамилия")
    first_name: str = Field(..., pattern=r'^[А-ЯЁ][а-яё]+$', description="Имя")
    birth_date: date
    phone_number: str = Field(..., pattern=r'^\+7\d{10}$', description="Телефон в формате +7XXXXXXXXXX")
    email: EmailStr

@app.post("/user")
def create_user(request: UserRequest):
    try:
        file_name = f"user_{uuid.uuid4().hex}.json"

        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(request.model_dump_json(), f, ensure_ascii=False, indent=4)

        return {"msg": "Заявка успешно сохранена", "file": file_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
