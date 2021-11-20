FROM python:3.10

COPY requirements.txt /
RUN pip3 install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 3000
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "entry:app"]