from threading import Thread, Condition
from random import randint, sample
from time import sleep

class Filosofo(Thread):

    tenedores = [False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre, number):
        Thread.__init__(self)

        self.name = nombre
        self.iteracion = number

    def run(self):

        print(f"El filósofo", self.name, "se sienta en la acogedora mesa.")

        sleep(randint(2,5))

        print(f"Filósofo", self.name, "va a estudiar.")

        sleep(randint(1,10))

        print(f"Filósofo", self.name, "quiere comer. Va a intentar coger sus tenedores.")

        self.tenedor1 = Filosofo.tenedores[(self.iteracion - 1) % 5]

        self.tenedor2 = Filosofo.tenedores[(self.iteracion + 1) % 5]

        Filosofo.cond.acquire()

        while Filosofo.tenedores[(self.iteracion - 1) % 5] == True:
            print("El filósofo", self.name, "está esperando a coger su tenedor 1.")
            Filosofo.cond.wait()
        
        Filosofo.tenedores[(self.iteracion - 1) % 5] = True

        while Filosofo.tenedores[(self.iteracion + 1) % 5] == True:
            print("El filósofo", self.name, "está esperando a coger su tenedor 2.")
            Filosofo.cond.wait()

        Filosofo.tenedores[(self.iteracion + 1) % 5] = True

        Filosofo.cond.release()

        print("El filósofo", self.name, "está comiendo.")
        sleep(randint(1,10))
        print("Filósofo", self.name, "ha terminado de comer.")

        Filosofo.cond.acquire()
        Filosofo.tenedores[(self.iteracion - 1) % 5] = False
        Filosofo.tenedores[(self.iteracion + 1) % 5] = False
        Filosofo.cond.notify_all()

        Filosofo.cond.release()


if __name__ == "__main__":

    nombres = ["Paco", "Alex", "Alejandro", "Da Vinci", "Amaro"]

    # Seleccionamos los nombres sin repetición usando random.sample
    nombres_seleccionados = sample(nombres, len(nombres))

    hilos = [Filosofo(nombres_seleccionados[i], i) for i in range(5)]  # Creamos 5 hilos
    for hilo in hilos:
        hilo.start()  # Iniciamos los hilos

    for hilo in hilos:
        hilo.join()  # Esperamos a que todos los hilos terminen