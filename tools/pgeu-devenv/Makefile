# Adjust to point to the checkout of your "skin", e.g. pgeu-web for the
# PGEU main instance.
SKIN_DIR ?= ./empty-skin

# Adjust to point to a proper settings file. This will get mounted into the
# container as `pgeu_system_settings.py`, so the original file extension does
# not matter.
SETTINGS ?= local_settings.py

POSTGRES_VERSION ?= 17

# Port to expose the app on (via http protocol).
EXP_PORT ?= 8080

SRC := maintenance.py \
	.gen.pgeu_system_settings.py \
	.gen.pgeu_system_override_settings.py \
	Dockerfile.maintenance \
	Dockerfile.httpd \
	Dockerfile.uwsgi \
	uwsgi.ini

all: check-env .stamp.base .stamp.build

SHELL := /bin/bash

# Creates or updates the env.sh file in case some setting given in the
# environment has changed compared to what's in env.sh. This in turn triggers
# regeneration of not just that file, but also of the docker images.
check-env:
	@echo "export SKIN_DIR=${SKIN_DIR}" > env.new
	@echo "export SETTINGS=${SETTINGS}" >> env.new
	@echo "export POSTGRES_VERSION=${POSTGRES_VERSION}" >> env.new
	@echo "export EXP_PORT=${EXP_PORT}" >> env.new
	@if [ ! -f env.sh ] || ! cmp -s env.sh env.new; then			\
		mv env.new env.sh;											\
	else															\
		rm env.new;													\
	fi

# Just triggers the check-env target.
env.sh: check-env

# Generates a settings file activating the skin, if any, and configuring
# a base development instance.
.gen.pgeu_system_settings.py: env.sh
	@echo "Regenerating $@"
	rm -f $@
	@if [ -f ${SETTINGS} ]; then cp ${SETTINGS} $@; fi
	@echo "" >> $@
	@echo "DEBUG = True" >> $@
	@echo "DISABLE_HTTPS_REDIRECTS = True" >> $@
	@echo "SESSION_COOKIE_SECURE = False" >> $@
	@echo "CSRF_COOKIE_SECURE = False" >> $@
	@echo "ALLOWED_HOSTS = [\"*\"]" >> $@
	@echo "SECRET_KEY = 'reallysecretbutwhocares'" >> $@
	@echo "" >> $@
	@echo "SYSTEM_SKIN_DIRECTORY = '/srv/skin'" >> $@
	@echo "STATIC_ROOT = '/srv/static/media'" >> $@

# Generates an override file to "cancel" some settings skins may activate,
# but which aren't usually useful in a development environment.
#
# For now, this always disables PG_COMMUNITY_AUTH and corrects the SITEBASE
# to localhost with the correct port.
.gen.pgeu_system_override_settings.py: env.sh
	@echo "Regenerating $@"
	@rm -f $@
	@echo "ENABLE_PG_COMMUNITY_AUTH = False" >> $@
	@source env.sh && echo "SITEBASE = 'http://localhost:${EXP_PORT}'" >> $@

.stamp.base: env.sh Dockerfile.base
	source env.sh && docker build -f Dockerfile.base -t pgeu-system-python-base:latest .
	@touch $@
# make sure to trigger a rebuild of dependent docker images
	@rm -f .stamp.build

.stamp.build: env.sh .stamp.base ${SRC}
	source env.sh && docker compose build
	@touch $@

start: env.sh .stamp.build
	source env.sh && docker compose up -d --build

stop: env.sh
	source env.sh && docker compose down

logwatch: env.sh
	source env.sh && docker compose logs -f

clean: env.sh
	source env.sh && docker compose down -v
	rm -rf .stamp.base .stamp.build \
			.gen.pgeu_system_settings.py \
			.gen.pgeu_system_override_settings.py

distclean: env.sh
	source env.sh \
		&& docker compose down -v
	rm -rf .stamp.base .stamp.build
	source env.sh && docker rmi \
		pgeu-system-maintenance \
		pgeu-system-uwsgi \
		pgeu-system-httpd \
		pgeu-system-python-base \
		2> /dev/null || /bin/true
	rm -rf env.sh env.new

.PHONY: check-env clean distclean all
