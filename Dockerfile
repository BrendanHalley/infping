FROM golang:latest

WORKDIR /app

RUN apt-get update && apt-get install fping && rm -rf /var/lib/apt/lists/*

COPY infping.go .
COPY config.toml .

RUN go get github.com/influxdata/influxdb1-client
RUN go get github.com/pelletier/go-toml


RUN go build -o main .

CMD ["./main"]
