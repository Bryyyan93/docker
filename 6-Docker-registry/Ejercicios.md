# Ejercicio 1.6.1
Hacer un log in en docker hub
# Ejercicio 1.6.2
## Descarga una imagen que te apetezca, por ejemplo "nginx"
docker pull nginx:1.26-alpine 
## Ponle un tag con otro nombre
docker tag nginx:1.26-alpine bryyyan/testalpine:v1.1
## Haz push a tu registry en Dockerhub
docker push bryyyan/testalpine:v1.1
