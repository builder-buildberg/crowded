FROM python:3.8.13-slim-buster

RUN pip install --upgrade pip --no-cache-dir

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

WORKDIR /app
COPY . /app


#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "crowded.wsgi:application", "--bind", "0.0.0.0:8000"]
