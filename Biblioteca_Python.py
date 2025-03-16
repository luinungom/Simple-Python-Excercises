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
        if len(titulo) == 0:
            print('El campo Título no puede estar vacío')
            return None
        elif len(autor) == 0:
            print('El campo Autor no puede estar vacío')
            return None
        elif len(isbn) == 0:
            print('El campo ISBN no puede estar vacío')
            return None
        elif not isbn.isdigit():
            print('El ISBN solo puede contener caracteres numéricos.')
            return None
        else:
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
        if len(libros_totales) == 0 or libros_totales is None:
            print('No hay libros en la biblioteca')
        else:
            for libro in libros_totales:
                # llamamamos al metodo buscar para reutilizar código
                Libro.buscar(libro.isbn, libros_totales)

    # Método para buscar un libro por ISBN
    @staticmethod
    def buscar(isbn, libros_totales):
        if len(libros_totales) == 0 or libros_totales is None:
            print('No hay libros en la biblioteca')
        else:
            isbn_existe = False
            for libro in libros_totales:
                if libro.isbn == isbn:
                    isbn_existe = True
                    print(
                        f'-{libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {'Si' if libro.disponible else 'No'}')
                    break
            if not isbn_existe:
                print(f'El ISBN: {isbn} introducido no existe')


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
    print("5. Buscar libro")
    print("6. Salir")
    eleccion: str = input("Elige una opción: ")

    if eleccion == "1":
        titulo: str = input("Introduce el título del libro: ").strip()
        autor: str = input("Introduce el autor del libro: ").strip()
        isbn: str = input("Introduce el ISBN del libro: ").strip()
        nuevo_libro = Libro.agregar(titulo, autor, isbn)
        if nuevo_libro is not None:
            libros_totales.append(nuevo_libro)
    elif eleccion == "2":
        isbn: str = input("Introduce el ISBN del libro: ").strip()
        Libro.prestar(isbn, libros_totales)
    elif eleccion == "3":
        isbn: str = input("Introduce el ISBN del libro: ").strip()
        Libro.devolver(isbn, libros_totales)
    elif eleccion == "4":
        Libro.mostrar(libros_totales)
    elif eleccion == "5":
        isbn: str = input("Introduce el ISBN del libro: ").strip()
        Libro.buscar(isbn, libros_totales)
    elif eleccion == "6":
        terminar_operacion = True
    else:
        print("Opción no disponible")