FROM python:3.9

WORKDIR /app

COPY consumer.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "consumer.py"]
