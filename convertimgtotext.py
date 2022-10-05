from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
image = Image.open('img.png')
text = pytesseract.image_to_string(image, lang="eng")
print(text)