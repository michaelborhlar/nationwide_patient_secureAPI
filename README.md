# nationwide_patient_secureAPI
An Application Programming Interface that stores and updates all medical data of patient across the country

# Nationwide Patient Secure API

## 📌 Project Overview
The **Nationwide Patient Secure API** is a Django REST Framework project designed to securely manage patient data and medical records across Nigeria.  
It provides role-based access for hospitals, doctors, nurses, and admins, ensuring data privacy and integrity.

---

## ⚙️ Tech Stack
- **Backend**: Django, Django REST Framework  
- **Database**: PostgreSQL  
- **Environment**: Python (Virtualenv / pipenv)  
- **Version Control**: Git & GitHub  

---

## 📂 Features (Planned & Implemented)
- ✅ PostgreSQL database integration  
- ✅ Custom user model with roles (Nurse, Doctor, Admin, SuperAdmin)  
- ✅ Models for State, LGA, Hospital, Patient, Medical Records, Vitals, Access Logs  
- 🔄 Serializers and API endpoints
- 🔄 Authentication & Role-based Permissions
- 🔄 API Deployment on render

---

## 🚀 Getting Started
### 1. Clone the Repository
```bash
git clone https://github.com/michaelborhlar/nationwide_patient_secureAPI.git
cd nationwide_patient_secureAPI

## setting up virtual environment

```bash
pipenv shell

## installing django
pip install django

## installing django rest framework
pip install djangorestframework


# Install JWT Authentication
pip install djangorestframework-simplejwt

# Install PostgreSQL adapter for Django
pip install psycopg2-binary


# Handle Cross-Origin Resource Sharing
pip install django-cors-headers

# For environment variables (instead of hardcoding secrets)
pip install python-decouple

## migrage after creating models
python manage.py makemigrations
python manage.py migrate

For deployment

# Whitenoise for static files
pip install whitenoise

# Gunicorn (WSGI server for deployment)
pip install gunicorn


##for deployment to render
python manage.py collectstatic --noinput

##To save all files so render can make use of them
pip freeze > requirements.txt


web: gunicorn nationwide_patient_secureAPI.wsgi --log-file -
