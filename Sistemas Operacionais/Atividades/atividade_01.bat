@echo off

chcp 65001 >nul

set /p pastaano="escolha o ano: "

mkdir %pastaano%

cd %pastaano%

mkdir "1-janeiro", "2-fevereiro", "3-março","4-abril", "5-maio", "6-junho", "7-julho", "8-agosto", "9-setembro", "10-outubro", "11-novembro", "12-dezembro"