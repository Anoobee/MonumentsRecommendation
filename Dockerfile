# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install required system packages
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev netcat-openbsd default-mysql-client

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Make sure start.sh is executable
RUN chmod +x /app/start.sh

EXPOSE 8000

CMD ["/app/start.sh"]
