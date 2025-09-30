#TESTING
from config import Libro, Biblioteca

biblioteca = Biblioteca()

while True:
    
    opcion = input('''
                    1
                    2
                    3
                    4
                    5
                    ''')

    if opcion == '1':
        
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        genero = input('Genero: ')
        
        while True:
            try:
                año_publicacion = int(input('Año de publicación: '))
                break
            except:
                print('Maldito fracasado, escribí bien')
        
        libro = Libro(titulo,autor,genero,año_publicacion)
        biblioteca.agregarLibro(libro)
        
    elif opcion == '2':
        
        lista = biblioteca.listarLibros()
        
        for i in lista:
            print(i.mostrarInfo())
        