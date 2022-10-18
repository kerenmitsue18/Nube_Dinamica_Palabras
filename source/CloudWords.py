# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
Tercera BIENAL estudiantil de ciencias y tecnología
Autor: Keren Mitsue Ramírez Vergara
Asesor: Dr. Asdrúbal López Chau
Descripción:
    
    Clase para generar una nube de palabras 

Created on Sat Jul 16 19:39:21 2022

@author: KerenMitsue
"""


from wordcloud import WordCloud
import matplotlib.pyplot as plt
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.corpus import stopwords
from TextClean import TextClean
import random


class CloudWords:
 
    def __init__(self):
        '''
        Constructor de la clase CloudWords

        Returns
        -------
        None.

        '''
        self.textClean = TextClean()
        self.colors =dict({
            #red
            '#anger': [359.5,100,50], 
            '#rage': [0.3, 100, 42],
            '#annoyance': [359,100,77],

            #yellow
            '#serenity': [62.1, 80, 79], 
            '#joy': [ 52.5,92,52], 
            '#ecstasy': [52.5, 99, 59],
            '#contentment': [53.3, 73, 86], 
            
            #blue
            '#acceptance': [189.3, 58, 76],
            '#pleasantness':[188,79,49],
            '#delight': [186.5, 94, 39],
            '#amazement': [203, 98,44],
            '#surprise': [203.8, 98, 67],
            '#distraction': [200.5,84,81],
            '#sadness': [200,65,55], 
            '#grief': [240,100,39],
            
            #orange
            '#vigilance': [29, 100,50],
            '#anticipation': [29,99,66],
            '#interest': [28,100,78],
            '#calmness': [ 33.4, 100, 60], 
            '#bliss': [33.5, 94,55],
            
            #green
            '#disgust':[ 127, 32, 70],
            '#deslike': [128,29,80],
            '#loathing': [118.5, 37,57],
            '#trust': [120,99,66],
            
            #pink
            '#eagerness': [ 334,81,73],
            '#enthusiasm': [331,82,64],
            '#responsiveness': [328,62,83],
            '#boredom': [300,100,89],
            
            #purple
            '#anxiety': [260,27,74],
            '#fear': [ 265,33,69],
            '#terror': [262,28,44],
            '#pensiveness': [240,100,77]   
            })
        
    def colorwc(self,word=None, font_size=None, position=None, orientation=None, random_state=None, **kwargs):
        '''
            Generación de un color para la nube de palabras        
        
        Parameters
        ----------
        word : str, optional
            Palabras a utilizar en el wordcloud. The default is None.
        font_size : str, optional
            Tamaño del wordcloud. The default is None.
        position : int, optional
            Posición del gráfico. The default is None.
        orientation : int, optional
            Orientación del gráfico. The default is None.
        random_state : int, optional
            números aleatorios. The default is None.
        Returns
        -------
        str
            Color para la nube de palabras

        '''
        return "hsl({}, {}%, {}%)".format(self.color[0],self.color[1],self.color[2])

    
    
    def wordCloud(self,frecuency, mood = 'all'):          
        '''
        Genera una nube de palabras

        Parameters
        ----------
        frecuency : Dict
            Diccionario con la estructura (palabras: frecuencia)
            La frecuencia considera la ponderación de la polaridad
        mood : str, optional
            Si el mood es 'all', se utiliza un color por defecto para el wordcloud, 
            de lo contrario, se asigna el color correspondiente a la emoción
            The default is 'all'.

        Returns
        -------
        wordcloud : Objeto wordcloud
            Nube de palabras

        '''
        stopWords = stopwords.words('spanish')
        wordcloud = WordCloud(width = 800, height = 800,
                        background_color ='white',
                        stopwords = stopWords,
                        collocations = False,
                        min_font_size = 16).generate_from_frequencies(frecuency)      
        if mood != 'all':
            self.color = self.getColor(mood)
            wordcloud.recolor(color_func=self.colorwc)
        return wordcloud


    def graphWordCloud(self, wordcloud, period):
        '''
        Genera el gráfico de la nube de palabras

        Parameters
        ----------
        wordcloud : Objeto wordcloud
            Objeto de la nube de palabras
        period : str
            Titulo del gráfico a mostrar

        Returns
        -------
        None.

        '''
        plt.figure(figsize = (5,5), facecolor = None)
        plt.title(period)
        plt.imshow(wordcloud)
        plt.axis("off")
    

    def getColor(self, mood):
        '''
        Obtener el color correspondiente a una emocion

        Parameters
        ----------
        mood : str
            emoción de SenticNet

        Returns
        -------
        color : array
            Arreglo de valores rgb para un color 

        '''
        for key, value in self.colors.items():
            if key == mood:
                color = value
        
        if len(color) == 0:
            color = [0,0,0]
        return color
                
        


    



