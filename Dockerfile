# Use official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY blockchain_simulation.py /app/blockchain_simulation.py

# Install any required Python packages (none required here, but you can add as needed)
RUN pip install --no-cache-dir -r requirements.txt || true

# Set the default command to run the script
CMD ["python", "blockchain_simulation.py"]
