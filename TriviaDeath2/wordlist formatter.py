import os, re

os.chdir(r'C:\Users\moorh\Documents\GitHub\JakobujoTradukejo\TriviaDeath2')
source = open('esperanto-vortlisto.txt', 'r', encoding= 'utf-8')
dic = source.read()

password = ''

for vorto in re.findall(re.compile(r'''\n\w\w\w\w \;'''), dic):
    vorto = vorto.replace(r' ;', '')
    password += vorto

outputFile = open('wordlistPasswordEo.txt', 'w', encoding= 'utf-8')
outputFile.write(password)
outputFile.close()