from datetime import date #Aqui se guarda la fecha del dia que se presto el libro

class Libro():
    def __init__(self, isbn, titulo, autor, ejemplares_totales):  #Aqui creo la classe libro donde se guardadn los atributos de libro
        self.isbn = isbn                                          # y comienza igual que los totales y disponibles porque apenas se va registrando
        self.titulo = titulo                                      #igual el print que vrifica que se gurado de forma correcta
        self.autor = autor
        self.ejemplares_totales = ejemplares_totales
        self.ejemplares_disponibles = ejemplares_totales
        print("Se registro un nuevo libro {} {}".format(isbn, titulo))


class Usuario():
    def __init__(self, id_usuario, nombre): #Aqui creo la clase usuario que guarda la matricula
        self.id_usuario = id_usuario        #y el nombre y el print para verificar que se registro correctamente
        self.nombre = nombre
        print("Se registro un nuevo usuario {} {}".format(id_usuario, nombre))


class Biblioteca():  #esta es la clase biblioteca es la mas importante
    def __init__(self):
        self.catalogo = {} # creo un diccionario donde se guardan los libros
        self.prestamos = [] #creo una lista donde se guardan los prestamos
        self.usuarios = {} # creo otro diccionario donde se guardan los usuarios

    def agg_libro(self, isbn, titulo, autor, ejemplares): #Este metodo tiene como funcion agregar libros toma los datos del libro y revisa que el
        if isbn in self.catalogo:                         #libro no haya estdo registrado si esta no hace nada y si no lo registra con el isbn en el diccionario
            print("El libro ya existe")
        else:
            self.catalogo[isbn] = Libro(isbn, titulo, autor, ejemplares)

    def reg_usuario(self, id_usuario, nombre):  #Este metodo registra un usuario hace lo mismo que el metodo agg_libro pero con la
        if id_usuario in self.usuarios:        # matricula si no existe lo crea y lo guarda en el diccionario
            print("El usuario ya existe")
        else:
            self.usuarios[id_usuario] = Usuario(id_usuario, nombre)

    def pres_libro(self, isbn, id_usuario): #En este metodo estan  las validaciones, aqui revisa que el libro exista al igual que el
        if isbn not in self.catalogo:       # usuario despues checa la disponibilidad de ejemplares disponibles para despues recorrer la lista
            print("El libro no existe")     # de prestamos para contar los prestamos que estan activos para el usuario ingresado
        elif id_usuario not in self.usuarios:#si encuentra el libro se detiene y igual si llega 3 prestamos, si pasa todas las validaciones
            print("El usuario  ingresado no existe")#registra el prestamo como tupla y le resta 1 al disponible
        else:
            lib = self.catalogo[isbn]
            if lib.ejemplares_disponibles == 0:
                print("No hay ejemplares disponibles")
            else:
                contador = 0
                for pres in self.prestamos:
                    if pres[1] == id_usuario:
                        if pres[0] == isbn:
                            print("El usuario ya tiene ese libro prestado")
                            return
                        contador = contador + 1
                if contador >= 3:
                    print("El usuario ingresado ya cuenta con 3 libros activos")
                else:
                    self.prestamos.append((isbn, id_usuario, str(date.today())))
                    lib.ejemplares_disponibles = lib.ejemplares_disponibles - 1
                    print("Prestamo fue registrado con exito")

    def dev_libro(self, isbn, id_usuario): #Aqui este metodo lo que hace es recorrer toda la tupla con el isbn del libro y la matricula
        encontrado = False                 #del usuario ingresado, despues de eso la borra de la lista con el remove y suma 1 a disponibilidad
        for prestD in self.prestamos:      #si no encuentra nada indica que no encontro algun prestamo
            if prestD[0] == isbn and prestD[1] == id_usuario:
                self.prestamos.remove(prestD)
                self.catalogo[isbn].ejemplares_disponibles = self.catalogo[isbn].ejemplares_disponibles + 1
                print("La devolucion fue realizada con exito")
                encontrado = True
        if encontrado == False:
            print("No se a encontrado algun prestamo")

    def ver_prestamos(self):                #Este metodo tiene como funcion recorrer toda la lista de prestamos para ver si esta vacia si no
        if len(self.prestamos) == 0:        #recorre cada tupla agarra como objeto libro usando en prest[0] para isbn prest[1]usuario
            print("Todavia no hay prestamos activos")#y con el prest[2] obtiene la fecha y de ahi imprime todo
        else:
            for prest in self.prestamos:
                libroo = self.catalogo[prest[0]]
                usuarioo = self.usuarios[prest[1]]
                print("{} prestado a {} el {}".format(libroo.titulo, usuarioo.nombre, prest[2]))

    def top3(self): #En este metodo creamos primero unndiccionario vacio para despues reccorrer todos los prestamos
        frecuencias = {}# y si esta en frecuencia se la suma 1 y si no le agrega y asi recorre el diccionario mostrando los primeros 3 con un contador
        for prestamo in self.prestamos:
            if prestamo[0] in frecuencias:
                frecuencias[prestamo[0]] = frecuencias[prestamo[0]] + 1
            else:
                frecuencias[prestamo[0]] = 1
        contador = 0
        print("Top 3 libros mas prestados:")
        for isbn in frecuencias:
            if contador < 3:
                print("{}. {} - {} prestamos".format(contador +1, self.catalogo[isbn].titulo, frecuencias[isbn]))
                contador = contador + 1

    def bus_autor(self, autor): #En este metodo recorremos todo el catalogo y por cada isbn agarra el atributo autor
        encontrado = False      #si lo encuentra lo imprime y si no recorre todo y avisa que no fue encontrado
        for isbn in self.catalogo:
            libroO = self.catalogo[isbn]
            if autor in libroO.autor:
                print("{} de {}".format(libroO.titulo, libroO.autor))
                encontrado = True
        if encontrado == False:
            print("No se a encontrado libro escrito por ese autor")


bib = Biblioteca() # aqui se crea el objeto de la clase

while True: # este es el menu donde cada numero llama a un metodo de la clase bilioteca con los datos ingresados
    print("""
    1. Alta de libros
    2. Registrar a un usuario
    3. Prestamo de un libro
    4. Devolucion de un libro
    5. Reportes
    6. Salir del sistema
    """)

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        isbn = input("Ingresa el isbn del libro: ")
        titulo = input("Ingresa el titulo del libro: ")
        autor = input("Ingresa el autor del libro: ")
        ejemplares = int(input("Ingresa ejemplares: "))
        bib.agg_libro(isbn, titulo, autor, ejemplares)

    elif opcion == "2":
        id_usuario = input("Ingresa la matricula del usuario a registrar: ")
        nombre = input("Ingresa el nombre del usuario a registrar: ")
        bib.reg_usuario(id_usuario, nombre)

    elif opcion == "3":
        isbn = input("Ingresa el ISBN del libro a prestar: ")
        id_usuario = input("Ingresa la matricula del usuario: ")
        bib.pres_libro(isbn, id_usuario)

    elif opcion == "4":
        isbn = input("Ingresa el ISBN del libro a devolver: ")
        id_usuario = input("Ingresa la matricula del usuario: ")
        bib.dev_libro(isbn, id_usuario)

    elif opcion == "5":
        print("""
        a) Lista de prestamos activos
        b) Top 3 libros mas prestados
        c) Consultar libros por autor
        """)
        sub = input("Elige el reporte: ")
        if sub == "a":
            bib.ver_prestamos()
        elif sub == "b":
            bib.top3()
        elif sub == "c":
            autor = input("Ingresa el autor a buscar: ")
            bib.bus_autor(autor)

    elif opcion == "6":
        print("Saliendo del sistema")
        break

    else:
        print("Opcion no valida")