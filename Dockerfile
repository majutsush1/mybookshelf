FROM alpine:3.14

RUN apk add --no-cache python3 py3-pip && \
    pip3 install --upgrade pip

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]