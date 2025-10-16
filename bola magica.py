

import random

print ("===Bienvenido a la bola magica===")

def iniciar_bola_magica():
    

    while True:
        pregunta = input("Hazme una pregunta y te dire lo que tienes que escuchar")
        if pregunta == "salir":
            print ("===Saliendode la bola magica===")
            break
    else:
        respuestas=[
            "Si.",
            "No.",
            "Tal vez.",
            "Puede ser.",
            "Probablemente.",
            "Quizas.",
            "Es probable.",
            "Es cierto.",
            "No es cierto.",

        ]
        respuesta(f"Mi respuesta es: {respuesta_aleatoria}")

iniciar_bola_magica