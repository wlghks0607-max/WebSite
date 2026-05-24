FROM ubuntu

RUN apt-get update
RUN apt-get install python
RUN pip install django

WORKDIR /usr/src/Website/
COPY . /usr/src/Website/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]