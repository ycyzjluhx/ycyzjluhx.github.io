#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python tests/verify_source.py

if command -v bundle >/dev/null 2>&1 && bundle exec jekyll --version >/dev/null 2>&1; then
  bundle exec jekyll build --trace
  test -f _site/index.html
  for page in research publications grants service news cv contact; do
    test -f "_site/${page}/index.html"
  done
  test -f _site/assets/css/main.css
  test -f _site/assets/img/profile.jpg
  test -f _site/assets/cv/Xusheng_Zhu_CV.pdf
  test -f _site/404.html
  test -f _site/sitemap.xml
  grep -q 'Xusheng Zhu' _site/index.html
  grep -q 'Marie Skłodowska-Curie Actions Postdoctoral Fellow' _site/index.html
  grep -q 'Fluid and Movable Antenna Systems' _site/research/index.html
  grep -q 'IEEE Transactions on Aerospace and Electronic Systems' _site/service/index.html
  grep -q 'AIPIP 2026' _site/service/index.html
  grep -q 'Fluid antenna systems: A geometric approach to error probability and fundamental limits' _site/publications/index.html
  for file in _site/index.html _site/research/index.html _site/publications/index.html _site/grants/index.html _site/service/index.html _site/news/index.html _site/cv/index.html _site/contact/index.html; do
    grep -q 'assets/css/main.css' "$file"
    grep -q 'name="viewport"' "$file"
  done
  echo "JEKYLL BUILD VERIFICATION PASSED"
else
  echo "Jekyll dependencies are unavailable in this environment; skipped generated-site build verification."
  echo "GitHub Actions will run the real Jekyll build on deployment."
fi
