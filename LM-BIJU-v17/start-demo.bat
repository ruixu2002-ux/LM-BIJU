@echo off
setlocal
chcp 65001 >nul
rem LM BIJU - demo local. Uso: start-demo.bat [porta]   (por omissao 8080)
cd /d "%~dp0"
set "PORT=%~1"
if "%PORT%"=="" set "PORT=8080"
set "PY="
py -3 --version >nul 2>&1 && set "PY=py -3"
if not defined PY python --version >nul 2>&1 && set "PY=python"
if not defined PY python3 --version >nul 2>&1 && set "PY=python3"
if not defined PY goto nopy

set "URL=http://localhost:%PORT%/proposals/demo-b.html"
echo.
echo  LM BIJU - demo
echo  Servidor: http://localhost:%PORT%/
echo  Demo completa:  %URL%
echo  Apresentacao:   http://localhost:%PORT%/proposals/demo-showcase.html
echo.
echo  Para terminar, feche esta janela (ou Ctrl+C).
echo  关闭本窗口即可停止演示服务器。
echo.
rem abre o navegador 2 s depois, quando o servidor ja esta a responder
start "" /b cmd /c "ping -n 3 127.0.0.1 >nul & start "" "%URL%""
%PY% -m http.server %PORT% --bind 127.0.0.1
if errorlevel 1 (
  echo.
  echo  Servidor terminado. Se nao chegou a arrancar, a porta %PORT% pode estar ocupada: start-demo.bat 8765
  echo  服务器已停止。如果一开始就没启动成功，可能是端口被占用，请运行：start-demo.bat 8765
  pause
)
goto :eof

:nopy
echo.
echo  Python nao encontrado neste computador.
echo  Sem Python: extraia demo-showcase-offline.zip e faca duplo clique em
echo  LM-BIJU-demo\demo-showcase.html  (funciona sem servidor e sem internet).
echo.
echo  未找到 Python。可以直接解压 demo-showcase-offline.zip，
echo  双击 LM-BIJU-demo\demo-showcase.html 打开（不需要服务器和网络）。
echo  如需安装 Python：https://www.python.org/downloads/
echo.
pause
