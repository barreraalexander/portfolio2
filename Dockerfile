FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY .env.sample .env

COPY . .

CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:flask_app"]