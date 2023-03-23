

class Contar:
    vocales = ["a","e","i","o","u"]
    texto = ""

    def __init__(self, texto):
        self.texto = texto
    
    def contarVocales(self):
        vocal = 0
        i = 0
        for n in self.texto:
            if self.texto[i] in self.vocales:
                vocal += 1 
            i +=1
        return vocal

    def contarPalabras(self):
        palabra = 1
        
        if self.texto.__len__() > 1:
            for n in self.texto:
                if n == " ":
                    palabra += 1
        return palabra