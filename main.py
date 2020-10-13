import pyttsx3
import PyPDF2
import sys

speaker = pyttsx3.init()
speaker.setProperty("rate", "100")
speaker.setProperty("volume", "50")
it_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


def init():
    if len(sys.argv) > 1:
        file= sys.argv[1]
        book = open(file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages

        for num in range(17, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.setProperty('voice', it_voice_id)
            speaker.say(text)
            speaker.save_to_file(pages, "audio.mp3")
            speaker.runAndWait()



    else:
        print ("\npython main.py FILENAME.pdf")


init()
