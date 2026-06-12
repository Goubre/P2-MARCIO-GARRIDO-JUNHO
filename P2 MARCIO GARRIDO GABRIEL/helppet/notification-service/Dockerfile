FROM python:3.14-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn

EXPOSE 8001

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]