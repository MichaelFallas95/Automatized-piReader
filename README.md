# Automatized-piReader

El presente proyecto consiste en la implementación de un sistema de lectura automatizada que lleva a cabo el proceso necesario para la reproducción en audio a partir de una imágen capturada de la página del libro en lectura. Este proceso estará basado en el uso de una Raspberry Pi, la cual será la encargada de llevar a cabo las diferentes funciones para esto:
* Software que permita la manipulación de la cámara para la captura de imágenes.
* Reconocimiento óptico de caracteres (OCR), con el fin de convertir la imágen a texto.
* Convertidor de texto a audio (TTS).
Se utiliza el lenguaje de programación Python para esta tarjeta de desarrollo.

Además, se implementará el uso de un Arduino con el fin de emplear las acciones necesarias para el paso automático de hojas para continuar la lectura del libro, controlando los diferentes tipos de motores y sensores a utilizar, por medio del lenguaje de programación C++. Ambas tarjetas estarán comunicadas por medio del puerto USB.
