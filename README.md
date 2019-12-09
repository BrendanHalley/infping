# infping
Parse fping output, store results in influxdb

See blog post for more info https://hveem.no/visualizing-latency-variance-with-grafana

Simply run :
```go
go get github.com/influxdata/influxdb/client
go get -d github.com/BrendanHalley/infping
```
Edit the config.toml file and add the retention policy in infping.go then

```go
go install github.com/BrendanHalley/infping
go run bin/infping
```

# Additional Info

I don't code in Go, best practice may not have been followed. Changes I've made here are to get a PoC working, which is does.
