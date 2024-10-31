import uvicorn # Uvicorn is ASGI webserver necessary for async framework
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel # Pydantic is library for data validation and 
                               # settings management using type annotations.
                               # It creates dataclasses called models, which 
                               # ensure data conforms to specific schema.
                               # It can also convert datatype when possible

app = FastAPI() #instantiate the app


students = {
    1:{
        "name" : "sachin",
        "age" : 26,
        "dept" : "cse"
    }
}

@app.get('/') # route the request on this url to method bound to it
def index():
    return {'message':"Hello World"}

@app.get('/all_students')
def all_students():  
    return students 

# The parameters can be obtained either   
# 1. With Path Parameters (below)

@app.get('/get-student/{student_id}')
def get_student(student_id:int = Path(..., description="The Student ID",ge=1,lt=100)):
    return students[student_id]
    # Path function in FastAPI provides additional validation, metadata, and documentation
    
    # Validation: Path allows you to add constraints to path parameters. 
    # For instance, you can specify that student_id must be a positive integer
    # Ex : Path(..., description="The Student ID you wish to view", ge=1)
    # ge=1 means student_id must be greater than or equal to 1. 
    # If a client tries to access /get-student/-5, a validation error occurs

    # Documentation: When you use Path, the parameter description and 
    # constraints show up in the /docs

# 2. With Query Parameters (below)
    # ex : google.com/results?search=football , Here search=football is query param
    # While Path params are values acting as new endpoints, query params are 
    # key-val pairs given to existing endpoints and are optional.

@app.get('/get-names')
def get_student( name: Optional[str] = None):
    for stud_id in students:
        if students[stud_id]['name'] == name:
            return students[stud_id]

    # Note that by default, name here is accepted as query parameter. So we can 
    # directly feed it in /docs or use http://127.0.0.1:8000/get-names?name=sachin
    # Note that when HTML forms/inputs use GET method, query params are used.

    #  Here, name is defined as an optional parameter with a default 
    # value of None. If the client doesn’t provide a value for name, 
    # it automatically defaults to None.

    # If u dont provide default val say fun(name: Optional[str]) 
    # then FastAPI will interpret this as a required query parameter 
    # due to the absence of a default value

# If we need more than one params at endpt, make sure default 
# values are not passed first.
@app.get('/get-details')
def get_student(*, name: Optional[str] = None, test:str):
    for stud_id in students:
        if students[stud_id]['name'] == name:
            return students[stud_id]
    # The above would have given error if we dont include * as first param

# We can combine Path and Query params.
@app.get('/get-names/{student_id}')
def get_student(*, student_id:int, name : Optional[str] = None, test:str):
    if name is None:
        return {'name_not_given': students[student_id]}
    for stud_id in students:
        if students[stud_id]['name'] == name:
            return {'name_given' : students[stud_id]}
# Above code gives back student details using : 
# 1. student_id if name not given
# 2. stud name if name is given

# Pydantic, Models
class Student(BaseModel):
    name : str
    age : int
    dept : str
    # Note: This class must reflect the schema we want to enforce on student
    # data received, hence is similar to student objects

# Post data to Create New Data
@app.post('/create_student/{student_id}')
def create_student( student_id:int, student: Student): # Student model makes sure
    if student_id in students:                         # data follows student structure
        return {"error":"student Already exists"}
    else:
        students[student_id] = student
        return students[student_id]

# Put method : Update already existing data

# Note that Student model of Pydantic allows only when all fields filled.
# But during we may need to pass only one/few set of values to PUT, not all.
# Hence lets create a new model which takes optionality into consideration

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    dept : Optional[str] = None # Now we can pass only field we need to update

@app.put('/update_student/{student_id}')
def update_student(student_id :int, student: UpdateStudent):
    if student_id not in students:
        return {"Error" : "No such student ID "}
    student = student.dict(exclude_unset = True) # Cant directly iterate on 
                            # model object. So Use dict(), exclude_unset gives
                            # only updated vals. Now student is python dict
    for field,val in student.items():
        students[student_id][field] = val
    return students[student_id]

if __name__ == '__main__':  # Run the app with uvicorn ASGI server
    uvicorn.run(app, host = '127.0.0.1', port=8000)

