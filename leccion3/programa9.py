import pytest

# El algoritmo a probar
def dividir(a, b):
    if b == 0: raise ValueError("División por cero")
    return a / b

# El Test
def test_dividir_positivo():
    assert dividir(10, 2) == 5

def test_dividir_error():
    # Verificamos que el algoritmo lance la excepción correcta
    with pytest.raises(ValueError):
        dividir(10, 0)