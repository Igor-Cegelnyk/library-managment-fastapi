Library Management API
Task
Create a Simple Library Management API

Objective
You should develop a basic library management API using FastAPI and SQLAlchemy ORM with SQLite as the database.

Requirements
Set up the project structure with the following files:
- main.py
- database.py
- models.py
- schemas.py
- crud.py
Set up a SQLite database connection in the database.py file.

Create SQLAlchemy models for 'Author' and 'Book' in the models.py file.

The 'Author' model should have the following fields:

- id (integer, primary key)
- name (string, unique)
- bio (string)
- books (relationship with the 'Book' model, one-to-many)
The 'Book' model should have the following fields:
- id (integer, primary key)
- title (string)
- summary (string)
- publication_date (date)
- author_id (foreign key referencing 'Author' model)
Create Pydantic models for data validation and serialization in the schemas.py file.

Create CRUD utility functions for authors and books in the crud.py file.

In the main.py file, integrate the parts created in previous steps to build the FastAPI application:

Create the database tables using the SQLAlchemy models.
Define the FastAPI application object.
Create a dependency function to manage database sessions.
Implement API endpoints for the following actions:
Create a new author.
Retrieve a list of authors with pagination (skip, limit).
Retrieve a single author by ID.
Create a new book for a specific author.
Retrieve a list of books with pagination (skip, limit).
Filter books by author ID.
Upon completion, you should have a functional library management API that allows the user to manage authors and their books.