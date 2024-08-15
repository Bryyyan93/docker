#!/bin/sh

# Cargar las variables de entorno
if [ -f "/docker-entrypoint-initdb.d/env_test1.env" ]; then
    set -a
    . /docker-entrypoint-initdb.d/env_test1.env
    set +a
else
    echo "El archivo env_test1.env no existe."
    exit 1
fi

# Generar el archivo SQL
cat <<EOF > /docker-entrypoint-initdb.d/init.sql
DO \$\$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_database
        WHERE datname = 'notas'
    ) THEN
        CREATE DATABASE notas;
    END IF;
END
\$\$;

DO \$\$;
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_roles
        WHERE rolname = 'prueba1'
    ) THEN
        CREATE ROLE prueba1 WITH LOGIN PASSWORD 'example1';
        GRANT ALL PRIVILEGES ON DATABASE notas TO prueba1;
    END IF;
END
\$\$;
EOF

exec docker-entrypoint.sh postgres