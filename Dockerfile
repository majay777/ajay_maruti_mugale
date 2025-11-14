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

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=6equj5_root
ENV MYSQL_USER=db_user
ENV MYSQL_DATABASE=home_db
ENV MYSQL_PASSWORD=6equj5_db_user

# Default command
CMD ["bash", "-c", "python read.py && python load_data.py"]