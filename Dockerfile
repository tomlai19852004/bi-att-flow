FROM ubuntu:latest
FROM python:3

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN ["python3", "-c", "import nltk; nltk.download('punkt')"]
ENTRYPOINT ["python"]
CMD ["run-demo.py"]