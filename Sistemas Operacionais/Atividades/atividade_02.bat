@echo off
:looprede
ipconfig
set/p valor="testar conectividade com: "
ping %valor%

set/p opcao="deseja continuar? (S/N):"

if "%opcao%"=="S" (
	goto looprede
)