# Use official Python image
FROM python:3.9
# Set working directory
WORKDIR /app
# Copy files to the container
COPY . .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose port 5000
EXPOSE 5000
# Run Flask app
CMD ["python", "2ndapp.py"]
