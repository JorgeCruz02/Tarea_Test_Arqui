<<<<<<< Updated upstream
from main import operaciones

def test_resta():
    assert operaciones.resta(7,3) == 4
=======
import logging
from main import operaciones

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_resta():
    num1 = 7
    num2 = 20
    result = operaciones.resta(num1, num2)

   
    # Logging debug
    logging.debug('Resta realizada')

    # Logging info
    logging.info(f'Resta realizada: {num1} - {num2} = {result}')

    if result < 0:
        # Logging warning
        logging.warning('El resultado es negativo, podría ocasionar algún problema en algún contexto específico.')

    if result < 0:
        # Logging error
        logging.error('La resta produjo un valor negativo, sólo se admiten resultados positivos.')

    if result < -10:
        # Logging critical
        logging.critical('La resta produjo un valor críticamente negativo. ¡El programa no puede continuar!')

    assert result == -13

if __name__ == "__main__":
    test_resta()





>>>>>>> Stashed changes
