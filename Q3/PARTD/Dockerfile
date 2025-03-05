# Use Python 3.9 as base
FROM python:3.9  

# Set the working directory
WORKDIR /app  

# Create a non-root user
RUN useradd -m myuser  

# Copy application files and set permissions
COPY . .  
RUN chown -R myuser:myuser /app  

# Switch to non-root user
USER myuser  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt  

# Run the application
CMD ["python", "app.py"]
