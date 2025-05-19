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

#### Front End Repo Link
https://git.generalassemb.ly/afnan07/react-event-planner-frontend

#### ERD diagram
![ERD](./assets/ERD%20event%20planner.png)

#### Routing Table
| Method      | URL                                       | Description                            |
| :---        |    :----:                                 |                                   ---: |
| Get         | api/home                                  | Home page
| POST        | api/signup/                               | Create a new account                   |
| Post        | api/login/                                | Log in                                 |
| Get         | api/events/                               | Get all the events from DB             |
| Post        | api/events/                               | Add a new event                        |
| Get         | api/events/<int:pk>/                      | Display event details based on ID      |
| Patch       | api/events/<int:pk>/                      | Update event                           |
| Delete      | api/events/<int:pk>/                      | Delete event                           |
| POST        | api/events/<int:event_id>/add-attendance/ | Register a user fo revent           |
| Get         | api/attendance/my-events/                 | View user's registered events |
| DELETE      | api/attendance/<event_id>/cancel/         |Cancel user attendance for an event|
| Get         | api/attendance/<event_id>/attendees/      | View attendees of an event for user |
| Post        | api/events/<int:event:_id>/notes          |Create a note for the event  |


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

#### IceBox Features
- Adding real-time notifications upon attendance registration.
- Add Calender


