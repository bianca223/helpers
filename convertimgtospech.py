from PIL import Image
import pytesseract
import pyttsx3

from googletrans import Translator


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
image = Image.open('img.png')
text = pytesseract.image_to_string(image, lang="eng")
with open('abc.txt',mode ='w') as file:     
                 file.write(text)
                 print(text)
p = Translator()
k = p.translate(text,dest='ro')
print(k.text)
engine = pyttsx3.init()

engine.say(k.text)
engine.runAndWait()