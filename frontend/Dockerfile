FROM nginx:alpine

RUN apk add --no-cache openssl && mkdir -p /etc/nginx/ssl

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/nginx/ssl/localhost.key \
  -out /etc/nginx/ssl/localhost.crt \
  -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

COPY nginx-default.conf /etc/nginx/conf.d/default.conf

COPY . /usr/share/nginx/html/

EXPOSE 3000 3001

CMD ["nginx", "-g", "daemon off;"]
