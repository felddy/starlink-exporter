# starlink-exporter ⭐️🔗🐳 #

[![GitHub Build Status](https://github.com/felddy/starlink-exporter/workflows/build/badge.svg)](https://github.com/felddy/starlink-exporter/actions/workflows/build.yml)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/x/badge)](https://bestpractices.coreinfrastructure.org/projects/x)
[![CodeQL](https://github.com/felddy/starlink-exporter/workflows/CodeQL/badge.svg)](https://github.com/felddy/starlink-exporter/actions/workflows/codeql-analysis.yml)
[![Known Vulnerabilities](https://snyk.io/test/github/felddy/starlink-exporter/badge.svg)](https://snyk.io/test/github/felddy/starlink-exporter)
[![License](https://img.shields.io/github/license/felddy/starlink-exporter)](/LICENSE)
[![Release](https://img.shields.io/github/release/felddy/starlink-exporter.svg)](https://github.com/felddy/starlink-exporter/releases/latest)
![GitHub go.mod Go version](https://img.shields.io/github/go-mod/go-version/felddy/starlink-exporter)
[![Go Report Card](https://goreportcard.com/badge/github.com/felddy/starlink-exporter)](https://goreportcard.com/report/github.com/felddy/starlink-exporter)

## Docker Image ##

[![Docker Pulls](https://img.shields.io/docker/pulls/felddy/starlink-exporter)](https://hub.docker.com/r/felddy/starlink-exporter)
[![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/felddy/starlink-exporter)](https://hub.docker.com/r/felddy/starlink-exporter)
[![Platforms](https://img.shields.io/badge/platforms-amd64%20%7C%20arm%2Fv6%20%7C%20arm%2Fv7%20%7C%20arm64%20%7C%20ppc64le%20%7C%20s390x-blue)](https://hub.docker.com/r/felddy/starlink-exporter/tags)

A [Starlink](https://www.starlink.com/) exporter for Prometheus.

## Running ##

### Running with Docker ###

To run the `felddy/starlink-exporter` image via Docker:

```console
docker run felddy/starlink-exporter:0.0.1
```

### Running with Docker Compose ###

1. Create a `docker-compose.yml` file similar to the one below to use [Docker Compose](https://docs.docker.com/compose/).

    ```yaml
    ---
    version: "3.7"

    services:
      starlink-exporter:
        image: felddy/starlink-exporter:0.0.1
       ports:
          - target: 9817
            published: 9817
            protocol: tcp
    ```

1. Start the container and detach:

    ```console
    docker-compose up --detach
    ```

## Updating your container ##

### Docker Compose ###

1. Pull the new image from Docker Hub:

    ```console
    docker-compose pull
    ```

1. Recreate the running container by following the [previous instructions](#running-with-docker-compose):

    ```console
    docker-compose up --detach
    ```

### Docker ###

1. Stop the running container:

    ```console
    docker stop <container_id>
    ```

1. Pull the new image:

    ```console
    docker pull felddy/starlink-exporter:0.0.1
    ```

1. Recreate and run the container by following the [previous instructions](#running-with-docker).

## Image tags ##

The images of this container are tagged with [semantic
versions](https://semver.org) of the underlying starlink-exporter project that they
containerize.  It is recommended that most users use a version tag (e.g.
`:0.0.1`).

| Image:tag | Description |
|-----------|-------------|
|`felddy/starlink-exporter:1.2.3`| An exact release version. |
|`felddy/starlink-exporter:1.2`| The most recent release matching the major and minor version numbers. |
|`felddy/starlink-exporter:1`| The most recent release matching the major version number. |
|`felddy/starlink-exporter:edge` | The most recent image built from a merge into the `develop` branch of this repository. |
|`felddy/starlink-exporter:nightly` | A nightly build of the `develop` branch of this repository. |
|`felddy/starlink-exporter:latest`| The most recent release image pushed to a container registry.  Pulling an image using the `:latest` tag [should be avoided.](https://vsupalov.com/docker-latest-tag/) |

See the [tags tab](https://hub.docker.com/r/felddy/starlink-exporter/tags) on Docker
Hub for a list of all the supported tags.

## Volumes ##

None

## Ports ##

The following ports are exposed by this container:

| Port | Purpose        |
|------|----------------|
| 9817 | Prometheus web target |

The sample [Docker composition](docker-compose.yml) publishes the
exposed port at 9817.

## Environment variables ##

### Required ###

There are no required environment variables.

### Optional ###

There are no optional environment variables.

## Secrets ##

There are no secrets.

## Building from source ##

Build the image locally using this git repository as the [build context](https://docs.docker.com/engine/reference/commandline/build/#git-repositories):

```console
docker build \
  --build-arg VERSION=0.0.1 \
  --tag felddy/starlink-exporter:0.0.1 \
  https://github.com/felddy/starlink-exporter.git#develop
```

## Cross-platform builds ##

To create images that are compatible with other platforms, you can use the
[`buildx`](https://docs.docker.com/buildx/working-with-buildx/) feature of
Docker:

1. Copy the project to your machine using the `Code` button above
   or the command line:

    ```console
    git clone https://github.com/felddy/starlink-exporter.git
    cd starlink-exporter
    ```

1. Create the `Dockerfile-x` file with `buildx` platform support:

    ```console
    ./buildx-dockerfile.sh
    ```

1. Build the image using `buildx`:

    ```console
    docker buildx build \
      --file Dockerfile-x \
      --platform linux/amd64 \
      --build-arg VERSION=0.0.1 \
      --output type=docker \
      --tag felddy/starlink-exporter:0.0.1 .
    ```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is released as open source under the [GPLv3](LICENSE).

All contributions to this project will be released under the same GPLv3 license.
By submitting a pull request, you are agreeing to comply with this waiver of
copyright interest.
