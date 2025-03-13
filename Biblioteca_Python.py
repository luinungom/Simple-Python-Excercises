class Libro:
    libros_totales = []

    # Método constructor
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.titulo: str = titulo
        self.autor: str = autor
        self.isbn: str = isbn
        self.disponible: bool = disponible

    # Método para añadir un nuevo libro
    def agregar(self, titulo, autor, isbn):
        nuevo_libro = Libro(titulo, autor, isbn)
        self.libros_totales.append(nuevo_libro)
        print('Libro agregado con éxito.')

    # Método para prestar un libro, cambia su atributo disponible a False si está disponible, de lo contratrio muestra "El libro ya estaba prestado"
    def prestar(self, isbn):
        isbn_existe = False
        for libro in Libro.libros_totales:
            if libro.isbn == isbn:
                isbn_existe = True
                if libro.disponible:
                    libro.disponible = False
                    print('Libro prestado con éxito.')
                else:
                    print('El libro ya estaba prestado')
            break #Una vez encontrado el libro se sale del bucle
        if not isbn_existe:
            print(f'El ISBN: {isbn} introducido no existe')

    # Método para devolver un libro, si no estaba prestado muestra "El libro ya estaba disponible" por pantalla
    def devolver(self, isbn):
        isbn_existe = False
        for libro in Libro.libros_totales:
            if libro.isbn == isbn:
                isbn_existe = True
                if not libro.disponible:
                    libro.disponible = True
                    print('Libro devuelto con éxito.')
                else:
                    print('El libro ya estaba disponible')
            break #Una vez encontrado el libro se sale del bucle
        if not isbn_existe:
            print(f'El ISBN: {isbn} introducido no existe')

    # Método para mostrar todos los libros del sistema
    def mostrar(self):
        try:
            for libro in self.libros_totales:
                print(f'-{libro.titulo}({libro.autor}) - ISBN: {libro.isbn} - Disponible: {libro.disponible}')
        except Exception as e:
            print('No hay libros en la biblioteca')


terminar_operacion : bool = False

while not terminar_operacion:
    print("\nBienvenido al Sistema de Gestión de Biblioteca")
    print("1. Agregar un libro")
    print("2. Prestar un libro")
    print("3. Devolver un libro")
    print("4. Mostrar libros")
    print("5. Salir")
    eleccion : str = input("Elige una opción: ")

    if eleccion == "1":
        titulo : str = input("Introduce el título del libro: ")
        autor : str = input("Introduce el autor del libro: ")
        isbn : str = input("Introduce el ISBN del libro: ")
        Libro.agregar(titulo, autor, isbn)
    elif eleccion == "2":
        isbn : str = input("Introduce el ISBN del libro: ")
        Libro.prestar(isbn)
    elif eleccion == "3":
        isbn : str = input("Introduce el ISBN del libro: ")
        Libro.devolver(isbn)
    elif eleccion == "4":
        Libro.mostrar()
    elif eleccion == "5":
        terminar_operacion = True
    else:
        print("Opción no disponible")
