FROM python:3.9-slim

# Install PostgreSQL development packages
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    apt-get clean

# Set the working directory
WORKDIR /app/app

# Set Python Path
ENV PYTHONPATH=/app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
