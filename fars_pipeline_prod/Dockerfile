FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project source code into container
COPY fars_pipeline_prod/ /app/fars_pipeline_prod/
COPY FARS2024NationalCSV/ /app/FARS2024NationalCSV/

# Default execution command
CMD ["python", "fars_pipeline_prod/src/train.py"]