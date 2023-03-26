FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the contents in requirements.txt
COPY requirements.txt .

# Install the necessary packages
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /dao-ocr
COPY . /app

# Expose port 5000 for the Flask app
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
