# Student Management API with FastAPI

A lightweight and extendable API built with FastAPI to manage student records. This project provides basic CRUD (Create, Read, Update, Delete) operations on student data with flexible query and path parameters for efficient data retrieval.

## Features
- **Path Parameters**: Access student data by unique IDs, with built-in validation.
- **Query Parameters**: Search by optional parameters like student names.
- **Validation & Documentation**: Utilizes FastAPI’s `Path` and `Query` features for parameter validation, providing constraints and descriptions directly within API docs.
- **Custom Error Handling**: Returns clear, structured messages for invalid inputs or missing data.

## Endpoints

1. **Root Endpoint**: `GET /` - Returns a "Hello World" message.
2. **All Students**: `GET /all-students` - Retrieves a list of all student records.
3. **Student By ID**: `GET /get-student/{student_id}` - Retrieves student data based on a unique ID.
4. **Student By Name**: `GET /get-student-by-name?name={name}` - Finds student details by name (optional query parameter).
5. **Student Details**: `GET /get-student-details` - Flexible search combining name and a default test parameter. Requires a query parameter for the name.
6. **Combined Path & Query**: `GET /get-student-details/{student_id}` - Search by both ID and optional name, with a default test parameter.
7. **Create Student**: `POST /create-student/{student_id}` - Creates a new student record. Expects a JSON body with student details (name, age, dept).
8. **Update Student**: `PUT /update-student/{student_id}` - Updates an existing student record. Expects a JSON body with any combination of fields (name, age, dept).
9. **Delete Student**: `DELETE /delete-student/{student_id}` - Deletes a student record by ID.

## Getting Started

### Prerequisites
- Python 3.7+
- FastAPI and Uvicorn

### Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-username/student-management-api.git
cd student-management-api
pip install -r requirements.txt
```
### Running the API
Use Uvicorn to start the API server:

```bash
uvicorn main:app --reload
```
Navigate to http://127.0.0.1:8000/docs for interactive API documentation.
