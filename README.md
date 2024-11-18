# To-Do List API

This is a simple **To-Do List API** built with **Flask**, **PostgreSQL**, and **Docker**. The API allows users to create, retrieve, update, and delete tasks. It is fully containerized using Docker and can be easily deployed.

---

## Features

- RESTful API for managing tasks.
- CRUD operations (Create, Read, Update, Delete).
- PostgreSQL for persistent storage.
- Dockerized for easy setup and deployment.

---

## Installation

### Prerequisites

Make sure you have the following installed on your machine:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Setup Environment Variables

Create a .env file in the root of the project and add the following:

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=mydb
DATABASE_URL=postgresql://user:password@db:5432/mydb

Run the Application
With Docker

    Build and start the containers:

docker-compose up --build

The API will be available at: http://localhost:8080


Endpoints

Here are the available API endpoints:
1. Create a Task

    POST /tasks
    Request Body:

{
  "title": "Learn Flask"
}

Response:

    {
      "id": 1,
      "title": "Learn Flask",
      "completed": false
    }

2. Get All Tasks

    GET /tasks
    Response:

    [
      {
        "id": 1,
        "title": "Learn Flask",
        "completed": false
      }
    ]

3. Update a Task

    PUT /tasks/{id}
    Request Body:

{
  "title": "Master Flask",
  "completed": true
}

Response:

    {
      "id": 1,
      "title": "Master Flask",
      "completed": true
    }

4. Delete a Task

    DELETE /tasks/{id}
    Response:

    {
      "message": "Task deleted"
    }

Development
Run Locally (Without Docker)

    Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt

Start the Flask app:

    python app.py

    Access the API at: http://localhost:8080

Testing
Run Tests with pytest

    Make sure you have pytest installed:

pip install pytest

Run the tests:

    pytest

Deployment
Deploy with Docker

You can deploy this project to platforms like Render or Railway by using the provided Dockerfile and docker-compose.yml.
Project Structure

To-Do/
├── app/
│   ├── __init__.py       # Package initialization
│   ├── models.py         # Database models
│   ├── routes.py         # API routes
│   ├── database.py       # Database configuration
├── tests/
│   ├── test_tasks.py     # Unit tests for the API
├── Dockerfile            # Docker configuration for the web service
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── app.py                # Entry point for the Flask application
└── README.md             # Project documentation

