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
- 🔄 Serializers and API endpoints (in progress)  
- 🔄 Authentication & Role-based Permissions (upcoming)  
- 🔄 API Deployment (upcoming)  

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
pip install djago

## installing django rest framework
pip install djangorestframework