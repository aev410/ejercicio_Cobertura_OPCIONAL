from Contar import Contar

def test_ContarBocales():
    a = Contar("Hola")
    b = a.contarVocales()
    assert  b == 2
    
def test_ContarPalabras():
    a = Contar("Hola mundo")
    b = a.contarPalabras()
    assert b == 2


