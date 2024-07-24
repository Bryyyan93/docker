# Crea una imagen que lance el siguiente comando
FROM alpine:3.20

# Instala curl en la imagen
RUN apk add --no-cache curl

# Sobreescribe el comando predeterminado para ejecutar en sh
CMD sh -c 'echo "Input website:"; read website; echo "Searching.."; sleep 1; curl  http://$website;'