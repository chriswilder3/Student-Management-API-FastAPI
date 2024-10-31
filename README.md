# Student Management API with FastAPI

A lightweight and extendable API built with FastAPI to manage student records. This project provides basic CRUD (Create, Read, Update, Delete) operations on student data with flexible query and path parameters for efficient data retrieval. 

## Features
- **Path Parameters**: Access student data by unique IDs, with built-in validation.
- **Query Parameters**: Search by optional parameters like student names.
- **Validation & Documentation**: Utilizes FastAPI’s `Path` and `Query` features for parameter validation, providing constraints and descriptions directly within API docs.
- **Custom Error Handling**: Returns clear, structured messages for invalid inputs or missing data.

## Endpoints

1. **Root Endpoint**: `GET /` - Returns a "Hello World" message.
2. **Member Search**: `GET /member?name={name}` - Returns a greeting for the provided name.
3. **Student By ID**: `GET /get-student/{student_id}` - Retrieves student data based on a unique ID.
4. **Student By Name**: `GET /get-names?name={name}` - Finds student details by name (optional query parameter).
5. **Custom Search**: `GET /get-details` - Flexible search combining name and custom parameters.
6. **Combined Path & Query**: `GET /get-names/{student_id}?name={name}&test={test}` - Search by both ID and optional name.

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
