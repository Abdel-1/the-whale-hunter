# Use an official lightweight Python image as the base
FROM python:3.11-slim

# Environment variables:
# - Don't write .pyc files
# - Don't buffer stdout/stderr (useful for logs)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker layer caching
COPY requirements.txt /app/requirements.txt

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code into the container
COPY src /app/src

# Default command to run our app
CMD ["python", "src/main.py"]

