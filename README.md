About this project

This is my first public web project under the brand ALTech Technology. It reflects both my growing programming skills and my identity as a digital artist. I created this platform to display my paintings, but also as a practical and elegant project for my programming portfolio.


# Portofoliu Galerie – Django Web Application

This is a Django-based web application built to showcase my personal collection of paintings in a clean, modern and interactive way. The project is part of my journey to become a Full-Stack Developer, combining my passion for art with web development.

---

## *Key Features*

- Art gallery with modal image preview
- Fully functional like and comment system (AJAX-powered, no reload)
- Dark/Light mode toggle in real time
- User authentication with logout button integrated into navbar
- Responsive design for all devices
- Navigation through pages: Home, Gallery, Portfolio, About, Contact

---

## *Tech Stack*

- *Backend*: Django (Python)
- *Frontend*: HTML5, CSS3, JavaScript (AJAX)
- *Database*: SQLite
- *Performance testing*: Locust (tested with 100+ concurrent users)
- *Version control*: Git & GitHub

---

## *Screenshots*
(coming soon)

Will include:
- Art gallery view
- Comment and like system
- Dark/Light theme switching
- Mobile and desktop layouts

---

## *How to run locally*

```bash
git clone https://github.com/Alexandru95py/Portofoliu_Galerie.git
cd Portofoliu_Galerie
python -m venv venv
venv\Scripts\activate     # or source venv/bin/activate on Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Author

Alexandru Goga (aka Alexandru95py)
Self-taught developer & digital artist
Email: alexandru.goga18@gmail.com
