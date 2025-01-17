# Book Management System

A backend project designed to manage book information using **Django**, **MongoDB**, and **Docker**. This project includes a RESTful API for CRUD operations, advanced MongoDB aggregation queries, and is packaged with a `Makefile` to simplify commands.

---

## Features

- **CRUD Operations**: Manage book records (create, read, update, delete).
- **Aggregation Pipeline**: Retrieve the average price of books published in a specific year.
- **Pagination**: REST API responses are paginated for efficiency.
- **Custom Serializers**: Data representation tailored to the needs of the API.
- **Postman Collection**: Includes sample API requests with both success and error cases.
- **Swagger Documentation**: Explore API documentation directly from the browser.

---

## Requirements

- Docker and Docker Compose
- Python 3.10+
- MongoDB (via Docker)

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/JoelBorrero/seek-books-management
cd seek-books-management
```

### 2. Environment Configuration
Copy the example environment variables file and make necessary adjustments:
```bash
cp dev.env .env
```

### 3. Build and Run the Project
For simplified commands, I recommend using Makefile:
```bash
make build    # Build Docker containers
make up       # Start the containers
```
Otherwise, you can run the following commands:
```bash
docker compose build
docker compose up -d
```
Or even simpler:
```bash
docker compose up -d --build
```

### 4. API Endpoints
#### Books API

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/books/ | List all books (paginated) |
| POST | /api/books/ | Create a new book |
| GET | /api/books/<id>/ | Retrieve details of a book |
| PUT | /api/books/<id>/ | Update a book’s details |
| DELETE | /api/books/<id>/ | Delete a book |

Aggregation API

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/books/average-price/ | Get the average price of books published in a year |

### 5. Authentication (Optional)

When implemented, APIs will require a token for access:
- Obtain a token via /api/token/.
- Add the token to the request header: Authorization: Bearer <your_token>.

### 6. Database Population

To populate the database with sample data:
1.	Enter the container shell:
```bash
make shell
```
2.	Run the following script:
```bash
with open('setup/populate_db.py') as f:
    exec(f.read())
```

### 7. Makefile Commands

| Command | Description |
| --- | --- |
| make build | Build Docker containers |
| make up | Start the application in detached mode |
| make down | Stop and remove containers |
| make shell | Access the Django container shell |
| make test | Run unit tests |

### 8. Deployment

Deploy the project on a cloud platform (AWS, GCP, or Azure) using free-tier services. Once deployed:
- Provide the API’s base URL for testing.
- Ensure the environment is configured securely for production.

### 9. Documentation
- Swagger UI: Access interactive API documentation at http://localhost:3000/.
- Postman Collection: Use the included collection to test all endpoints.

### 10. Challenges and Next Steps

#### Completed

- [x] Implementation of aggregation pipelines.
- [x] Modular code structure with reusable components.
- [x] Comprehensive API documentation and example requests.

#### Next Steps
- [ ] Add token-based authentication.
- [ ] Write additional unit tests for aggregation functions.

### Contact
For questions or support:

Name: Joel Borrero

Email: joelborrero@gmail.com

GitHub: https://github.com/JoelBorrero