FROM python:3-alpine3.12

RUN apk update

RUN apk add gcc
RUN apk add linux-headers
RUN apk add musl-dev
RUN apk add firefox --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

ADD src/ ./src/
ADD drivers/ ./drivers/
ADD snapshots/ ./snapshots/

RUN ls -la /app

CMD ["python", "/app/src/snapshot-test.py"] 
