// Updated using Starlink Dish Firmware Version - 29424243-0ba5-4e9b-b402-79d25cb6f8de.uterm.release

package main

import (
	"fmt"
	"net/http"

	flag "github.com/spf13/pflag"

	"github.com/felddy/starlink-exporter/internal/exporter"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	log "github.com/sirupsen/logrus"
)

const (
	metricsPath = "/metrics"
	version     = "0.0.1"
)

func main() {
	port := flag.String("port", "9817", "listening port to expose metrics on")
	address := flag.String("address", exporter.DishAddress, "IP address and port to reach dish")
	version_flag := flag.Bool("version", false, "Print version and exit")
	flag.Parse()

	if *version_flag {
		fmt.Printf("%s", version)
		return
	}

	exporter, err := exporter.New(*address)
	if err != nil {
		log.Fatalf("could not start exporter: %s", err.Error())
	}
	defer exporter.Conn.Close()
	log.Infof("dish id: %s", exporter.DishID)

	r := prometheus.NewRegistry()
	r.MustRegister(exporter)

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		_, _ = w.Write([]byte(`<html>
             <head><title>Starlink Exporter</title></head>
             <body>
             <h1>Starlink Exporter</h1>
             <p><a href='` + metricsPath + `'>Metrics</a></p>
             <p><a href='/health'>Health (gRPC connection state to Starlink dish)</a></p>
             </body>
             </html>`))
	})

	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		switch exporter.Conn.GetState() {
		case 0, 2:
			// Idle or Ready
			w.WriteHeader(http.StatusOK)
		case 1, 3:
			// Connecting or TransientFailure
			w.WriteHeader(http.StatusServiceUnavailable)
		case 4:
			// Shutdown
			w.WriteHeader(http.StatusInternalServerError)
		}
		_, _ = fmt.Fprintf(w, "%s\n", exporter.Conn.GetState())
	})

	http.Handle(metricsPath, promhttp.HandlerFor(r, promhttp.HandlerOpts{}))
	log.Fatal(http.ListenAndServe(":"+*port, nil))
}
