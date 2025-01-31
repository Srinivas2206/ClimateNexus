FROM python:3.9-slim
WORKDIR /app
COPY src/api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/api/ .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]