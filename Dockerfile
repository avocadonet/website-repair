FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY populate_database.py .

RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

CMD ["python", "src/main.py"]