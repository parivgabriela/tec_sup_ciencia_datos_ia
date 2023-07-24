#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def validate_number(mensaje_input):
    """validate a number must be positive and an integer

    Args:
        mensaje_input (str): message to print in the input to user

    Returns:
        int: return a validate number
    """
    flag = True

    while flag == True:
        try:
            number = int(input(f"Enter {mensaje_input}: "))
            if number >= 0:
                flag = False
        except:
            print("Enter a number")
    return number

def validate_number_float(mensaje_input, min):
    """validate a number must be positive and an float or int

    Args:
        mensaje_input (str): message to print in the input to user

    Returns:
        float: return a validate number
    """
    flag = True

    while flag == True:
        try:
            number = float(input(f"Enter {mensaje_input}: "))
            if number >= min:
                flag = False
        except:
            print("Enter a number")
    return number

def calculate_jornal(hours, hour_value):
    
    calcJornal = hour_value * hours
    return calcJornal


def jornal_empleado():
    hour = validate_number("total hours")
    hour_value = validate_number("value of hour")
    total = calculate_jornal(hour, hour_value)
    print("El valor del jornal es: ", total)


def celcius_to_farenheit_view():
    gCelcius = validate_number_float(" tempeture in celcius")
    gFar = celcius_to_farenheit(gCelcius)
    print(f"{gCelcius} grados celcius equivale a {gFar}") 

def celcius_to_farenheit(gCelcius):
    gFar = gCelcius * 1.8 + 32
    return gFar
