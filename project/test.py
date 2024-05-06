#from melo.api import TTS
from PyPDF2 import PdfReader

# Speed is adjustable
speed = 0.8
device = 'cpu' # or cuda:0

#text = "我最近在学习machine learning，希望能够在未来的artificial intelligence领域有所建树。"
# model = TTS(language='ZH', device=device)
# speaker_ids = model.hps.data.spk2id



reader = PdfReader("/Users/siyuanhe/code/files/example.pdf")

text = ''
number_of_pages = len(reader.pages)
for pageNum in range(11, 15):
  #page = reader.pages[pageNum].extract_text().replace('-\n', '')
  page = reader.pages[pageNum].extract_text().replace('-\n', '')
  #page = page.replace('\n', '')
  print(page)
  # American accent
  text = text + page
  print('finish one page')
print("the end")
# output_path = 'xiaobo.wav'
# model.tts_to_file(text, speaker_ids['ZH'], output_path, speed=speed)
