# Crea una red “test1” y otra “test2”
`docker network create test1`
`docker network create test2`
`docker network ls`
# Crea 2 contenedores (app1 y bbdd1) dentro de la red “test1” y que se pueda hacer ping de  uno a otro con “ping app1” y “ping bbdd1” respectivamente.
`docker run -d --name app1 --network test1 alpine:3.20 sh -c "while true; do sleep 3600; done"`
`docker run -d --name ddbb1 --network test1 alpine:3.20 sh -c "while true; do sleep 3600; done"`
## hacer ping
Para el primer contenedor (172.18.0.3)
```
docker exec -it ddbb1 sh
ifconfig
ping ipapp1 
```
Para el segundo contenedor (172.18.0.3)
```
docker exec -it app1 sh
ifconfig
ping ipddbb1
```
# Crea 2 contenedores (app2 y bbdd2) dentro de la red “test2” y que se pueda hacer ping de  uno a otro con “ping app2” y “ping bbdd2” respectivamente.
`docker run -d --name app2 --network test2 alpine:3.20 sh -c "while true; do sleep 3600; done"`
`docker run -d --name ddbb2 --network test2 alpine:3.20 sh -c "while true; do sleep 3600; done"`
## hacer ping
Para el primer contenedor (172.19.0.3)
```
docker exec -it ddbb1 sh
ifconfig
ping ipapp2 
```
Para el segundo contenedor (172.19.0.2)
```
docker exec -it app1 sh
ifconfig
ping ipddbb2
```
# Los contenedores de “test1” y de “test2” no deben tener conectividad (ping app2 desde app1  no debería de funcionar).
Al comprobar las IP de los contenedores se puede ver que están en rangos IP distintos, por tanto, no van a llegar.
# Borrarlo todo.

# Preguntas:
- ¿Importa mucho conocer las IPs de los propios dockers?
    No necesariamente, se puede hacer un ping usando los nombres de los contenedores.
    No obstante, se debería configurar un rango IP deseado.
    `docker network create --subnet=192.168.100.0/24 test1`
- ¿Cómo saber la IP asignada a un docker? (propón 2 formas).
    * Primera forma
        ```
        docker exec -it app1 sh
        ifconfig
        ```
    * Segunda forma
        `docker exec -it ddbb1 ifconfig` 
    * Para hacer ping
        `docker exec -it app1 ping -c 4 bbdd1` 
- ¿Por qué se pueden resolver los nombres de los contenedores a sus IPs? ¿Qué pasa en la  network "default"?
    La capacidad de Docker para resolver los nombres de los contenedores a sus direcciones IP se debe al sistema de red integrado que proporciona resolución de DNS automática dentro de las redes Docker.

