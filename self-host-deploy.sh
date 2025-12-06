#!/usr/bin/env bash
set -euo pipefail

HUGO_ENABLEGITINFO=true hugo --gc --minify -b https://grokcv.site/

mkdir -p /var/www/grokcv

rsync -a --delete --exclude='*__.webp' public/ /var/www/grokcv/