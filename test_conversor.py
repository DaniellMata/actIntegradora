"""
Casos de prueba del conversor de unidades, usando pytest.
"""

import pytest
import conversor


# TC01 - RF01/RF02: Celsius <-> Fahrenheit (usa parametrize y marker)
@pytest.mark.unit
@pytest.mark.parametrize("celsius, esperado", [
    (0, 32),
    (100, 212),
    (-40, -40),
])
def test_celsius_a_fahrenheit(celsius, esperado):
    resultado = conversor.celsius_a_fahrenheit(celsius)
    assert round(resultado, 2) == esperado


# TC02 - RF03: Kilometros <-> Millas
@pytest.mark.unit
def test_km_a_millas():
    resultado = conversor.km_a_millas(10)
    assert round(resultado, 2) == 6.21


# TC03 - RF04: Pesos Mexicanos <-> Dolares (tasa fija de 17.5)
@pytest.mark.unit
def test_pesos_a_dolares():
    resultado = conversor.pesos_a_dolares(175)
    assert round(resultado, 2) == 10.00


# TC04 - RNF02: el sistema debe rechazar un valor no numerico
@pytest.mark.unit
def test_validar_numero_invalido():
    with pytest.raises(ValueError):
        conversor.validar_numero("abc")
