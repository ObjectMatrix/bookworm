import pyttsx3
import PyPDF2

name = pdfFileName = './books/god.pdf'
book = open(pdfFileName, 'rb')
reader = PyPDF2.PdfFileReader(book)
totalPages = reader.numPages
print(totalPages)
engine = pyttsx3.init()

voiceRate = 180
engine.setProperty('rate', voiceRate)

startPage = 11
for num in range(startPage, totalPages):
  page = reader.getPage(num)
  text = page.extractText()
  engine.say(text)
  engine.runAndWait()
