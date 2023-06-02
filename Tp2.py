import threading
import time

# Función que se ejecuta en el hilo 1
def contar_numeros1(contador):
    contador = 1
    while contador<= 10:
        print(f"El hilo 1 comienza en: {contador}")
        contador += 1
        time.sleep(3)

# Función que se ejecuta en el hilo 2
def contar_numeros2(contador):
    contador = 1
    while contador<= 10:
        print(f"El hilo 2 comienza en: {contador}")
        contador += 1
        time.sleep(3)

# Creamos los hilos 1 y 2
hilo1 = threading.Thread(target=contar_numeros1, args=(1,) )
hilo2 = threading.Thread(target=contar_numeros2, args=(1,))
                                                       
                                  

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()
