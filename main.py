#This file reads a PDF as an audio file
#There is an option to save the file as an MP3. Uncomment it to run.

import PyPDF3
import pyttsx3
import pdfplumber

#Type in the path to the file you want read aloud
text_file = "cat_ipsum.pdf"

book = open(text_file, "rb")
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages

#Extract the text
finalText = ""

#Loop through the pages to read them 
with pdfplumber.open(text_file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

#Converting text to audio
#This is the option to save to a file; uncomment and type your path here:
# engine = pyttsx3.init()
#engine.save_to_file(finalText, "lorem.mp3")
# engine.runAndWait()

#Reading the file only without saving
engine = pyttsx3.init()
engine.say(finalText)
engine.runAndWait()