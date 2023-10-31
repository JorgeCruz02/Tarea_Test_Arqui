
import logging
from main import operaciones

# Configura el registro
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_division():
    a = -1
    b = 0

    # Mensaje de depuración
    logging.debug(f"Realizando la división d {a} entre {b}")

    try:
        result = operaciones.division(a, b)
        # Mensaje de información
        logging.info(f"La división de {a} entre {b} es {result}")
        assert result == 0
    except ZeroDivisionError:
        # Mensaje de error
        logging.error("No se puede dividir por cero")
    except Exception as e:
        # Mensaje de error crítico
        logging.critical(f"Ocurrió un error crítico: {str(e)}")

if __name__ == "__main__":
    test_division()

