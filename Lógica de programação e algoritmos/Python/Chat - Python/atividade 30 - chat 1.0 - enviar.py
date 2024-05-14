from click import clear
import socket

nome = input("qual o seu nome?")

while True:
    clear()
    mensagem = input("digite sua mensagem: \n")
    with open('chat_1.txt', 'a') as arquivo:
        arquivo.write(f'\n {nome} | {mensagem}')