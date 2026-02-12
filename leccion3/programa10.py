import pytest
from unittest.mock import Mock

@pytest.fixture
def datos_de_prueba():
    return {"id": 1, "nombre": "Alexis"}

def test_procesar_usuario(datos_de_prueba):
    # Simulamos una respuesta de base de datos
    db_mock = Mock()
    db_mock.obtener_usuario.return_value = datos_de_prueba
    
    resultado = db_mock.obtener_usuario(1)
    assert resultado["nombre"] == "Alexis"
    db_mock.obtener_usuario.assert_called_once_with(1)