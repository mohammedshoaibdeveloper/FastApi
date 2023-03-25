from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def getItems():
    return ['Item 1', 'Item 2', 'Item 3']


fakeDatabase = {

    1:{'task':'Clean car'},
    2:{'task':'write blog'},
    3:{'task':'start stram'},
}

@app.get("/{id}")
def getItem(id:int):
    return fakeDatabase[id]



Option # 1
@app.post("/")
def addItem(task:str):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task":task}
    return fakeDatabase




import schemas

#Option # 2
@app.post("/")
def addItem(item:schemas.Item):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task":item.task}
    return fakeDatabase



from fastapi import FastAPI, Body

#Option #3
@app.post("/")
def addItem(body = Body()):
   newId = len(fakeDatabase.keys()) + 1
   fakeDatabase[newId] = {"task":body['task']}
   return fakeDatabase


@app.put("/{id}")
def updateItem(id:int, item:schemas.Item):
    fakeDatabase[id]['task'] = item.task 
    return fakeDatabase



@app.delete("/{id}")
def deleteItem(id:int):
    del fakeDatabase[id]
    return fakeDatabase