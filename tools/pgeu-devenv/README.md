# Docker based pgeu-devenv

A Docker and docker compose based test setup for the pgeu-system, so
far intended for local development only, not for production use.

## Quickstart

After checking out the pgeu-system repository, a simple `make start` from
the directory this `README.md` lives in will create all required Docker images
and start an instance of the pgeu-system reachable on a browser on
`localhost:8080`.

This creates a bunch of docker images and then launches the entire
composition, including an apache2 reverse proxy, an uwsgi service, a
maintenance container, and of course a Postgres database.

## Persistent Configuration

The docker composition uses a few environment variables for configuration. The
`Makefile` automatically stores these in `env.sh`. To allow direct invocation
of e.g. `docker compose`, it is recommended to source this file, so that
matching settings are used:

```
make
source env.sh
```

Any change to the settings will be registered and (ideally) should trigger a
rebuild of the Docker images, when needed.

Note, however, that the volume with the database is not ever cleared
automatically. To reset everything and start from scratch, simply issue:

```
make clean
```

## Adding a Skin

While the app shows something and the database gets initialized underneath,
it is not very useful without a skin. These usually come in a separate
repository, but can easily be mounted into these docker containers.

Assuming for example the main PGEU skin is to be loaded and a checkout from
the [official repo](https://git.postgresql.org/git/pgeu-web.git) is available,
simply let the environment variable `SKIN_DIR` point to that directory and
re-run `make`:

```
export SKIN_DIR=/home/myself/pgeu-web-checkout
make
source env.sh
```

## Usage

The docker compose file `compose.yaml` is the main part and defines the four
containers: the database (db), the actual Django app (uwsgi), a monitoring
and maintenance component (maintenance), and the frontend webserver (httpd).

A `Makefile` puts together some useful commands and provides short-cuts,
but it's completely fine and reasonable to work with `docker compose`
more directly. Note, however, that some environment variables need to be set
for `docker compose` to work. The `Makfile` conveniently emits the used
configuration to an `env.sh` file to source from. Some example usage:

```sh
# Download required images and assemble Docker images on top. Requires
# the environment variables SETTINGS and SKIN_DIR to be set. Emits the used
# configuration into an env.sh file to later source from.
make

# Start the entire composition in the background.
make start

# Use docker compose directly to check the status of the services.
source env.sh
docker compose ps
docker compose logs uwsgi
docker compose logs maintenance

# Access the underlying database via psql.
source env.sh
docker compose exec maintenance psql

# Watch logs of the composition started in the background.
make logwatch

# Stop all services, delete all volumes, and remove all images built.
make clean
```

## Troubleshooting



## Software Components and Requirements

The web application uses quite a bunch of different Python modules,
some of which seem rather outdated. It's evident it has been developed
for Debian 11 (AKA bullseye) initially and attempts to get it to run
on Debian 12 have not been successful so far.

Note that the uwsgi package is compiled against a specific version of
Python. Thus using the package from the distribution means having to
use the python version of that distribution as well (e.g. Debian 11
comes with Python 3.9). So far, attempts to compile uwsgi from scratch
(to be able to at least use a newer Python version) have not been
fruitful, either.

Below a list of Python modules required compared to the latest version
Debian (12 AKA bookworm and current stable) provides.

| component          | pgeu requirement | current Debian version | comment
| Django             | >=4.2,<4.3       | 3.2.19                 | newest: 5.1.3
| python3-jinja2     | >=2.10,<2.11     | 3.2.1
| python3-markdown   | ==3.0.1          | 3.4.1
| python3-markupsafe | ==1.1.0          | 2.1.1
| Pillow             | ==5.4.1          | n/a
| python3-jwt        | *                | 2.6.0
| argparse           | *                | n/a
| cryptography       | *                | 38.0.4
| fitz               | n/a              | 1.24.10                | renamed to mupdf
| flup               | *                | n/a
| httplib2           | *                | 0.20.4
| psycopg2-binary    | *                | n/a
| pycryptodomex      | 3.6.1            | n/a                    | newest: 3.20.0
| reportlab          | >=3.5.59,<3.7    | 3.6.12                 | newest: 4.2
| python-dateutil    | *                | 3.8.2
| request            | *                | 3.28.1
| request-oauthlib   | ==1.0.0          | 1.3.0
| file-magic         | *                | n/a
