import logging


class operaciones:    
    def suma(x, y):
        logger.info(f"Esto es un logging de suma de 2 variable {x} + {y} = {x+y}")
        return x + y

    def resta(x, y):
            if x - y < 0:
                logger.error(f"Esto es un logging de resta de 2 variable {x} - {y} = {x-y}")

    def multiplicacion(x, y):
        return x * y

    def is_greater_than(num_1,num_2):
        return num_1 > num_2
    
    def division(x,y):
        return x / y
