FROM alpine:3.20

RUN apk add --no-cache bash

CMD [ "bash", "-c", "c=0; while true; do echo $c; sleep 1; let c++; done" ]

