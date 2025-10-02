#TESTING
from config import Libro, Biblioteca, tk, messagebox

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
    
    elif opcion == '3':
        
        titulo = input('Ingrese titulo a ser prestado: ')
        res = biblioteca.prestar_por_titulo(titulo)
        if res == 1:
            messagebox.showinfo(title='ÉXITO', message='Prestado correctamente')
        elif res == 2:
            messagebox.showwarning(title='NO DISPONIBLE', message='Ese libro no está disponible debido a que ya fue prestado')
        else:
            messagebox.showerror(title='NO EXISTENTE', message='El ítem que intentó pedir no existe')
    
    elif opcion == '4':
        
        titulo = input('Ingrese titulo a ser regresado: ')
        res = biblioteca.devolver_por_titulo(titulo)
        if res == 1:
            messagebox.showinfo(title='ÉXITO', message='Devuelto correctamente')
        elif res == 2:
            messagebox.showwarning(title='NO PRESTADO', message='Ese libro no fue prestado')
        else:
            messagebox.showerror(title='NO EXISTENTE', message='El ítem que intentó devolver no existe')
    
    elif opcion == '5':
        
        lista = biblioteca.listarLibros()
        
        for i in lista:
            if i.esAntiguo():
                print(i.mostrarInfo())