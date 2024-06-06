FROM python:3.11

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["python3", "/app/main.py"]