#!/usr/bin/python

with open('/data/counter.txt', 'r') as f:
    text = f.read()
    text = int(text)
    text += 1
    text = str(text)

text_on_file = text

with open('/data/counter.txt', 'w') as g:
    g.write(text_on_file)

