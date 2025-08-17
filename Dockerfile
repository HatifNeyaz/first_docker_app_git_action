# Start from a slim Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

EXPOSE 8501

# Set the command to run the app
CMD ["streamlit", "run", "app.py"]