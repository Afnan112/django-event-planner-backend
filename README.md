# 🎯 Django Event Planner Backend

## 📝 Project Description

This is a backend system for an Event Planner application.  
It allows users to:
- Create events
- Register their attendance
- Add important notes for attendees

The goal is to simplify organizing and tracking events efficiently.

---
## ⚙️ Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication (`djangorestframework-simplejwt`)
- PostgreSQL
- `django-cors-headers`
- Postman (for testing APIs)
- GitHub

---

## 🖥️ Frontend Repository
🔗 [react-event-planner-frontend](https://git.generalassemb.ly/afnan07/react-event-planner-frontend)

## 🧠 ERD Diagram
![ERD](./assets/ERD%20event%20planner.png)


## 📬 API Routes
| Method | Endpoint                                        | Description                            |
|--------|--------------------------------------------------|----------------------------------------|
| GET    | `/api/home/`                                     | Home page                              |
| POST   | `/api/signup/`                                   | Register a new user                    |
| POST   | `/api/login/`                                    | Login                                   |
| GET    | `/api/events/`                                   | Get all events                         |
| POST   | `/api/events/add`                                | Create a new event                     |
| GET    | `/api/events/<int:pk>/`                          | Get event details by ID                |
| PATCH  | `/api/events/<int:pk>/`                          | Update event                           |
| DELETE | `/api/events/<int:pk>/`                          | Delete event                           |
| POST   | `/api/events/<int:event_id>/add-attendance/`     | Register user attendance               |
| GET    | `/api/attendance/my-events/`                     | Get events the user registered for     |
| DELETE | `/api/attendance/<event_id>/cancel/`             | Cancel user attendance for an event    |
| GET    | `/api/attendance/<event_id>/attendees/`          | Get attendees of an event              |
| POST   | `/api/events/<int:event_id>/notes/`              | Create a note for the event            |



#### Installation Instructions
1. git clone [my_repo_link](https://git.generalassemb.ly/afnan07/django-event-planner-backend.git)
2. Activate a virtual environment
   pipenv shell
3. Install packages
    pipenv install djangorestframework-simplejwt 
    pipenv install djangorestframework
     pipenv install django-cors-headers
4. Apply migrations
   python manage.py migrate
5. Run runserver

## 🧪 Installation Instructions

1. Clone the repository:  
   ```bash
   git clone https://github.com/Afnan112/django-event-planner-backend.git
   cd django-event-planner-backend
   
#### IceBox Features
- Adding real-time notifications upon attendance registration.
- Add Calender


