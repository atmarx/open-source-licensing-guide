#!/bin/bash
set -euo pipefail

cd /opt/projects/open-source-licensing-guide
mkdir -p caddy

mv _staged/docker-compose.production.yml ./docker-compose.production.yml
mv _staged/open-source-licensing-guide.caddy ./caddy/open-source-licensing-guide.caddy

docker compose -f docker-compose.production.yml pull
docker compose -f docker-compose.production.yml up -d --remove-orphans

cp caddy/open-source-licensing-guide.caddy /opt/caddy-stack/sites/
docker exec caddy caddy reload --config /etc/caddy/Caddyfile

docker image prune -f
echo "Production deployment complete"
