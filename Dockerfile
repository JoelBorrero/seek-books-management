FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container
COPY . .

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
