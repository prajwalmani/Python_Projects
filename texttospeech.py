#  PYTHON PROGRAM FOR TEXT TO SPEECH
# gtts module is used for the conversion and os is used open the mmp3 file
from gtts import gTTS
import os

# eg.txt file which contains the text for the program to convert into speech
with open('eg.txt', 'r') as myfile:
    # to read the text from file to the string
    data = myfile.read()
l = "en"
o = gTTS(text=data, lang=l, slow=False)
# To save the mp3 file
o.save("w.mp3")
# To open the saved mp3 file
os.system(" w.mp3")
