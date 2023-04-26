FROM python:3.11-alpine
LABEL maintainer="Vladislav Yarmak <vladislav-ex-src@vm-0.com>"

COPY . /build
WORKDIR /build
RUN true \
   && apk add --no-cache --virtual .build-deps alpine-sdk libffi-dev openssl-dev cargo \
   && apk add --no-cache libffi \
   && CARGO_NET_GIT_FETCH_WITH_CLI=true pip3 install --no-cache-dir . \
   && apk del .build-deps \
   && true

VOLUME [ "/certs" ]
ENTRYPOINT [ "quickcerts", "-o", "/certs" ]
