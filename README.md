# 🐞 Defect Tracking & Management System

A Django-based web application with REST APIs to manage software defects. The system allows developers and testers to collaborate efficiently by reporting, assigning, and resolving defects.

## 🚀 Features
- User management (Developers & Testers linked with Django `User` model)
- Create, update, delete, and filter defects
- Attach and view screenshots of defects
- REST API endpoints for integration with frontend/UI or third-party tools
- Simple UI using Django templates

## 🛠️ Tech Stack
- Python, Django, Django REST Framework
- HTML, CSS, JavaScript
- SQLite (default database)
- Git & GitHub

## ⚡ API Endpoints

**Developers**
- `GET /developers/` → List all developers  
- `POST /developers/` → Add a new developer  

**Testers**
- `GET /testers/` → List all testers  
- `POST /testers/` → Add a new tester  

**Defects**
- `GET /defects/` → List all defects  
- `POST /defects/` → Create new defect  
- `GET /defects/<id>/` → Retrieve defect details  
- `PUT /defects/<id>/` → Update defect  
- `DELETE /defects/<id>/` → Delete defect  

**Screenshots**
- `GET /screenshots/` → List screenshots  
- `POST /screenshots/` → Upload screenshot 
