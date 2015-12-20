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
	#Empezar el OCR Tesseract de la imagen y guardarlo en out-test.txt
	call ("tesseract image-test.jpg out-test", shell=True)
	print "OCR completado"
	
	#Abrir el documento de texto y hacer las subdiviciones de este en pequeñas oraciones
	fname="out-test.txt"
	f=open(fname)
	content=f.read()
	print content
	sentences = splitParagraphIntoSentences(content)

	#Reproducción en audio de estas oraciones subdivididas
	for s in sentences:
		sound(s.strip())
