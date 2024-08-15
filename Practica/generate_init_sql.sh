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

# Esperar a que PostgreSQL esté listo
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$POSTGRES_USER"; do
  echo "Esperando a que PostgreSQL esté listo..."
  sleep 2
done

# Generar el archivo SQL en /tmp
cat <<EOF > /tmp/init.sql
DO \$\$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database
      WHERE datname = '$DB_NAME'
   ) THEN
      CREATE DATABASE $DB_NAME;
   END IF;
END
\$\$;

DO \$\$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_roles
      WHERE rolname = '$DB_USER'
   ) THEN
      CREATE ROLE $DB_USER WITH LOGIN PASSWORD '$DB_PASS';
      GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
   END IF;
END
\$\$;
EOF

# Ejecutar el SQL en la base de datos
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --file=/tmp/init.sql

# Eliminar el archivo temporal
rm -f /tmp/init.sql