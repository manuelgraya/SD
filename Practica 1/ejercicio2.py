""". #Existe una variable de entorno que nos permite ejecutar comandos
ubicados en /bin, sin necesidad de escribir la ruta completa, ni situarnos
en el directorio en cuestión, muestra en pantalla el valor que contiene.
¿Qué módulo permite ver esto usando import nombreDelModulo al principio
del script?
"""

import os

# Obtener el valor de la variable de entorno PATH
path_value = os.getenv('PATH')

# Mostrar en pantalla el valor de la variable PATH
print("La ruta es:" ,path_value)
