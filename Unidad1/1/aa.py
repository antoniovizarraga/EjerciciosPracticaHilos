from threading import Thread
from time import sleep
from random import randint


class Hilo(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        self.name = nombre

    def run(self):
        while True:
            print(f"Soy {self.name} y estoy trabajando")
            sleep(randint(1,10))
            print(f"Soy {self.name} y he terminado de trabajar")

if __name__ == "__main__":
    nombres = ["Pepe", "Viyuela", "Amaro", "Pepelu", "Notch"]
    hilos = [Hilo(i) for i in nombres]
    for hilo in hilos:
        hilo.start()