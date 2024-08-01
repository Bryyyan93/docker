# Desplegar una ddbb mysql
FROM mysql:9.0.1

RUN chown -R mysql:root /var/lib/mysql/

# Pasar las variables 
ARG MYSQL_DATABASE=paisesdb
ARG MYSQL_USER=pepito
ARG MYSQL_PASSWORD=pepe1234
ARG MYSQL_ROOT_PASSWORD=qwerty123456

# Variables de entorno
ENV MYSQL_DATABASE=$MYSQL_DATABASE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD


COPY init.sql /docker-entrypoint-initdb.d

EXPOSE 3306
