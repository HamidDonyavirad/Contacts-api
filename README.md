# 📇 Contact API

A simple RESTful API for managing contact information, built with Django and Django REST Framework.

## 🚀 Features

This API supports full CRUD (Create, Read, Update, Delete) operations for managing contacts:

- List all contacts (GET `/contacts/`)
- Retrieve a single contact by ID (GET `/contacts/{id}/`)
- Create a new contact (POST `/contacts/`)
- Update an existing contact (PUT `/contacts/{id}/`)
- Partially update a contact (PATCH `/contacts/{id}/`)
- Delete a contact (DELETE `/contacts/{id}/`)

### 🔎 Additional Features

- **Search** contacts by fullName or numberPhone  
  Example: `GET /contacts/?search=John`

- **Ordering** results by fullName  (ascending or descending)  
  Example: `GET /contacts/?ordering=fullName` 

- **Filtering** by specific fields (e.g., exact name or phone)  
  Example: `GET /contacts/?fullname=Alice` or `GET /contacts/?numberPhone=1234567890`

Each contact includes:
- `id` – Unique identifier
- `fullName` – Full name
- `numberPhone` – Phone number

## 🛠️ Technologies Used

- Python 🐍
- Django 🌐
- Django REST Framework 🔧
- SQLite (default development database)


