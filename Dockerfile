# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for the Streamlit app
EXPOSE 8501

# Define environment variable
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]