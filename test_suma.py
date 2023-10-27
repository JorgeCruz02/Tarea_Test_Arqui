from main import operaciones
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_suma():
    assert operaciones.suma(9,2) == 11
    
if __name__ == "__main__":
    test_suma()