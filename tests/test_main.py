# Funcion de test_main

def test_main():
    assert True
    
def test_long_strings():
    izquierda = "Esta es una cadena muy larga que se va a comparar con otra cadena larga"
    derecha = "Esta es una cadena muy larga que se va a comparar con otra cadena larga"
    assert izquierda == derecha

def test_lists():
    left = ["sugar", "wheat", "coffee", "salt", "water", "milk"]
    right = ["sugar", "coffee", "wheat", "salt", "water", "milk"]
    assert left == right

def test_diccionarios():
    izquierda = {"calle": "Ferry Ln.", "número": 39, "estado": "Nevada", "código postal": 30877, "condado": "Frett"}
    derecha = {"calle": "Ferry Lane", "número": 38, "estado": "Nevada", "código postal": 30877, "condado": "Frett"}
    assert izquierda == derecha