FROM python:3.9-slim

# Install PostgreSQL development packages and clean up after
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Set Python Path environment variable
ENV PYTHONPATH=/app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:80", "app.api:app"]

