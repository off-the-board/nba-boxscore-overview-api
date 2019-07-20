FROM python:3.7.2-alpine

ENV PYPI_REPO_HOST ec2-52-91-248-99.compute-1.amazonaws.com

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev  && \
    apk add postgresql-dev libffi-dev netcat-openbsd

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app
RUN pip install --upgrade pip && pip install --trusted-host $PYPI_REPO_HOST --extra-index-url http://$PYPI_REPO_HOST:80 -r requirements.txt

RUN chmod +x /usr/src/app/entry-point.sh

CMD ["./entry-point.sh"]
