# Project Task Description

## Framework and Tools

- Framework: FastAPI  
- Dependency Management: Poetry  
- Database: MongoDB (driver: motor)  
- Message Broker: RabbitMQ  
- Deployment: Docker Compose  

---

## Task Details

### 1. Create a User Model

Create a Pydantic user model with the following attributes:

- id
- first_name
- last_name
- email
- role (one of: admin, dev, `simple mortal`)
- is_active
- created_at
- last_login
- password

---

### 2. Validation Strategy

Define and implement a validation strategy for each field, ensuring:

- Proper data types.
- Constraints like email format, role validation, etc.
- Timestamps for created_at and last_login.

---

### 3. Implement REST API Methods

Using the defined Pydantic model, implement REST API methods to handle user-related operations:

- Create user
- Retrieve user
- Update user
- Delete user

---

### 4. Implement Authentication Middleware

Develop a simple authentication middleware to handle user authentication and role-based access control.

---

### 5. Admin-Restricted Route

Create a route accessible only to users with the admin role. This route should allow updating other users' attributes by their oid (ObjectId), excluding the password field.

---

### 6. Trigger RabbitMQ Message on User Creation

After a user is created, send a message to RabbitMQ to simulate triggering a welcome email sender. Use the following details:

- Routing Key: crm.user.created  
- JSON Body Fields:  
  - id
  - email
  - first_name
  - last_name
  - created_at

---

### 7. Docker-Compose Deployment

Create a docker-compose.yml file to deploy the application, including:

- FastAPI app service.
- RabbitMQ service.
- MongoDB service.

---

### 8. GitHub Submission

Upload the solution to GitHub and provide a link.

---

## Evaluation Criteria

1. Project Structure: Adherence to best practices.
2. PEP8 Compliance: Code follows PEP8 standards.
3. Code Style: Clean and maintainable code.

---

Good luck!