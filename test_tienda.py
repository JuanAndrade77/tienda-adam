import pytest
from tienda import calcular_total, aplicar_descuento, procesar_pago

# Pruebas de calcular_total
def test_total_correcto():
    assert calcular_total(10, 3) == 30

def test_total_cero():
    assert calcular_total(0, 5) == 0

# Pruebas de aplicar_descuento
def test_descuento_correcto():
    assert aplicar_descuento(100, 10) == 90

def test_descuento_invalido():
    with pytest.raises(ValueError):
        aplicar_descuento(100, -5)

# Pruebas de procesar_pago
def test_pago_con_tarjeta():
    assert procesar_pago(100, "tarjeta") == "Pago de $100 procesado con tarjeta"

def test_pago_metodo_invalido():
    with pytest.raises(ValueError):
        procesar_pago(100, "bitcoin")