from threading import Thread


class Hilo(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        self.name = nombre
        self.contador = 0

    def run(self):
        while True:
            if self.contador==0:
                print(f"Soy el hilo {self.name} y voy a empezar mi trabajo")
            else:
                print(f"Soy el hilo {self.name} y he terminado mi hora")

if __name__ == "__main__":
    hilos = [Hilo(i) for i in range(5)]
    for hilo in hilos:
        hilo.start()