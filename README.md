# Django Blog Application

A blog web application built using **Django** where users can create, edit, delete, and comment on blog posts. The system includes **user authentication and permission-based actions**, ensuring that only logged-in users can manage their own posts.

---

## Features

* User Registration and Login
* Create Blog Posts
* Edit Existing Posts
* Delete Posts (only by logged-in users / post owners)
* Comment on Blog Posts
* View all blog posts on the homepage
* Secure authentication using Django's built-in authentication system

---

## Tech Stack

* Python
* Django
* HTML
* CSS
* SQLite
* Git & GitHub

---

## Project Structure

django-blog-project
│
├── accounts/          # User authentication system
├── blog/              # Blog app logic
├── templates/         # HTML templates
├── db.sqlite3         # SQLite database
└── manage.py          # Django project manager

---

## Installation

1. Clone the repository

git clone https://github.com/vardhan12391/django-blog-project.git

2. Navigate to the project folder

cd django-blog-project

3. Run migrations

python manage.py migrate

4. Start the server

python manage.py runserver

5. Open in browser

http://127.0.0.1:8000/

---

## Usage

1. Register a new account
2. Login to the system
3. Create blog posts
4. Edit or delete your own posts
5. Add comments to posts

---

## Learning Outcomes

This project demonstrates practical experience with:

* Django project structure
* Authentication and authorization
* CRUD operations
* Template rendering
* Database integration using SQLite
* Git and GitHub version control

---

## Author

Laxmi Vardhan
