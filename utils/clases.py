#CLASES

class Libro:
    def __init__(self,titulo,autor,genero,año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año_publicacion = año_publicacion
        self.disponible = True
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False
    
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return True
        else:
            return False
    
    def esAntiguo(self):
        if self.año_publicacion > 20:
            return True
        else:
            return False
    
    def mostrarInfo(self):
        return self.titulo, self.autor, self.genero, self.año_publicacion, self.disponible

class Biblioteca:
    def __init__(self):
        self.lista_libros = []
    
    def agregarLibro(self, libro):
        self.lista_libros.append(libro)
    
    def listarLibros(self):
        return self.lista_libros
    
    def prestar_por_titulo(self,nombre):
        if self.lista_libros.count(nombre):
            indice = self.lista_libros.index(nombre)
            self.lista_libros[indice].prestar()
            return True
        else:
            return False
            
    def devolver_por_titulo(self,nombre):
        if self.lista_libros.count(nombre):
            indice = self.lista_libros.index(nombre)
            self.lista_libros[indice].devolver()
            return True
        else:
            return False