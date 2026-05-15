# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expose port
EXPOSE 5000

# Start app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]