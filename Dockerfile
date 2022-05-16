##
## Build
##
FROM golang:1.18.2-bullseye AS build

WORKDIR /app

COPY src ./

RUN go build -o /starlink-exporter cmd/starlink-exporter/main.go

##
## Deploy
##
FROM gcr.io/distroless/base-debian11

# For a list of pre-defined annotation keys and value types see:
# https://github.com/opencontainers/image-spec/blob/master/annotations.md
# Note: Additional labels are added by the build workflow.
LABEL org.opencontainers.image.authors="markf+github@geekpad.com"
LABEL org.opencontainers.image.vendor="Geekpad"

WORKDIR /

COPY --from=build /starlink-exporter /starlink-exporter

EXPOSE 9817

USER nonroot:nonroot

ENTRYPOINT ["/starlink-exporter"]
