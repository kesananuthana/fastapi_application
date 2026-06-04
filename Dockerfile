FROM python:3.10-slim
WORKDIR /app
copy . .
RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary
CMD ["uvicorn", "first:app", "--host" ,"0.0.0.0", "--port" ,"7000", "--reload"]