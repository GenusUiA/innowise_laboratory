# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in container
WORKDIR /lecture_6

# Copy the current directory contents into the container at /lecture_6
COPY . /lecture_6

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /lecture_6/requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Rum fastapi.py when the container launches
CMD ["uvicorn", "fastapi_app:app","--host", "0.0.0.0", "--port", "8080"]
