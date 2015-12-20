import time
from subprocess import call
import re

#Función que subdivide un párrafo grande en pequeñas partes para facilidad del TTS
def splitParagraphIntoSentences(paragraph):
    sentenceEnders = re.compile('[:,;.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList

#Definición de características del eSpeak TTS
#	-v:		Definición de voz masculina
#	-s140:		Definición de 140 palabras por minuto
#	es:		Definición del idioma español para lectura
def sound(spk):
        cmd_beg=" espeak -v es -s140 '"
        cmd_end="' | aplay"
        print cmd_beg+spk+cmd_end
        call ([cmd_beg+spk+cmd_end], shell=True)

while True:
	#Captura de imagen por medio de la cámara de la Raspberry Pi, se define sharpness = 100
	call ("raspistill -o image.jpg -t 1 -sh 100", shell=True)
	print "Imagen capturada"
	
	#Empezar el OCR Tesseract de la imagen capturada y guardarlo en out.txt
	call ("tesseract image.jpg out", shell=True)
	print "OCR completado"
	
	#Abrir el documento de texto y hacer las subdiviciones de este en pequeñas oraciones
	fname="out.txt"
	f=open(fname)
	content=f.read()
	print content
	sentences = splitParagraphIntoSentences(content)

	#Reproducción en audio de estas oraciones subdivididas
	for s in sentences:
		sound(s.strip())
