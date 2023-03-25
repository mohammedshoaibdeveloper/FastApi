from fastapi import FastAPI

app = FastAPI()

#main.py
from fastapi import FastAPI,Body, Depends
import schemas
import models
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
#This will create our database if it doesent already exists
Base.metadata.create_all(engine)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()



@app.get("/")
def get_Items(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items



@app.post("/")
def add_Item(item:schemas.Item, session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.get("/{id}")
def get_Item(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item

@app.put("/{id}")
def update_Item(id:int, item:schemas.Item, session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject


@app.delete("/{id}")
def delete_Item(id:int, session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item was deleted'