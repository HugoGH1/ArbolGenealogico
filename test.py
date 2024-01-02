import os
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izquierdo = None
        self.derecho = None

    def agregar_hijo(self, hijo):
        if self.izquierdo is None:
            self.izquierdo = hijo
        elif self.derecho is None:
            self.derecho = hijo
        else:
            raise ValueError("El nodo ya tiene dos hijos, no es posible agregar más")

contador_nodos = 0
niveles = []
def incrementar_contador_nodos():
    global contador_nodos
    contador_nodos += 1

def obtener_contador_nodos():
    return contador_nodos

def obtener_numero_valido(pregunta, opciones_validas):
    while True:
        try:
            numero = int(input(pregunta))
            if numero in opciones_validas:
                return numero
            else:
                print("Número no válido. Introduce un número válido.")
        except ValueError:
            print("Error: Introduce un número entero válido.")

def nombre_valido(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isalpha():
            return entrada
        else:
            print("Por favor, ingresa un nombre válido.")

def mostrar_arbol(nodo, nivel=0):
    if nivel == len(niveles):
        niveles.append(0)
    niveles[nivel] += 1
    print("  " * nivel + nodo.nombre)
    if nodo.izquierdo is not None:
        mostrar_arbol(nodo.izquierdo, nivel + 1)
    if nodo.derecho is not None:
        mostrar_arbol(nodo.derecho, nivel + 1)
            

def mostrar_arbol2(nodo, ax, x=0, y=0, nivel=0, nivel_height=0.1):
    if nodo is not None:
        dx = 1.0 / 2**(nivel + 1)
        dy = nivel_height
        ax.text(x, y, nodo.nombre, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))
        
        if nodo.izquierdo is not None:
            mostrar_arbol2(nodo.izquierdo, ax, x - dx, y - dy, nivel + 1, nivel_height)
            ax.add_patch(FancyArrowPatch((x, y), (x - dx, y - dy), color='black', arrowstyle='->', mutation_scale=15))
        
        if nodo.derecho is not None:
            mostrar_arbol2(nodo.derecho, ax, x + dx, y - dy, nivel + 1, nivel_height)
            ax.add_patch(FancyArrowPatch((x, y), (x + dx, y - dy), color='black', arrowstyle='->', mutation_scale=15))

def mostrar_arbol_preorden(nodo):
    if nodo is not None:
        print(nodo.nombre, end=" ")
        mostrar_arbol_preorden(nodo.izquierdo)
        mostrar_arbol_preorden(nodo.derecho)

def mostrar_arbol_inorden(nodo):
    if nodo is not None:
        mostrar_arbol_inorden(nodo.izquierdo)
        print(nodo.nombre, end=" ")
        mostrar_arbol_inorden(nodo.derecho)

def mostrar_arbol_postorden(nodo):
    if nodo is not None:
        mostrar_arbol_postorden(nodo.izquierdo)
        mostrar_arbol_postorden(nodo.derecho)
        print(nodo.nombre, end=" ")

def busqueda(nombre, nodo):
    if nodo is None:
        #print(f"El nodo {nombre} no ha sido encontrado en el árbol.")
        return None
    elif nombre == nodo.nombre:
        #print(f"El nodo {nombre} fue encontrado (existe en el árbol).")
        return nodo
    resultado_izquierdo = busqueda(nombre, nodo.izquierdo)
    resultado_derecho = busqueda(nombre, nodo.derecho)
    return resultado_izquierdo or resultado_derecho



hijo2 = None; hijo2AM= None;tio1= None;tio2=None;primo1=None;primo2=None;primo1M=None;primo2M=None;hermano1 = None

# Crear el nodo raíz del árbol genealógico
#ingresa el nombre del bisabuelo que servirá para partir
bisa_raiz = nombre_valido("Ingresa el nombre del bisabuelo: ")
raiz = Nodo(bisa_raiz)
incrementar_contador_nodos()

if raiz.nombre is not None :
    # Insertar personas en el árbol
    AP = nombre_valido("Ingresa el nombre del abuelo paterno: ")
    abueloPaterno = Nodo(AP)
    incrementar_contador_nodos()
    AM = nombre_valido("Ingresa el nombre del abuelo materno: ")
    abueloMaterno = Nodo(AM)
    incrementar_contador_nodos()

    #Cuantos hijos tiene el abuelo paterno?
    numero_hijosAP = obtener_numero_valido("Ingresa el número de hijos que tiene el abuelo paterno (1 o 2): ", [1, 2])
    if numero_hijosAP == 1:
        hijo1 =nombre_valido("Ingresa el nombre del primer hijo/hija: ")
        padre = Nodo(hijo1)
        incrementar_contador_nodos()
        abueloPaterno.agregar_hijo(padre)
    elif numero_hijosAP == 2:
        hijo1 =nombre_valido("Ingresa el nombre del primer hijo/hija: ")
        padre = Nodo(hijo1)
        incrementar_contador_nodos()
        hijo2 =nombre_valido("Ingresa el nombre del segundo hijo/hija: ")
        tio1 = Nodo(hijo2)
        incrementar_contador_nodos()
        abueloPaterno.agregar_hijo(padre)
        abueloPaterno.agregar_hijo(tio1)
    else:
        print("El número de hijos no es válido")
        
    #Cuantos hijos tiene el abuelo materno?
    numero_hijosAM = obtener_numero_valido("Ingresa el número de hijos que tiene el abuelo materno (1 o 2): ", [1, 2])
    if numero_hijosAM == 1:
        hijo1AM =nombre_valido("Ingresa el nombre del primer hijo/hija: ")
        madre = Nodo(hijo1AM)
        incrementar_contador_nodos()
        abueloMaterno.agregar_hijo(madre)
    elif numero_hijosAM == 2:
        hijo1AM =nombre_valido("Ingresa el nombre del primer hijo/hija: ")
        madre = Nodo(hijo1AM)
        incrementar_contador_nodos()
        hijo2AM =nombre_valido("Ingresa el nombre del segundo hijo/hija: ")
        tio2 = Nodo(hijo2AM)
        incrementar_contador_nodos()
        abueloMaterno.agregar_hijo(madre)
        abueloMaterno.agregar_hijo(tio2)
    else:
        print("El número de hijos no es válido")
    
    #Cuantos hijos tiene el tio paterno?
    if hijo2 is not None:
        numero_primosP = obtener_numero_valido("Ingresa el número de hijos que tiene el tío paterno (0, 1 o 2): ", [0,1,2])
        if numero_primosP == 0:
            print("El tío paterno no tiene hijos")
        elif numero_primosP == 1:
            primo1N = nombre_valido("Ingresa el nombre del primer hijo/hija: ")
            primo1 = Nodo(primo1N)
            incrementar_contador_nodos()
            tio1.agregar_hijo(primo1)
        elif numero_primosP == 2:
            primo1N = nombre_valido("Ingresa el nombre del primer hijo/hija: ")
            primo1 = Nodo(primo1N)
            incrementar_contador_nodos()
            tio1.agregar_hijo(primo1)
            primo2N = nombre_valido("Ingresa el nombre del segundo hijo/hija: ")
            primo2 = Nodo(primo2N)
            incrementar_contador_nodos()
            tio1.agregar_hijo(primo2)
        else:
            print("Número de hijos no es válido")
    else:
        print("No hay un tío paterno")

    #Cuantos hijos tiene el tio materno?
    if hijo2AM is not None:
        numero_primosM = obtener_numero_valido("Ingresa el número de hijos que tiene el tío materno (0, 1 o 2): ", [0,1,2])
        if numero_primosM == 0:
            print("El tío materno no tiene hijos")
        elif numero_primosM == 1:
            primo1MN = nombre_valido("Ingresa el nombre del primer hijo/hija: ")
            primo1M = Nodo(primo1MN)
            incrementar_contador_nodos()
            tio2.agregar_hijo(primo1M)
        elif numero_primosM == 2:
            primo1MN = nombre_valido("Ingresa el nombre del primer hijo/hija: ")
            primo1M = Nodo(primo1MN)
            incrementar_contador_nodos()
            primo2MN = nombre_valido("Ingresa el nombre del segundo hijo/hija: ")
            primo2M = Nodo(primo2MN)
            incrementar_contador_nodos()
            tio2.agregar_hijo(primo1M)
            tio2.agregar_hijo(primo2M)
        else:
            print("Número de hijos no es válido")
    else:
        print("No hay un tío materno")

    #Cuantos hermanos tengo, sólo puede haber 0 o 1?
    num_hermanos = obtener_numero_valido("Ingresa el número de hermanos que tienes (0 o 1): ", [0,1,2])
    if num_hermanos == 1:
        hermano1N = nombre_valido("Ingresa el nombre de tu hermano: ")
        hermano1 = Nodo(hermano1N)
        incrementar_contador_nodos()
        miNombre = nombre_valido("Ingresa tu nombre: ")
        yo = Nodo(miNombre)
        incrementar_contador_nodos()
        padre.agregar_hijo(hermano1)
        madre.agregar_hijo(hermano1)
        padre.agregar_hijo(yo)
        madre.agregar_hijo(yo)
    elif num_hermanos == 0:
        miNombre = nombre_valido("Ingresa tu nombre: ")
        yo = Nodo(miNombre)
        incrementar_contador_nodos()
        padre.agregar_hijo(yo)
        madre.agregar_hijo(yo)
    else:
        print("Número de hermanos no válido")


    #raiz.agregar_hijo(abueloPaterno)
    #raiz.agregar_hijo(abueloMaterno)
    raiz.izquierdo = abueloPaterno
    incrementar_contador_nodos()
    raiz.derecho = abueloMaterno
    incrementar_contador_nodos()
    print("\n");print("\n");
    # Mostrar el árbol genealógico
    os.system('clear')
    print("\nArbol genealógico:")
    #mostrar_arbol(raiz)

    resumen_niveles = mostrar_arbol(raiz)
   

    print()
    # Mostrar los recorridos
    recorridos = True
    while recorridos:
        print("\n Selecciona una opción para visualizar los recorridos:")
        print("1. Recorrido en preorden")
        print("2. Recorrido en inorden")
        print("3. Recorrido en postorden")
        print("4. Buscar en el árbol")
        print("5. Salir del programa")
        print("6. Ver información del árbol")
        print("7. Mostrar árbol")
        opcion = int(input("Opción: "))
        if opcion == 1:
            print("Recorrido en pre-orden:")
            mostrar_arbol_preorden(raiz)
            print()
        elif opcion == 2:
            print("Recorrido en in-orden:")
            mostrar_arbol_inorden(raiz)
            print()
        elif opcion == 3:
            print("Recorrido en post-orden:")
            mostrar_arbol_postorden(raiz)
            print()
        elif opcion == 4:
            nombre_busqueda = nombre_valido("Ingrese el nombre a buscar: ")
            nombre_encontrado = busqueda(nombre_busqueda,raiz)

            if nombre_encontrado is not None:
                print(f"El nombre '{nombre_busqueda}' se encuentra en el árbol")
            else:
                print(f"El nombre '{nombre_busqueda}' no se encuentra en el árbol")
        elif opcion == 5:
            print("Adiós (:")
            sys.exit(0)
        elif opcion == 6:
            print("Información del árbol:")
            print(f"Raíz del árbol: {raiz.nombre}")
            print(f"Grado del árbol: 2")
            print(f"Altura del árbol: {len(niveles)}")
            print(f"Peso del árbol: {obtener_contador_nodos()}")
        elif opcion == 7:
            print("Mostrar árbol")
            fig, ax = plt.subplots(figsize=(12, 12))
            mostrar_arbol2(raiz, ax)
            ax.set_aspect('equal')
            ax.axis('off')
            plt.show()
        else:
            print("Opción inválida. Intente de nuevo.")

else:
    print("No hay un bisabuelo (raíz)")
