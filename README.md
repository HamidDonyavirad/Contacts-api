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

Each contact includes:
- `id` – Unique identifier
- `name` – Full name
- `phone` – Phone number

## 🛠️ Technologies Used

- Python 🐍
- Django 🌐
- Django REST Framework 🔧
- SQLite (default development database)
