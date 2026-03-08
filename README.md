<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/4149/4149692.png" width="100" height="100" alt="Cloud Icon">
</p>

<h1 align="center">CLOUD — Modern Cloud Storage</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue">
  <img src="https://img.shields.io/badge/Django-4.2-green">
  <img src="https://img.shields.io/badge/License-MIT-orange">
</p>

<p align="center">
  A clean, modern cloud storage application built with Django. Store, manage and organize your files with an intuitive interface.
</p>

---

## Features

| Feature | Description |
|---------|-------------|
| Folders | Create and organize files in folders |
| Upload | Easy file upload |
| Favorites | Mark important files |
| Trash | Soft delete with restore option |
| Search | Quick file search |
| Responsive | Works on all devices |

---

## Tech Stack

- Backend: Django 4.2
- Database: SQLite
- Frontend: HTML5, CSS3, JavaScript
- Icons: Font Awesome
- Font: Google Fonts (Inter)

---

## Quick Start

### 1. Clone repository
git clone https://github.com/yourusername/cloud.git
cd cloud

2. Create virtual environment
bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3. Install dependencies
bash
pip install -r requirements.txt

4. Apply migrations
bash
python manage.py migrate

5. Create superuser
bash
python manage.py createsuperuser

6. Run server
bash
python manage.py runserver

7. Open browser
http://127.0.0.1:8000

Project Structure
cloud/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── mycloud/
│   └── settings.py
└── storage/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── admin.py
    └── templates/
        └── storage/
            └── index.html
            
Contributing
Feel free to fork and improve.

License
MIT License — free for personal and commercial use

<p align="center"> Star this repo if you like it. </p> ```