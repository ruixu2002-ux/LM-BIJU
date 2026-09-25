#!/bin/sh
# LM BIJU - demo local (macOS / Linux). Uso: ./start-demo.sh [porta]   (por omissão 8080)
cd "$(dirname "$0")" || exit 1
PORT="${1:-8080}"
if command -v python3 >/dev/null 2>&1; then PY=python3
elif command -v python >/dev/null 2>&1; then PY=python
else
  echo "Python não encontrado. Sem Python: extraia demo-showcase-offline.zip e abra LM-BIJU-demo/demo-showcase.html."
  echo "未找到 Python。可以解压 demo-showcase-offline.zip，直接打开 LM-BIJU-demo/demo-showcase.html。"
  exit 1
fi
URL="http://localhost:$PORT/proposals/demo-b.html"
echo ""
echo "  LM BIJU - demo"
echo "  Demo completa:  $URL"
echo "  Apresentação:   http://localhost:$PORT/proposals/demo-showcase.html"
echo "  Ctrl+C para terminar / 按 Ctrl+C 停止"
echo ""
(
  sleep 2
  if command -v open >/dev/null 2>&1; then open "$URL"
  elif command -v xdg-open >/dev/null 2>&1; then xdg-open "$URL" >/dev/null 2>&1
  else echo "  Abra no navegador: $URL"
  fi
) &
exec "$PY" -m http.server "$PORT" --bind 127.0.0.1
