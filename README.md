# URL Shortener using FastAPI and Postgresql

## Prerequisites

Ensure you have the following installed:
- Python 3.11 or higher (for direct setup)
- Docker and Docker Compose (for Docker setup)

## Setup

### 1. Clone the Repository

Clone the repository containing the URL Shortener API:

```bash
git clone https://github.com/Yash114Bansal/FastAPI-Url-Shortner
cd FastAPI-Url-Shortner
```


### 2. Configuration

Create a `.env` file in the project root with the following content:

```python
DATABASE_URL=postgresql+psycopg2://myuser:mypassword@db/mydatabase
POSTGRES_DB=mydatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
```

### 3. Setup Methods

#### Method 1: Direct Setup

1. **Create a Virtual Environment**

   Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```

2. **Install Dependencies**

   Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run Database Migrations**

   Run the Alembic migrations to set up the database schema:

    ```bash
    alembic upgrade head
    ```

4. **Run the Application**

   Start the FastAPI server:

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

   Your application will be available at `http://localhost:8000`.

#### Method 2: Docker Setup

1. **Build and Run Docker Containers**

   Build and start the Docker containers:

    ```bash
    docker compose up --build
    ```

   This command will build the Docker image, start the PostgreSQL container, apply migrations, and run the FastAPI server. The application will be available at `http://localhost:8000`.

## API Endpoints

### 1. Shorten URL

- **Endpoint**: `POST /shorten`
- **Description**: Accepts a long URL and returns a shortened URL.
- **Request Body**:
    ```json
    {
      "original_url": "http://example.com"
    }
    ```
- **Response**:
    ```json
    {
      "original_url": "http://example.com",
      "short_url": "http://localhost:8000/abc123"
    }
    ```

### 2. Redirect to Original URL

- **Endpoint**: `GET /{short_code}`
- **Description**: Redirects to the original URL based on the provided short code.
- **Example Request**: `GET /abc123`
- **Response**: Redirects to the original URL.