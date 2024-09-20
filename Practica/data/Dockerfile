FROM postgres:13-alpine

WORKDIR /data

# Copiar los archivos

ARG POSTGRES_PASSWORD: qwerty
ARG POSTGRES_USER: superadmin

COPY db_data /var/lib/postgresql/data
COPY generate_init_sql.sh /docker-entrypoint-initdb.d/generate_init_sql.sh
COPY env_test1.env /docker-entrypoint-initdb.d/env_test1.env
