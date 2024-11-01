from microbit import *
import radio
import random

# Configuración inicial de la radio
radio.on()
radio.config(channel=7)

# Variables globales
puntos = 0
rondas = 0
mi_carta = 0

def asignar_carta():
    global mi_carta
    mi_carta = random.randint(1, 10)  # Valores aleatorios del 1 al 10
    display.show(str(mi_carta))

def enviar_mensaje(mensaje):
    radio.send(mensaje)

def recibir_mensaje():
    return radio.receive()

def manejar_mensaje(mensaje):
    global puntos
    if mensaje == "truco":
        display.show("T")
        sleep(1000)
        if button_a.is_pressed():
            enviar_mensaje("aceptar")
        else:
            enviar_mensaje("rechazar")
    elif mensaje == "quiero":
        display.show("Q")
        sleep(1000)
        if button_a.is_pressed():
            puntos += 1
            enviar_mensaje("aceptado")
        else:
            enviar_mensaje("rechazado")

def mostrar_puntos():
    display.scroll("Puntos: " + str(puntos))

# Bucle principal
while True:
    if button_b.was_pressed():
        asignar_carta()
        enviar_mensaje("truco")
    
    mensaje_recibido = recibir_mensaje()
    if mensaje_recibido:
        manejar_mensaje(mensaje_recibido)
    
    if button_a.was_pressed() and not mensaje_recibido:
        enviar_mensaje("quiero")
    
    mostrar_puntos()
    sleep(2000)
