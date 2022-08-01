# main.py
from fastapi import FastAPI, Body
import schemas
app = FastAPI()

fakeDatabase = {
    1: {'task': 'Learn Neo4j'},
    2: {'task': 'Learn Flutter'},
    3: {'task': 'learm Fast Api'}
}

# Get All records


@app.get('/')
def get_all_items():
    return fakeDatabase

# Get single record with specific id


@app.get('/{id}')
def get_single_item(id: int):
    return fakeDatabase[id]

# Adding a record in existing fakeDatabase (Option # 1 | Query Parameter)


@app.post('/addItemThroughQueryParamter')
def add_item_through_query_parameter(task: str):
    newId = len(fakeDatabase)+1
    fakeDatabase[newId] = {'task': task}
    return fakeDatabase

# Adding a record in existing fakeDatabase (Option # 2 | Request Body)


@app.post('/addItemThroughRequestBody')
def add_item_through_request_body(item: schemas.Item):
    newId = len(fakeDatabase)+1
    fakeDatabase[newId] = {'task': item.task}
    return fakeDatabase

# Adding a record in existing fakeDatabase (Option # 3 | Request Body as a Dictionary)


@app.post('/addItemThroughRequestBodyAsDictionary')
def add_item_through_request_body_as_dictionary(body=Body()):
    newId = len(fakeDatabase)+1
    fakeDatabase[newId] = {"task": body}
    return fakeDatabase
