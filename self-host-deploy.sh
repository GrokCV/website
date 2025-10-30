#!/usr/bin/env bash
set -euo pipefail

hugo --gc --minify -b https://grokcv.site/

mkdir -p /var/www/grokcv

rsync -a --delete public/ /var/www/grokcv/