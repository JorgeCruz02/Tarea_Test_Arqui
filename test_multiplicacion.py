from main import operaciones
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_multiplicacion():
    assert operaciones.multiplicacion(7,3) == 21
    
if __name__ == "__main__":
    test_multiplicacion()
