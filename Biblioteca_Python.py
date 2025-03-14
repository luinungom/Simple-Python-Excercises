class Libro:

    # Método constructor
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.titulo: str = titulo
        self.autor: str = autor
        self.isbn: str = isbn
        self.disponible: bool = disponible

    # Método para añadir un nuevo libro
    @staticmethod
    def agregar(titulo, autor, isbn):
        nuevo_libro = Libro(titulo, autor, isbn)
        print('Libro agregado con éxito.')
        return nuevo_libro

    # Método para prestar un libro, cambia su atributo disponible a False si está disponible, de lo contratrio muestra "El libro ya estaba prestado"
    @staticmethod
    def prestar(isbn, libros_totales):
        isbn_existe = False
        for libro in libros_totales:
            if libro.isbn == isbn:
                isbn_existe = True
                if libro.disponible:
                    libro.disponible = False
                    print('Libro prestado con éxito.')
                else:
                    print('El libro ya estaba prestado')
            break  # Una vez encontrado el libro se sale del bucle
        if not isbn_existe:
            print(f'El ISBN: {isbn} introducido no existe')

    # Método para devolver un libro, si no estaba prestado muestra "El libro ya estaba disponible" por pantalla
    @staticmethod
    def devolver(isbn, libros_totales):
        isbn_existe = False
        for libro in libros_totales:
            if libro.isbn == isbn:
                isbn_existe = True
                if not libro.disponible:
                    libro.disponible = True
                    print('Libro devuelto con éxito.')
                else:
                    print('El libro ya estaba disponible')
            break  # Una vez encontrado el libro se sale del bucle
        if not isbn_existe:
            print(f'El ISBN: {isbn} introducido no existe')

    # Método para mostrar todos los libros del sistema
    @staticmethod
    def mostrar(libros_totales):
        if len(libros_totales) == 0:
            print('No hay libros en la biblioteca')
        else:
            for libro in libros_totales:
                print(f'-{libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {'Si' if libro.disponible else 'No'}')


## Iniciamos el programa ##
## Esta variable controla el bucle principal del programa ##
terminar_operacion: bool = False
## Creamos una lista de libros vacía ##
libros_totales = []

## Usamos un bucle para crear el menu principal, seguirá pidiendo opciones hasta que el usuario elija la opción 5 ##
while not terminar_operacion:
    print("\nBienvenido al Sistema de Gestión de Biblioteca")
    print("1. Agregar un libro")
    print("2. Prestar un libro")
    print("3. Devolver un libro")
    print("4. Mostrar libros")
    print("5. Salir")
    eleccion: str = input("Elige una opción: ")

    if eleccion == "1":
        titulo: str = input("Introduce el título del libro: ")
        autor: str = input("Introduce el autor del libro: ")
        isbn: str = input("Introduce el ISBN del libro: ")
        if not isbn.isdigit():
            print("El ISBN solo puede contener caracteres numéricos")
        else:
            libros_totales.append(Libro.agregar(titulo, autor, isbn))
    elif eleccion == "2":
        isbn: str = input("Introduce el ISBN del libro: ")
        Libro.prestar(isbn, libros_totales)
    elif eleccion == "3":
        isbn: str = input("Introduce el ISBN del libro: ")
        Libro.devolver(isbn, libros_totales)
    elif eleccion == "4":
        Libro.mostrar(libros_totales)
    elif eleccion == "5":
        terminar_operacion = True
    else:
        print("Opción no disponible")
