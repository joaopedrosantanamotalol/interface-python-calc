def soma(a, b):
    try:
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        return "Entrada inválida"
    
def multiplicacao(a,b):
    try:
        a = float(a)
        b = float(b)
        return a * b
    except ValueError:
        return "Entrada inválida"