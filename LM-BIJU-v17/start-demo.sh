#!/bin/sh
# LM BIJU - demo local (macOS / Linux). Uso: ./start-demo.sh [porta]   (por omissão 8080)
cd "$(dirname "$0")" || exit 1
PORT="${1:-8080}"
if command -v python3 >/dev/null 2>&1; then PY=python3
elif command -v python >/dev/null 2>&1; then PY=python
else
  echo "Python não encontrado. Sem Python: extraia lm-biju-demo-offline.zip e abra LM-BIJU-demo/index.html."
  echo "未找到 Python。可以解压 lm-biju-demo-offline.zip，直接打开 LM-BIJU-demo/index.html。"
  exit 1
fi
URL="http://localhost:$PORT/proposals/index.html"
echo ""
echo "  LM BIJU - demo"
echo "  Escolher versão: $URL"
echo "  Demos:          http://localhost:$PORT/proposals/demo-dark.html  |  proposals/demo-light.html"
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
