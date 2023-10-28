import logging
from main import operaciones

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_resta():
    num1 = 7
    num2 = 20
    result = operaciones.resta(num1, num2)

   
    # Logging debug, se realiza siempre que se ejecute el código para este ejemplo.
    logging.debug('Resta realizada')

    # Logging info, se realiza siempre que se ejecute el código para este ejemplo indicando el resultado de la resta. 
    logging.info(f'Resta realizada: {num1} - {num2} = {result}')

    if result < 0:
        # Logging warning, únicamente se da si el resultado es menor a cero. 
        logging.warning('El resultado es negativo, podría ocasionar algún problema en algún contexto específico.')

    if result < -5:
        # Logging error, se da si el resultado es menor a menos cinco. 
        logging.error('La resta produjo un valor negativo, sólo se admiten resultados positivos.')

    if result < -10:
        # Logging critical, se da si el resultado es menor a menos diez. 
        logging.critical('La resta produjo un valor críticamente negativo. ¡El programa no puede continuar!')

    assert result == -13

if __name__ == "__main__":
    test_resta()






