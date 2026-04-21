FROM python:3.11-slim

WORKDIR /app # Set the working directory to /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 # Set environment variables to prevent Python from writing .pyc files and to ensure output is not buffered

COPY requirements.txt . # Copy the requirements.txt file to the working directory

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] # Command to run the FastAPI application using Uvicorn, listening on all interfaces and port 8000