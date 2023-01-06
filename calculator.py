from numbers import Number


def mul(x,y):
    """AOR"""
    return x ** y 

def soma(x,y):
    """AOR"""
    return x + y

def invert(x):
    """
    AOD - Delete o operador
    AOR - troca o operador 
    """
    return -x

def sum_(*vals):
    """
    ASR - Troca o operador de atribuição
    CRP - troca as constantes
    """
    result = 0
    for val in vals:
        result += val
    return result

def is_number(val):
    """
        COD - deletar operadores sozinhos (not)
        COI 
    """
    if not isinstance(val, Number):
        return False
    return True
        