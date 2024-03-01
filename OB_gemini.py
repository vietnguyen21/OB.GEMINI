#import libary

import PySimpleGUI as sg
import google.generativeai as genai
import textwrap
from IPython.display import Markdown
import pyttsx4

#markdown function get on document to set the text
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#API KEY
API_key = 'AIzaSyA2BZg4Ngyb5x1F0HwYrFXCr0gzXbv1ZT0'

#verify api and set model 
genai.configure(api_key=API_key)
model = genai.GenerativeModel('gemini-pro')
history = []

#layout setting
sg.theme('GreenMono')

layout = [
    [sg.Input(size = (50,20),key = "TEXT-INPUT")],
    [sg.Button("Get",size=(20,1), key="get")],
    [sg.Button("Speech",size=(20,1),key='speak')],
    [sg.Multiline(size=(800,500),key='RESPONSE',autoscroll = True)],
    [sg.Text(size=(10,1),key='ERROR')]
]

window = sg.Window("OB.GEMINI", layout,size=(900,600))

#function setting
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'get':
        get = str(values['TEXT-INPUT'])
        response = model.generate_content(get)
        to_markdown(response.text)
        history.append(response.text)
        window["RESPONSE"].update(response.text)
        if event == 'speak':
            engine = pyttsx4.init()
            engine.setProperty('rate', 160)
                
            # Speak the response
            engine.say(str(response.text))
            engine.runAndWait()
            

