FROM python:3.6

COPY . YEET
WORKDIR YEET

RUN apt update && apt install -y postgresql-client
RUN pip install -r requirements.txt

#CMD chmod +x start.sh && ./start.sh