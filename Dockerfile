FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your script
COPY src/read.py .
COPY src/schema.sql .
COPY src/load_data.py .
COPY data/fake_property_data_new.json .

# Default command
CMD ["bash", "-c", "python read.py && python load_data.py"]