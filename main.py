import logging

class operaciones:    
    def suma(x, y):
        logging.info(f"Esto es un logging de suma de 2 variable {x} + {y} = {x+y}")
        return x + y

    def resta(x, y):
        return x - y

    def multiplicacion(x, y):
        logging.info(f"Esto es un logging de multiplicacion de 2 variables {x} * {y} = {x*y}")
        return x * y

    def is_greater_than(num_1,num_2):
        return num_1 > num_2
    
    def division(x,y):
        return x / y
    
