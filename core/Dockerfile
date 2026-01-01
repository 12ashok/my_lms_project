# Use the official Python image
FROM python:3.11-slim

# Prevent Python from buffering output or writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /code

# Install system dependencies for PostgreSQL and GCC
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /code/

# DIAGNOSTIC: This will print the files during the build log
RUN ls -la /code/manage.py || (echo "ERROR: manage.py not found!" && exit 1)

# Expose the port Django runs on
EXPOSE 8000

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
