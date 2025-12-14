# Sweet Shop Management System

# Project Overview

The Sweet Shop Management System  is a full-stack web application designed to manage the inventory and sales of sweets in a shop.  
It provides secure user authentication, role-based access control (Admin/User), and real-time inventory management through a modern web interface.

The system is built using a **FastAPI backend** and a **React (SPA) frontend**, connected via RESTful APIs and secured using **JWT-based authentication**.  
The application allows users to browse and purchase sweets, while admin users can manage inventory by adding, updating, restocking, or deleting sweets.

This project demonstrates practical skills in:
- Backend API development
- Authentication & authorization
- Database management
- Frontend SPA development
- Full-stack integration


# Tech Stack

## Backend
- Python
- FastAPI
- SQLite
- SQLAlchemy
- JWT Authentication
- Uvicorn

## Frontend
- React (Vite)
- Axios
- React Router
- CSS
- Javascript

---

# Features

## User Features
- User registration and login
- View all available sweets
- Search and filter sweets
- Purchase sweets (quantity decreases automatically)
- Purchase disabled when stock is zero

## Admin Features
- Add new sweets
- Update sweet details
- Restock sweets
- Delete sweets
- Admin-only access enforced on backend

---

## Project Structure

sweet_shop/
│
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── dependencies.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── seed.py
│   ├── make_admin.py
│   └── sweetshop.db
│
└── frontend/
└── sweet-shop-frontend/
├── src/
├── public/
├── index.html
└── package.json

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies 
pip install fastapi uvicorn sqlalchemy python-jose passlib[bcrypt] python-multipart

# Start backend server
uvicorn main:app --reload
Backend will run at: http://127.0.0.1:8000

# Start frontend
npm run dev
Frontend will run at: http://localhost:5173

# Screenshots
![Login](https://github.com/user-attachments/assets/7a8ef8cd-5e22-4f69-82b9-e17b6eb9a5f2)
![Dashboard](https://github.com/user-attachments/assets/c8e51f16-7976-4af8-bee8-055118d0653f)
![Inventory update](https://github.com/user-attachments/assets/2a5d0e7a-31c3-439a-8c24-c77505ee221a)
![Add_Sweet](https://github.com/user-attachments/assets/829f11b6-0144-4f5b-bb69-473ce0ad4809)


# API Endpoints Summary

## Auth
  •	POST /api/auth/register
	•	POST /api/auth/login
	•	GET /api/auth/me

## Sweets (Protected)
  •	GET /api/sweets
	•	POST /api/sweets (Admin)
	•	PUT /api/sweets/{id}
	•	DELETE /api/sweets/{id} (Admin)
	•	GET /api/sweets/search

## Inventory
  •	POST /api/sweets/{id}/purchase
	•	POST /api/sweets/{id}/restock (Admin)
  
# My AI Usage
Tool- ChatGPT
How I Used ChatGPT:
  •	To debug authentication and authorization issues (JWT, role-based access)
	•	To understand and resolve complex integration bugs between frontend and backend
AI significantly improved my development workflow by acting as a real-time assistant for debugging, architectural decisions, and learning unfamiliar concepts.


# Author

Lupinder Singh Sidhu

