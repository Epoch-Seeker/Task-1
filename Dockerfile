# Dockerfile
# Base image: Linux with Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and program
COPY requirements.txt requirements.txt
COPY sample_pathway.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the sample program
CMD ["python", "sample_pathway.py"]
