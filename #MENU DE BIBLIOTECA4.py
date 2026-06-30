#MENU DE BIBLIOTECA

#lista inicializada
libro=[]

#funcion menu()
def menu():
    print("-"*30)
    print("---------------MENU---------------")
    print("="*30)
    print("1) AGREGAR LIBRO")
    print("2) BUSCAR LIBRO")
    print("3) ELIMINAR LIBRO")
    print("4) ACTUALIZAR DISPONIBILIDAD")
    print("5) MOSTRAR LIBROS")
    print("6)  SALIR")
#esta es toda la validacion para poder hacer correr el programa correctamente
def opciones():
    try:
        opc=int(input("ingrese una opcion del menu"))
        if opc < 1 or opc > 6:
            print("ingrese un digito valido entre las opciones del menu")
        else:
             return opc
    except ValueError:
        print("ERROR: ingrese valores numericos solamente")
def validar_titulo(titulo):
    if titulo.strip()!="":
        return True
    return False
def validar_copias(copias):
    try:
        copias=int(copias)
        if copias>0:
            return True
        else:
            return False
    except ValueError:
        return False
def validar_prestamo(prestamo):
    try:
        prestamo=int(prestamo)
        if prestamo >0:
            return True
        else:
             return False
    except ValueError:
        return False
#esta es la primera opcion del menu, esta permite agregar libros dentro de la lista
def agregar_libro(lista):
    titulo=input("ingrese el titulo del libro que desea llevar")
    copias=input("ingrese la cantidad de copias del libro")
    prestamo=int(input("ingrese la cantidad de dias que desea solicitar el libro"))
    if not validar_titulo(titulo):
        print("el titulo no puede estar vacio y ser solo espacios en blanco")
        return
    if not validar_copias(copias):
        print("ingrese solo valores enteros y digitos numericos")
        return
    if not validar_prestamo(prestamo):
        print("ingrese solo valores enteros y digitos numericos")

    libro={

        "titulo":titulo,
        "copias":copias,
        "prestamo":prestamo,
        "disponible": False
    }
    lista.append(libro)
    print("libro agregado")
#esta funcion busca un libro que pida el usuario recorriendo la lista 
def buscar_libro(lista,titulo):
    for libro in range (len(lista)):
        if lista[libro]["titulo"]==titulo:
            return libro
    return -1
#esta funcion solo hace que se eliminen los libros deseados de la lista utilizando el .pop()
def eliminar_libros(lista):
    titulo=input("ingrese el titulo del libro que desea eliminar")
    posicion=buscar_libro(lista,titulo)
    if posicion != 1:
        lista.pop(posicion)
        print("libro eliminado correctamente")
    else:
         print(f"el libro {titulo} no se encuentra registrado")
#la funcion cumple haciendo una actualizacion de disponibilidad de los libros registrados
def actualizar_disponibilidad(lista):
    for i in range (len(lista)):
        if lista[i]["copias"]>=1:
            lista[i]["disponible"]=True
        else:
             lista[i]["disponible"]=False
    print("disponibilidad actualizada")
#en esta funcion se recorre por completo la lista 
def mostrar_libros(lista):
    actualizar_disponibilidad(lista)
    if len(lista)==0:
        print("no hay ningun libro regsistrado")
        return
    print("===LISTA DE LIBROS===")
    for i in range(len(lista)):
        print(f"TITULO:{lista[i]["titulo"]}")
        print(f"COPIAS:{lista[i]["copias"]}")
        print(f"PRESTAMO:{lista[i]["prestamo"]}")
        print(f"ESTADO:{lista[i]["disponible"]}")

        if lista[i]["disponible"]==True:
            print("DISPONIBLE")
        else:
            print("NO DISPONIBLE")
        print("*"*45)
#funcion para correr el programa 
#se genera la lista y se llama a las respectivas funciones dependiendo de cada opcion que se llame
def programa():
    lista=[]
    while True:
        menu()
        opc=opciones()
        #opc 1 solo se llama a la funcion y se agrega a la lista
        if opc==1:
            agregar_libro(lista)
        #opc 2 aqui cambia lo que se pone dentro de la opc porque aqui te pide mostrar donde esta el libro que uno quiere agregar
        elif opc==2:
            titulo=input("ingrese el titulo del libro que desea agregar")
            posicion=buscar_libro(lista,titulo)
            if posicion!=1:
                print(f"libro encontrado en las posicion{posicion}")
                print(f"titulo: {lista[posicion]["titulo"]}")
                print(f"copias: {lista[posicion]["copias"]}")
                print(f"prestamo:{lista[posicion]["prestamo"]}")
                print(f"disponible:{lista[posicion]["disponible"]}")
            else:
                print(f"el libro {titulo}no se encuentra")
        #opc 3 se llama a la funcion elminira_libros() para poder ejecutarla
        elif opc==3:
            eliminar_libros(lista)
        #opc 4 lo mismo que la anterior pero esta funcion actualiza la disponibilidad de cada libro
        elif opc==4:

            actualizar_disponibilidad(lista)
        #opc 5 por ultimo esta opcion ejecuta la funcion la cual consiste en recorrer toda la lista y asi pueda mostrar cada uno de los libros registrados 
        elif opc==5:

            mostrar_libros(lista)
        #opc 6 esta opcion es un mensaje de salida y da el termino a la funcion programa 
        elif opc==6:

            print("Gracias por usar el sistema. Vuelva Pronto ")
            break
#para que se llama la funcion programa al final. para poder ejecturarlo y poder hacerla funcionar
programa()