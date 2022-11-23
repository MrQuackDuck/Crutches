FROM python:3.10

# Ensures that the python output streams are sent straight to terminal and you can see the output in real time.
ENV PYTHONUNBUFFERED=1

WORKDIR /docker

# Requirements to install
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Port we're working with
EXPOSE 8000

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]