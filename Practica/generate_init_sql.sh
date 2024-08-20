#!/bin/sh

# Cargar las variables de entorno
set -e

# Cargar variables de entorno desde el archivo .env
export $(grep -v '^#' ./env_test1.env | xargs)

# Ejecutar comandos de SQL usando las variables de entorno cargadas
DB_EXIST=$(psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -tc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME';")
if [ -z "$DB_EXIST" ]; then
    echo "Creating database $DB_NAME..."
    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "CREATE DATABASE $DB_NAME;"
else
    echo "Database $DB_NAME already exists."
fi

# Comprobar si el rol ya existe
ROLE_EXIST=$(psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -tc "SELECT 1 FROM pg_roles WHERE rolname = '$DB_USER';")
if [ -z "$ROLE_EXIST" ]; then
    echo "Creating role $DB_USER..."
    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<-EOSQL
        CREATE ROLE $DB_USER WITH LOGIN PASSWORD '$DB_PASS';
        GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOSQL
else
    echo "Role $DB_USER already exists."
fi