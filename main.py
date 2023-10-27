import logging

logging.basicConfig(level=logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger = logging.getLogger('test')
logger.addHandler(console_handler)
console_logs = console_handler.stream.getvalue(logger)
print(console_logs)
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
    
