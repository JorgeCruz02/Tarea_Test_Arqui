# Tarea_Test_Arqui
Tarea de Arquitectura de software para probar las suits de pruebas y logging

Readme con los participantes:

-Cervantes Figueroa Angélica

-Cruz Molina Jorge Antonio

-Velázquez Peña Alejandro

-Visomblain Eva

Lenguaje: python

La suite que están utilizando para pruebas: pytest

Como continuación a su tarea de pruebas unitarias, utilizando una libreria de logging, agregar al menos una línea por cada nivel de logging.

Libreria que usamos: logging

Descripción de las líneas de logueo que agregaron.
-logging.debug():Mensajes detallados, útiles para diagnóstico durante el desarrollo.

-logging.info(): Mensajes informativos que muestran el progreso del programa en un nivel más alto que DEBUG.

-logging.warning(): Mensajes que indican que algo inesperado ha ocurrido o puede indicar un problema en el futuro cercano 

-logging.error(): Mensajes de error debido a los cuales el programa no pudo realizar alguna función.

-logging.critical(): Mensajes de error muy graves que indican que el programa no puede continuar ejecutándose.
      
Explicar en dónde se cambia el valor del nivel de logging y qué valores son válidos:

-Test suma 

Para este ejemplo únicamente se agregó el logging de info que indica el resultado de la operación.

-Test resta 

Para este ejemplo se decidió que el logging cambiara de la siguiente manera: 

      Loggig debug: Se realiza siempre que se ejecuta el código. 
      
      Logging info: Se realiza siempre que se ejecute el código indicando el resultado de la resta.
      
      Logging warning: Únicamente aparece si el resultado es menor a 0.
      
      Logging error: Se da si el resultado es menor a -5. 
      
      Logging critical: Se da si el resultado es menor a -10.
      
-Test multiplicación

Para este ejemplo únicamente se agregó el logging de info que indica el resultado de la operación. 

-Test división 

Para este ejemplo se decidió que los logging cambiaran de la siguiente manera:

      Logging debug: Indica que se realiza la división. 
      
      Logging info: Indica el resultado de la división en caso de tener éxito.
      
      Logging error: Únicamente se da si se desea dividir entre 0. 
      
      Logging critical: Ocurre en caso de haber una excepción en donde no se pueda realizar la operación. 


