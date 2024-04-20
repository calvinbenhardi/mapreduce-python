# Use an official Python runtime as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run python script
CMD ["python", "main.py"]