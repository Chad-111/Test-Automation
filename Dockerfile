# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to the outside world (optional, if you're building a web app)
EXPOSE 80

# Run your Python script by default when the container starts
CMD ["python", "run_tests.py"]
