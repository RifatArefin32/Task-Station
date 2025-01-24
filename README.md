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

