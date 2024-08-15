#!/bin/sh

# Cargar las variables de entorno
set -a
. ./env_test1.env
set +a

# Generar el archivo SQL
cat <<EOF > /docker-entrypoint-initdb.d/init.sql
CREATE DATABASE IF NOT EXISTS $DB_NAME;
CREATE ROLE IF NOT EXISTS $DB_USER WITH LOGIN PASSWORD '$DB_PASS';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
FLUSH PRIVILEGES;
EOF

exec docker-entrypoint.sh postgres