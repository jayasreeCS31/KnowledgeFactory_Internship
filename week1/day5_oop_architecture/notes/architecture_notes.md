```markdown
# Software Architecture Notes

## What is Software Architecture?

Software architecture is the structure/design of a software application.
It explains:
- frontend
- backend
- database
- communication flow

---

# Basic Architecture Diagram

User
 ↓
Frontend
 ↓
Backend
 ↓
Database

---

# 1. Frontend

Frontend is the user interface of the application.

Users interact with:
- buttons
- forms
- pages
- menus

Technologies:
- HTML
- CSS
- JavaScript
- React

Responsibilities:
- UI Design
- User interaction
- Sending API requests
- Displaying data

---

# 2. Backend

Backend is the server-side logic of application.

Responsibilities:
- APIs
- Authentication
- Business logic
- Database operations

Technologies:
- Node.js
- Express.js
- Python Flask
- Django

Example APIs:

GET /jobs
POST /login
POST /signup
---
# 3. Database
Database stores application data permanently.

Examples:
- MongoDB
- MySQL
- PostgreSQL

Stores:
- users
- jobs
- applications
- passwords
---
# API (Application Programming Interface)
API acts as communication bridge between frontend and backend.

Example:

Frontend → GET /jobs → Backend

Backend sends jobs data to frontend.
---
# Client-Server Architecture
Client:
- browser
- mobile app

Server:
- backend application

Flow:

Client → Server → Database
---
# Request Flow Example
1. User clicks login
2. Frontend sends request
3. Backend validates data
4. Database checks credentials
5. Backend sends response
6. Frontend displays result
---
# Types of Architecture

## Monolithic Architecture
Everything in one application.

Advantages:
- simple
- beginner-friendly

Disadvantages:
- difficult to scale
---
## Microservices Architecture
Application divided into multiple services.
Examples:
- authentication service
- payment service
- notification service

Advantages:
- scalable
- flexible

Disadvantages:
- complex
---
# Real Project Architecture Example
FarmConnect Architecture:
Frontend
(GitHub Pages)
        ↓
Backend
(Render + Node.js)
        ↓
Database
(MongoDB Atlas)
---
# Professional Backend Structure
backend/
├── routes/
├── controllers/
├── models/
├── middleware/
├── config/
├── server.js
---
# Folder Responsibilities
| Folder | Purpose |
|---|---|
| routes | API routes |
| controllers | business logic |
| models | database schemas |
| middleware | authentication |
| config | database configuration |
---
# Why Architecture is Important
- clean structure
- scalability
- teamwork
- security
- maintainability
---
# Important Terms
| Term | Meaning |
|---|---|
| Frontend | User interface |
| Backend | Server logic |
| Database | Data storage |
| API | Communication bridge |
| Architecture | System design |
---
# Conclusion
Software architecture helps organize applications efficiently and supports scalable software development.