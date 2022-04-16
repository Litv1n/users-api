from fastapi import FastAPI

import datetime
import uuid
from typing import List
from passlib.context import CryptContext

import db
import models


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


app = FastAPI()


@app.on_event('startup')
async def start_up():
    await db.database.connect()


@app.on_event('shutdown')
async def shutdown():
    await db.database.disconnect()


@app.get('/get-user-list', response_model=List[models.UserList])
async def find_all_users():
    """List all users from api"""
    query = db.users.select()
    return await db.database.fetch_all(query)


@app.post('/create-user', response_model=models.UserList)
async def register_user(user: models.UserEntry):
    """Create a new user with encrypted password and return it"""
    gID = str(uuid.uuid1())
    gDate = str(datetime.datetime.now())
    query = db.users.insert().values(
        id=gID,
        username=user.username,
        email=user.email,
        password=pwd_context.hash(user.password),
        register_date=gDate,
    )

    await db.database.execute(query)
    return {
        'id': gID,
        **user.dict(),
        'register_date': gDate,
    }


@app.get('/search/{userId}', response_model=models.UserList)
async def find_user_by_id(userId: str):
    """Find a unique user"""
    query = db.users.select().where(db.users.c.id == userId)
    return await db.database.fetch_one(query)


@app.put('/update-password', response_model=models.UserList)
async def update_user_pw(user: models.UserUpdatePw):
    """Update instance password"""
    query = db.users.update().where(db.users.c.id == user.id).values(
        password=pwd_context.hash(user.password),
    )
    await db.database.execute(query)

    return await find_user_by_id(user.id)


@app.delete('/delete-user/{userId}')
async def delete_user(user: models.UserDelete):
    query = db.users.delete().where(db.users.c.id == user.id)
    await db.database.execute(query)

    return 'This user has been deleted successfully.'
