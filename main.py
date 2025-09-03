import pdfplumber
import os
from ai_summary import *
from text_to_audio import *

pdfs = []
summaries = []
for article in os.listdir('./articles_example'):
    if article.endswith('.pdf'):
        with pdfplumber.open(f'./articles_example/{article}') as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
            pdfs.append({'file_name': article, 'content': text})
summary = summarise_text(pdfs[0]['content'])

text_to_audio(summary)


for pdf in pdfs:
    summaries.append({'article_name':pdf['file_name'],'summary':summarise_text(pdf['content'])})

for summary in summaries:
    text_to_audio(summary['summary'])
