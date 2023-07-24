from clase05_04 import calculate_jornal, celcius_to_farenheit

def test_calculate_jornal():
    assert calculate_jornal(10,100) == 1000

def test_celcius_to_farenheit():
    assert celcius_to_farenheit(0) == 32
