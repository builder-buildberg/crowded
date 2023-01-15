FROM python:3.8.13-slim-buster

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "crowded.wsgi:application", "--bind", "0.0.0.0:8000"]
