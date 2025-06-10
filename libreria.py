import datetime

class Libro:
    def __init__(self, titulo, autor, isbn, num_paginas, genero):
        self.titulo = titulo
        self.autor = autor  # Se asocia con un objeto Autor
        self.isbn = isbn
        self.num_paginas = num_paginas
        self.genero = genero
        self.__prestado = False  # Atributo encapsulado (privado)

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            return True
        else:
            return False

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            return True
        else:
            return False

    def esta_prestado(self):
        return self.__prestado

    def __str__(self):
        return f"'{self.titulo}' por {self.autor.nombre}"

class LibroElectronico(Libro):
    def __init__(self, titulo, autor, isbn, num_paginas, genero, formato):
        super().__init__(titulo, autor, isbn, num_paginas, genero)
        self.formato = formato

    def __str__(self):
        return f"'{self.titulo}' (E-book - {self.formato}) por {self.autor.nombre}"

class LibroAudiovisual(Libro):
    def __init__(self, titulo, autor, isbn, duracion_min, genero):
        # Un libro audiovisual no tiene número de páginas, usamos None o 0
        super().__init__(titulo, autor, isbn, 0, genero)
        self.duracion_min = duracion_min

    def __str__(self):
        return f"'{self.titulo}' (Audiolibro - {self.duracion_min} min) por {self.autor.nombre}"

class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento # Usar formato 'YYYY-MM-DD'

    def publicar_libro(self, titulo, isbn, num_paginas, genero):
        # Un autor puede "publicar" un libro, devolviendo un objeto Libro
        return Libro(titulo, self, isbn, num_paginas, genero)

    def __str__(self):
        return self.nombre

class Lector:
    def __init__(self, nombre, edad, direccion, numero_socio):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numero_socio = numero_socio
        self.libros_prestados = []

    def solicitar_prestamo(self, libro):
        if not libro.esta_prestado():
            if libro.prestar():
                self.libros_prestados.append(libro)
                print(f"{self.nombre} ha solicitado el préstamo de '{libro.titulo}'.")
                return True
        print(f"'{libro.titulo}' no está disponible para préstamo.")
        return False

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            if libro.devolver():
                self.libros_prestados.remove(libro)
                print(f"{self.nombre} ha devuelto '{libro.titulo}'.")
                return True
        print(f"'{libro.titulo}' no fue prestado a {self.nombre}.")
        return False

    def __str__(self):
        return f"Lector: {self.nombre} (Socio: {self.numero_socio})"

class LectorNinio(Lector):
    def __init__(self, nombre, edad, direccion, numero_socio, tutor):
        super().__init__(nombre, edad, direccion, numero_socio)
        self.tutor = tutor

    def solicitar_prestamo(self, libro):
        # Regla especial para niños: solo pueden prestar libros de género "Infantil"
        if libro.genero == "Infantil" and not libro.esta_prestado():
            if libro.prestar():
                self.libros_prestados.append(libro)
                print(f"{self.nombre} (niño) ha solicitado el préstamo de '{libro.titulo}'.")
                return True
        elif libro.genero != "Infantil":
            print(f"{self.nombre} (niño) solo puede solicitar libros de género 'Infantil'.")
        else:
            print(f"'{libro.titulo}' no está disponible para préstamo.")
        return False

    def __str__(self):
        return f"Lector (Niño): {self.nombre} (Socio: {self.numero_socio}, Tutor: {self.tutor})"


class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo_libros = []
        self.lista_autores = []
        self.lista_lectores = []

    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self.catalogo_libros.append(libro)
            print(f"Se agregó '{libro.titulo}' al catálogo.")
        else:
            print("Solo se pueden agregar objetos de tipo Libro.")

    def agregar_autor(self, autor):
        if isinstance(autor, Autor):
            self.lista_autores.append(autor)
            print(f"Se agregó a {autor.nombre} a la lista de autores.")
        else:
            print("Solo se pueden agregar objetos de tipo Autor.")

    def registrar_lector(self, lector):
        if isinstance(lector, Lector):
            self.lista_lectores.append(lector)
            print(f"Se registró a {lector.nombre} como lector.")
        else:
            print("Solo se pueden registrar objetos de tipo Lector.")

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.catalogo_libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, libro, lector):
        if libro in self.catalogo_libros and lector in self.lista_lectores:
            return lector.solicitar_prestamo(libro)
        else:
            print("Libro o lector no encontrados en la librería.")
            return False

    def devolver_libro(self, libro, lector):
        if libro in self.catalogo_libros and lector in self.lista_lectores:
            return lector.devolver_libro(libro)
        else:
            print("Libro o lector no encontrados en la librería.")
            return False

    def mostrar_catalogo(self):
        print(f"\n--- Catálogo de {self.nombre} ---")
        if not self.catalogo_libros:
            print("El catálogo está vacío.")
            return
        for libro in self.catalogo_libros:
            estado = "Prestado" if libro.esta_prestado() else "Disponible"
            print(f"- {libro} (Estado: {estado})")
        print("------------------------------")

    def mostrar_lectores(self):
        print(f"\n--- Lectores Registrados en {self.nombre} ---")
        if not self.lista_lectores:
            print("No hay lectores registrados.")
            return
        for lector in self.lista_lectores:
            print(f"- {lector}")
            if lector.libros_prestados:
                print(f"  Libros prestados: {[libro.titulo for libro in lector.libros_prestados]}")
            else:
                print("  No tiene libros prestados.")
        print("------------------------------------------")


# --- Ejemplo de Uso ---
if __name__ == "__main__":
    # 1. Crear objetos de Autor
    autor1 = Autor("Gabriel García Márquez", "Colombiana", "1927-03-06")
    autor2 = Autor("J.K. Rowling", "Británica", "1965-07-31")
    autor3 = Autor("Stephen King", "Estadounidense", "1947-09-21")

    # 2. Crear objetos de Libro
    cien_anios = Libro("Cien Años de Soledad", autor1, "978-0307474728", 496, "Realismo Mágico")
    harry_potter = Libro("Harry Potter y la Piedra Filosofal", autor2, "978-8478886510", 256, "Fantasía")
    it = Libro("It", autor3, "978-0451169518", 1138, "Terror")
    el_principito = Libro("El Principito", Autor("Antoine de Saint-Exupéry", "Francesa", "1900-06-29"), "978-3125642273", 96, "Infantil")
    
    # Crear un libro electrónico y un audiolibro
    harry_potter_ebook = LibroElectronico("Harry Potter y la Cámara Secreta", autor2, "978-8478886527", 320, "Fantasía", "PDF")
    cien_anios_audiolibro = LibroAudiovisual("Cien Años de Soledad", autor1, "978-0307474728-A", 1800, "Realismo Mágico")

    # 3. Crear objetos de Lector
    lector1 = Lector("Ana García", 28, "Calle Falsa 123", "LS001")
    lector2 = Lector("Pedro Martínez", 35, "Avenida Siempre Viva 742", "LS002")
    lector_ninio = LectorNinio("Sofía Pérez", 8, "Calle de los Niños 5", "LS003", "Laura Pérez")

    # 4. Crear objeto de Librería
    mi_libreria = Libreria("Mi Librería del Saber")

    # 5. Operaciones de la Librería
    mi_libreria.agregar_autor(autor1)
    mi_libreria.agregar_autor(autor2)
    mi_libreria.agregar_autor(autor3)

    mi_libreria.agregar_libro(cien_anios)
    mi_libreria.agregar_libro(harry_potter)
    mi_libreria.agregar_libro(it)
    mi_libreria.agregar_libro(el_principito)
    mi_libreria.agregar_libro(harry_potter_ebook)
    mi_libreria.agregar_libro(cien_anios_audiolibro)

    mi_libreria.registrar_lector(lector1)
    mi_libreria.registrar_lector(lector2)
    mi_libreria.registrar_lector(lector_ninio)

    mi_libreria.mostrar_catalogo()
    mi_libreria.mostrar_lectores()

    print("\n--- Realizando préstamos ---")
    mi_libreria.prestar_libro(cien_anios, lector1)
    mi_libreria.prestar_libro(harry_potter, lector2)
    mi_libreria.prestar_libro(cien_anios, lector2) # Intentar prestar un libro ya prestado
    mi_libreria.prestar_libro(it, lector_ninio) # Intentar prestar un libro no infantil a un niño
    mi_libreria.prestar_libro(el_principito, lector_ninio) # Prestar libro infantil a un niño

    mi_libreria.mostrar_catalogo()
    mi_libreria.mostrar_lectores()

    print("\n--- Realizando devoluciones ---")
    mi_libreria.devolver_libro(cien_anios, lector1)
    mi_libreria.devolver_libro(it, lector1) # Intentar devolver un libro que no tiene

    mi_libreria.mostrar_catalogo()
    mi_libreria.mostrar_lectores()

    print("\n--- Buscando un libro ---")
    libro_encontrado = mi_libreria.buscar_libro_por_titulo("It")
    if libro_encontrado:
        print(f"Libro encontrado: {libro_encontrado}")
    else:
        print("Libro no encontrado.")

    libro_no_encontrado = mi_libreria.buscar_libro_por_titulo("La Odisea")
    if libro_no_encontrado:
        print(f"Libro encontrado: {libro_no_encontrado}")
    else:
        print("Libro 'La Odisea' no encontrado.")