from app.calculadora import somar, subtrair, calcular_desconto


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(5, 3) == 2


def test_calcular_desconto():
    assert calcular_desconto(100, 10) == 90