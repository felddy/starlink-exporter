##
## Build
##
FROM golang:1.20.0-bullseye AS build

WORKDIR /app

COPY src ./

# Build a static binary
RUN go build -ldflags '-linkmode external -extldflags "-static"' \
    -o /starlink-exporter cmd/starlink-exporter/main.go

##
## Deploy
##
FROM alpine:3.16.2

# For a list of pre-defined annotation keys and value types see:
# https://github.com/opencontainers/image-spec/blob/master/annotations.md
# Note: Additional labels are added by the build workflow.
LABEL org.opencontainers.image.authors="markf+github@geekpad.com"
LABEL org.opencontainers.image.vendor="Geekpad"

WORKDIR /

COPY --from=build /starlink-exporter /starlink-exporter

EXPOSE 9817

ENTRYPOINT ["/starlink-exporter"]
