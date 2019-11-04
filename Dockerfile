FROM ubuntu:latest
MAINTAINER Shikhar Sharma "shikhar.adroit@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN mkdir -p /app
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["GameAPI.py"]