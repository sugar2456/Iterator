FROM python:3.12-slim

WORKDIR /app

RUN adduser --disabled-password --gecos "" user

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

USER user

CMD ["python", "app/main.py"]