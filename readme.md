Explicación de los Conceptos de POO
Creación de Clases
Hemos definido las siguientes clases:

Libro: Representa un libro físico con sus atributos básicos y métodos para su gestión.
Autor: Representa al autor de un libro.
Lector: Representa a una persona que puede tomar prestados libros.
Libreria: Actúa como el contenedor principal, gestionando libros, autores y lectores.
LibroElectronico y LibroAudiovisual: Heredan de Libro, demostrando cómo se pueden crear tipos más específicos de libros que comparten características comunes pero también tienen las suyas propias.
LectorNinio: Hereda de Lector, mostrando cómo diferentes tipos de lectores pueden tener comportamientos distintos (polimorfismo).
Atributos y Métodos
Cada clase tiene:

Atributos: Son las características que describen el objeto (ej. titulo, autor en Libro; nombre, nacionalidad en Autor).
Métodos: Son las acciones que el objeto puede realizar (ej. prestar(), devolver() en Libro; solicitar_prestamo() en Lector). El método __init__ es especial y se usa para inicializar el objeto al crearlo.
Relaciones entre Objetos
Libro y Autor: Un objeto Libro tiene un atributo autor que es, a su vez, un objeto Autor. Esto establece una relación "tiene un" (has-a).
Libreria y otros objetos: La clase Libreria contiene listas de objetos Libro, Autor y Lector. Esto significa que la Libreria "tiene" múltiples libros, autores y lectores, lo que es un ejemplo de composición.
Lector y Libro: Cuando un Lector toma prestado un Libro, este Libro se añade a la lista libros_prestados del Lector, estableciendo una relación de préstamo.
Encapsulación
El atributo __prestado en la clase Libro es un ejemplo de encapsulación. El doble guion bajo (__) antes del nombre lo convierte en un atributo "privado" (o al menos lo dificulta su acceso directo desde fuera de la clase). Esto significa que el estado de si un libro está prestado o no debe ser gestionado únicamente a través de los métodos prestar(), devolver() y esta_prestado(). Esto ayuda a proteger la integridad de los datos del objeto.

Polimorfismo
El polimorfismo ("muchas formas") se ilustra con las clases Lector y LectorNinio. Ambas tienen un método solicitar_prestamo(), pero la implementación de este método es diferente:

El Lector general puede solicitar cualquier libro disponible.
El LectorNinio tiene una regla especial: solo puede solicitar libros cuyo género sea "Infantil".
Cuando llamas a solicitar_prestamo() sobre un objeto Lector o LectorNinio, Python sabe automáticamente qué versión del método ejecutar basándose en el tipo de objeto.