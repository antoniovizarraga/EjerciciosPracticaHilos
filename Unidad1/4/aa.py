from threading import Event, Thread
from random import randint


class Hilo(Thread):

    rutaFichero = "Unidad1/4/texto2.txt"

    def __init__(self, vocal):
        Thread.__init__(self)
        self.intento = -1
        self.letra = vocal
        self.numLetra = 0

    def run(self):
        # open file in read mode
        file = open(Hilo.rutaFichero, 'r')
    
        # store content of the file in a variable
        text = file.read()
    
        # using count()
        numLetra = text.count(self.letra)

        print(f"La letra {self.letra} ha sido encontrada {numLetra} veces.")


if __name__ == "__main__":
    letras = ["a", "e", "i", "o", "u"]
    hilos = [Hilo(i) for i in letras]  # Creamos 10 hilos
    for hilo in hilos:
        hilo.start()  # Iniciamos los hilos

    for hilo in hilos:
        hilo.join()  # Esperamos a que todos los hilos terminen