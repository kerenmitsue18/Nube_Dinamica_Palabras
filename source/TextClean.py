# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
Tercera BIENAL estudiantil de ciencias y tecnología
Autor: Keren Mitsue Ramírez Vergara
Asesor: Dr. Asdrúbal López Chau
Descripción:
    
    Clase para recolpilar datos 

Created on Sun May 29 20:43:04 2022

@author: KerenMitsue
"""
from unidecode import unidecode_expect_nonascii
import nltk
import string
from nltk.corpus import stopwords

class TextClean:
    
    def __init__(self):
        '''
        

        Returns
        -------
        None.

        '''
        self.vacias = stopwords.words('spanish')
        othersWords = ['va', 'vas', 'vez','van','vamos','ve', 'mientras', 'ante', 'meses', 
                       'sin', 'tras',
                 'para','cabe','cuenta', 'dias',  'dia', 'en', 'asi','hace','hacer',
                 'tal','hecho', 'decir','dices', 'dijo','digo', 'dice','dicen','dio', 'debe',
                 'de', 'pues','das', 'tan', 'ser', 'aqui', 'ver', 'tener', 'oye', 'solo',
                 'sera', 'aun', 'mas','si', 'que', 'siendo',  'nunca', 'igual', 'tambien',
                 'ademas', 'aunque', 'puede', 'quieren', 'quiere', 'quienes', 'gran',
                 'cierto', 'cada', 'sabe', 'creo', 'usted', 'ustedes','despues', 'cuanto',
                 'todo', 'toda', 'todos', 'todas', 'dar', 'da', 'ahi','parece', 'pareces',
                 'entonces', 'ningun', 'saber', 'sabe','sabemos', 'misma', 'mejor',
                 'mismo', 'deja', 'ahora', 'dime', 'bien', 'traves', 'estan', 'embargo',
                 'pueden', 'sigue', 'solo', 'habia', 'luego', 'sino', 'seria', 'etc'
                 'segun', 'hacen', 'nadie', 'sido', 'hara']
        self.vacias.extend(othersWords)

    
    def clean(self, textLine):
        textLine = self.unidecode(textLine)
        textLine = self.removeSpaces(textLine)
        textLine = self.removeSymbols(textLine)
        textLine = textLine.split()
        words = self.getwords(textLine)
        if  len(words) !=0:
            for word in words:
                textLine.remove(word)
        text = " ".join(textLine)       
        return self.remove_stopwords(text)

    def unidecode(self, textLine):
        return unidecode_expect_nonascii(textLine)
    
    def removeSpaces(self, textLine):
        textLine = textLine.replace("\n", "")
        textLine = textLine.strip()
        return textLine
    
    def removeSymbols(self, textLine):
        symbols = [",","'","´", "|", ".", "`",'"',"'", "-", "``"]
        for symbol in symbols:
            if symbol in textLine:
                textLine = textLine.replace(symbol, "")
            textLine = textLine.strip()
        return textLine
    
    
    def remove_stopwords(self, text):
        temp = []
        tokens = nltk.tokenize.word_tokenize(text, language="spanish")
        if len(tokens)==0:
            pass
        for token in tokens:
            if len(token)>1:
                if token.lower() not in self.vacias:
                    if not token.isdigit():
                        if token.lower() not in string.punctuation:
                            temp.append(token.lower()) 
        return temp
    
    def getwords(self,textLine):
        words = []
        for word in textLine:
            if "#" in word or "@" in word or "https" in word or "http" in word:
                words.append(word)
        return words
