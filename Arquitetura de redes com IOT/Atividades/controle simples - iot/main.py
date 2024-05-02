from machine import Pin, I2C
import time
import machine
import ssd1306

i2c = I2C(0, scl=Pin(14), sda=Pin(12))
led1 = Pin(16, Pin.OUT)
led2 = Pin(17, Pin.OUT)
botao1 = Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
botao2 = Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)

largura = 128
altura = 64

tela = ssd1306.SSD1306_I2C(largura, altura, i2c)
tela.text(" Botao azul ", 0, 21)
tela.text(" ou ", 0, 29,)
tela.text(" Vermelho? ", 0, 38)
tela.show()

while True:
    estado1 = botao1.value()
    estado2 = botao2.value()

    if estado1 == 0:
        led1.value(1)
        time.sleep(0.5)
        led1.value(0)
        tela.fill(0)
        tela.text('temperatura: ', 0, 21)
        tela.text('30', 100, 21)
        tela.show()
    elif estado2 == 0:
        led2.value(1)
        time.sleep(0.5)
        led2.value(0)
        tela.fill(0)
        tela.text('umidade: ', 0, 21)
        tela.text('20', 70, 21)
        tela.show()