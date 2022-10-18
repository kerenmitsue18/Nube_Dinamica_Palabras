# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
Tercera BIENAL estudiantil de ciencias y tecnología
Autor: Keren Mitsue Ramírez Vergara
Asesor: Dr. Asdrúbal López Chau
Descripción:
    
    Clase para obtener emociones y polaridad 
    basadas en SenticNet de un corpus

Created on Sat Jul 16 19:39:21 2022

@author: KerenMitsue
"""


from senticnet.senticnet import SenticNet
import numpy as np

class SenticNetClass:
    
    
    def __init__(self):
        '''
        Constructor con objeto SenticNet

        Returns
        -------
        None.

        '''
        self.sn = SenticNet()
    
    def getMoods(self, words):
       '''
        Obtener los moods de una lista de palabras

        Parameters
        ----------
        words : List
            Lista de palabras

        Returns
        -------
        moodtags : List
            Lista de moodtags que existen en la lista de palabras 

        ''' 
       set_moodtags = set()
       for word in words:
            try:
                moodtags = self.sn.moodtags(word)
                for mt in moodtags:
                    set_moodtags.add(mt)
            except:
                pass
       moodtags = list(set_moodtags)
       moodtags.sort()
       return moodtags       
    
    def getSemantics(self, words):
        '''
        Obtener la semántica de una lista de palabras

        Parameters
        ----------
        words : List
            Lista de palabras

        Returns
        -------
        semantics : List
            Lista de semántica que existen en la lista 

        '''
        set_semantics = set()
        for word in words:
            try:
                semantics = self.sn.semantics(word)
                for mt in semantics:
                    set_semantics.add(mt)
            except:
                pass
        semantics = list(set_semantics)
        semantics.sort()
        return semantics       
            
    def getPolarity(self, words):
        '''
        Obtener la polaridad de una lista de palabras

        Parameters
        ----------
        words : List
            Lista de palabras

        Returns
        -------
        Dict
            Diccionario con la estructura (palabra: polaridad),
            si no existe la palabra en SenticNet, la polaridad es 'null'

        '''
        polarity = []
        for word in words:
            try:
                x = self.sn.concept(word)
                value = float(x.get('polarity_value'))
                value = np.abs(value)
                polarity.append(value)
            except:
                polarity.append('null')
                
        return dict(zip(words, polarity))               
    
    def getMood(self, words):
        '''
        Obener los moods de cada elemento de la lista de palabras

        Parameters
        ----------
        words : List
            Lista de palabras

        Returns
        -------
        Dict
            Diccionario con la estructura (palabra: moods),
            si no existe la palabra en SenticNet, el mood es 'null'

        '''
        moods = []
        for word in words:
            try:
                x = self.sn.concept(word)
                moods.append(x.get('moodtags'))
            except:
                moods.append('null')               
        return dict(zip(words,moods))   
    
    
'''
sentic  = SenticNetClass()
t = ['que', 'que', 'buena', 'pelicula', 'pablo', 'gasolina', 'las', 'mentiras', 'de', 'amlo', 'gas' ,'bienestar', 'aeropuerto', 'aifa', 'sin', 'vuelo']
print(sentic.getMoods(t))

polarity = sentic.getPolarity(t)
print(polarity)
'''