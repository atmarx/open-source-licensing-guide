FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdocs build

FROM caddy:2-alpine
COPY --from=builder /app/site /srv
COPY Caddyfile /etc/caddy/Caddyfile
EXPOSE 3000
