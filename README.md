# Task Station
This project involves creating an API for a `Task Management system`. It will include users, tasks, categories, and statuses. Users can manage their tasks by creating, updating, deleting, and marking them as completed.

<br>
<br>
<br>

# Conceptual Data Model
## User
- id (Primary Key)
- username (Unique, String)
- email (Unique, String)
- password (String, hashed for security)
- organization
- designation

### Relationships
- A `User` can have one `UserProfile` **(1-to-1)**.
- A `User` can have multiple `Tasks` **(1-to-Many)**.
- A `User` can create multiple `Categories` **(1-to-Many)**.


## UserProfile
- id (Primary Key)
- bio (Text, optional)
- profile_picture (Image URL or FileField, optional)
- user_id (One-to-One, linked to User)


## Task
- id (Primary Key)
- title (String)
- description (Text, optional)
- due_date (DateTime, optional)
- priority (Enum: Low, Medium, High)
- status (Enum: Pending, In Progress, Completed)
- user_id (Foreign Key to User, required)
- category_id (Foreign Key to Category, optional)

### Relationships
- A `Task` can have multiple `Tags` **(M-to-M)**.


## Category
- id (Primary Key)
- name (String, unique for each user)
- user_id (Foreign Key to User, required)


## Tag
- id (Primary Key)
- name (String, unique)

### Relationships
- A `Tag` can belong to multiple `Tasks` **(M-to-M)**.

<br>
<br>
<br>


# Project Setup
First create a root directory for the project and enter into the directory.

```bash
mkdir TaskStation
cd TaskStation
```

Create a virtual environment and activate it.

```bash
python3 -m venv env
source env/bin/activate
```

Install `django` and `django rest framework`.

```bash
pip install django
pip install djangorestframework
```

Add `requirements.txt` file and include the installed packages.

```bash
pip freeze > requirements.txt
```

Create the `task_station` project.

```bash
django-admin startproject task_station .
```

Go to the `./task_station/settings.py` file and register `'rest_framework'` in the `INSTALLED_APPS` array.

<br>
<br>
<br>


# Database Connection (PostgreSQL)
Install PostgreSQL (if not installed).
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Install `psycopg2` Python Package. Django uses the `psycopg2` library adapter to interact with PostgreSQL. Install it using pip in the virtual environment.
```bash
pip install psycopg2-binary
```

Enter into the PostgreSQL terminal, create database for this project and create a user to access the database.
```sql
CREATE DATABASE task_station;
CREATE USER task_station_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE task_station TO task_station_user;
```

Add the following snippet at `./task_station/settings.py`.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_station',
        'USER': 'task_station_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # Set to empty string for localhost.
        'PORT': '5432',       # Default PostgreSQL port.
    }
}
```

Run migration for the initial migration files.
```bash
python3 manage.py migrate
```

