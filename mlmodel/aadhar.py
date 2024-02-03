import re
import json
import pytesseract
import cv2
import numpy as np
import sys
import re
import os
from PIL import Image
import ftfy
import io
import pickle
import requests


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def adhaar_read_data(text):
    res=text.split()
    name = None
    dob = None
    adh = None
    sex = None
    nameline = []
    dobline = []
    text0 = []
    text1 = []
    text2 = []
    lines = text.split('\n')
    for lin in lines:
        s = lin.strip()
        s = lin.replace('\n','')
        s = s.rstrip()
        s = s.lstrip()
        text1.append(s)

    if 'female' in text.lower():
        sex = "FEMALE"
    else:
        sex = "MALE"

    text1 = list(filter(None, text1))
    text0 = text1[:]
    
    try:

        # Cleaning first names
        name = text0[0]
        name = name.rstrip()
        name = name.lstrip()
        name = name.replace("8", "B")
        name = name.replace("0", "D")
        name = name.replace("6", "G")
        name = name.replace("1", "I")
        name = re.sub('[^a-zA-Z] +', ' ', name)

        # Cleaning DOB
        dob = text0[1][-10:]
        dob = dob.rstrip()
        dob = dob.lstrip()
        dob = dob.replace('l', '/')
        dob = dob.replace('L', '/')
        dob = dob.replace('I', '/')
        dob = dob.replace('i', '/')
        dob = dob.replace('|', '/')
        dob = dob.replace('\"', '/1')
        dob = dob.replace(":","")
        dob = dob.replace(" ", "")

        # Cleaning Adhaar number details
        aadhar_number=''
        for word in res:
            if len(word) == 4 and word.isdigit():
                aadhar_number=aadhar_number  + word + ' '
        if len(aadhar_number)>=14:
            print("Aadhar number is :"+ aadhar_number[0:14])
        else:
            print("Aadhar number not read")
        adh=aadhar_number

        

    except:
        pass

    data = {}
    data['Name'] = name
    data['Date of Birth'] = dob
    data['Adhaar Number'] = adh
    data['Sex'] = sex
    data['ID Type'] = "Adhaar"
    return data
def findword(textlist, wordstring):
    lineno = -1
    for wordline in textlist:
        xx = wordline.split( )
        if ([w for w in xx if re.search(wordstring, w)]):
            lineno = textlist.index(wordline)
            textlist = textlist[lineno+1:]
            return textlist
    return textlist

img = cv2.imread(r'img')
img = cv2.resize(img, None, fx=2, fy=2,interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
var = cv2.Laplacian(img, cv2.CV_64F).var()
if var < 50:
    print("Image is Too Blurry....")
    k= input('Press Enter to Exit.')
    exit(1)


text = pytesseract.image_to_string(Image.open(r'img'), lang = 'eng')

text_output = open('output.txt', 'w', encoding='utf-8')
text_output.write(text)
text_output.close()

file = open('output.txt', 'r', encoding='utf-8')
text = file.read()

text = ftfy.fix_text(text)
text = ftfy.fix_encoding(text)


data = adhaar_read_data(text)






