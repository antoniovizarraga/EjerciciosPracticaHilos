from threading import Event, Thread
from random import randint


class Hilo(Thread):

    numero = randint(0,100)
    evento = Event()

    def __init__(self, nombre):
        Thread.__init__(self)
        self.name = nombre
        self.intento = -1

    def run(self):
            print(f"El hilo {self.name} va a intentar adivinar.")

            while not self.evento.is_set():  # El hilo sigue intentando hasta que se acierte
                self.intento = randint(0, 100)  # Realiza un intento

                if self.intento == Hilo.numero:
                    print(f"¡He acertado! Soy el hilo {self.name}, el número era: {Hilo.numero}, y mi intento fue: {self.intento}.")
                    self.evento.set()  # Señala que el número ha sido adivinado
                else:
                    print(f"Soy {self.name} y no he acertado.")

            # Aquí los hilos terminan cuando se adivina el número
            print(f"Soy el hilo {self.name} y me voy.")


if __name__ == "__main__":
    hilos = [Hilo(i) for i in range(10)]  # Creamos 10 hilos
    for hilo in hilos:
        hilo.start()  # Iniciamos los hilos

    for hilo in hilos:
        hilo.join()  # Esperamos a que todos los hilos terminen