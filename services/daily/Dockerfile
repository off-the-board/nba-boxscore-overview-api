FROM python:3.7.2-alpine

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev  && \
    apk add netcat-openbsd

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install dependencies/*.gz

RUN chmod +x /usr/src/app/entry-point.sh

CMD ["./entry-point.sh"]
