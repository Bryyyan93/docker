DO $$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_database
        WHERE datname = 'notas'
    ) THEN
        CREATE DATABASE notas;
    END IF;
END
$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_roles
        WHERE rolname = 'prueba1'
    ) THEN
        CREATE ROLE prueba1 WITH LOGIN PASSWORD 'example1';
        GRANT ALL PRIVILEGES ON DATABASE notas TO prueba1;
    END IF;
END
$$;

