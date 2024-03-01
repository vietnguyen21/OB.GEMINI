import google.generativeai as genai
import textwrap
from IPython.display import Markdown
import pyttsx4

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
API_key = 'AIzaSyA2BZg4Ngyb5x1F0HwYrFXCr0gzXbv1ZT0'

genai.configure(api_key=API_key)

model = genai.GenerativeModel('gemini-pro')

input_text = str(input('type your question: '))
response = model.generate_content(input_text)

to_markdown(response.text)

for chunk in response:
  print(chunk.text)

try:
  voice = pyttsx4.init()
  voice.setProperty('rate', 160)
  voice.say(str(response.text))
  voice.runAndWait()
except:
  print('end')