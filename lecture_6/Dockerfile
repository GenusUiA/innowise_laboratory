# Official Python parent image
FROM python:3.13.5-slim

# Set working directory in the container
WORKDIR /lecture_6

# Copy the current directory contents into the container at /lecture_6
COPY ./app /lecture_6/app

# Copy dependencies to install them
COPY ./requirements.txt /lecture_6/requirements.txt

# Install any needed dependencies
RUN pip install --no-cache-dir -r /lecture_6/requirements.txt

# Install curl to check the query
RUN apt-get update \ 
 && apt-get install -y curl

# Make port 8000 available
EXPOSE 8000

# Healthecheck to check how it work
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
CMD curl -f http://localhost:8000/healthcheck || exit 1

# Run fastapi_app.py when the container launches
CMD ["uvicorn", "app.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]