# HBnB Project - Part 3: Enhanced Backend with Authentication and Database Integration

Welcome to **Part 3** of the HBnB Project!
In this phase, you'll enhance the backend by implementing user authentication, database integration, and persistent storage. You'll also introduce access control for different types of users and prepare the app for real-world deployment.

---

## 🚀 Project Objectives

- **Authentication and Authorization**
  - Implement JWT-based authentication with `Flask-JWT-Extended`
  - Use role-based access control via the `is_admin` attribute
- **Database Integration**
  - Replace in-memory storage with **SQLite** for development
  - Use **SQLAlchemy** as the Object Relational Mapper (ORM)
  - Configure **MySQL** for production use
- **Persistent CRUD Operations**
  - Refactor all create, read, update, delete logic to use persistent storage
- **Database Design & Relationships**
  - Use `mermaid.js` to design and visualize the database schema
  - Ensure correct mapping and relationships between models
- **Data Validation & Consistency**
  - Apply validation and enforce constraints on all model fields

---

## 🎯 Learning Objectives

By completing this part, you will:

- Understand and implement JWT authentication and secure user sessions
- Apply role-based access control to restrict sensitive actions to admins
- Use SQLite with SQLAlchemy to persist application data
- Transition your app to a production-grade RDBMS like MySQL
- Design relational schemas and visualize relationships using `mermaid.js`
- Build a secure, scalable backend API ready for deployment

---

## 🧱 Project Context

In Parts 1 and 2, you used in-memory data structures for development. While fast and simple, they lack persistence and scalability.
In Part 3, you'll transition to a real database using **SQLite** (for local development) and configure the app for **MySQL** in production.

You'll also secure your API with **JWT tokens**, ensuring that only authenticated users can access specific endpoints and that admin-only routes are properly restricted.

---

## 📚 Project Resources

- 🔐 [Flask-JWT-Extended Docs](https://flask-jwt-extended.readthedocs.io/)
- 🛠 [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- 🗃 [SQLite Documentation](https://sqlite.org/docs.html)
- 🧪 [Flask Official Docs](https://flask.palletsprojects.com/)
- 🧩 [Mermaid.js ER Diagrams](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)

---

## 📁 Project Structure & Tasks

### 🔐 Authentication & Authorization
- Modify the `User` model to include a hashed password using `bcrypt`
- Set up JWT authentication using `Flask-JWT-Extended`
- Add role-based access control with `is_admin`

### 🗄 Database Integration & Persistence
- Replace in-memory storage with a **SQLite** backend using `SQLAlchemy`
- Map models: `User`, `Place`, `Review`, and `Amenity`
- Define relationships between entities with SQLAlchemy
- Implement all CRUD endpoints using the database

### 🏗 Production Configuration
- Add environment configuration to toggle between SQLite (dev) and MySQL (prod)
- Prepare for deployment with a MySQL-compatible schema

### 🧬 Database Visualization
- Use `mermaid.js` to create ER diagrams for:
  - Users ↔️ Places
  - Places ↔️ Reviews
  - Places ↔️ Amenities

---

## ✅ Outcome

By the end of Part 3, you will have:

- A **secure**, **authenticated**, and **role-aware** REST API
- A **persistent database layer** using SQLite & SQLAlchemy
- A backend that’s ready for production deployment using MySQL
- A clear understanding of scalable backend systems

---

## 🧪 Quick Setup (for Development)

1. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
