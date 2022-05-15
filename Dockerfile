##
## Build
##
FROM golang:1.18.2-bullseye AS build

WORKDIR /app

COPY src ./

RUN go mod tidy

RUN go build -o /starlink_exporter cmd/starlink_exporter/main.go

##
## Deploy
##
FROM gcr.io/distroless/base-debian11

WORKDIR /

COPY --from=build /starlink_exporter /starlink_exporter

EXPOSE 9817

USER nonroot:nonroot

ENTRYPOINT ["/starlink_exporter"]