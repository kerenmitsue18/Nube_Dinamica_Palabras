# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
Tercera BIENAL estudiantil de ciencias y tecnología
Autor: Keren Mitsue Ramírez Vergara
Asesor: Dr. Asdrúbal López Chau
Descripción:
    
    Clase para recolpilar datos 

Created on Wed Jul  6 23:04:43 2022
@author: KerenMitsue
"""


import tweepy
import pandas as pd
from Authentication import Authentication
import csv
import numpy as np
import random
import collections

class SelectData:
    
        
    def __init__(self, iterations=2):
        '''
        Constructor de la clase SelecData

        Parameters
        ----------
        iterations : int, optional
            Número de iteraciones que se realizará para recopilar datos. The default is 2.

        Returns
        -------
        None.

        '''
        self.keywords = ['4T', 'obrador', 'amlo','ElPeorPresidenteDeLaHitoria' ,'ConferenciaPresidente', 'AmloLiderMundial', 'AmloNarcoDictador', 'AmloLaVerguenzaDeMexico', 'AMLOTraidorALaPatria' ]
        self.iterations = iterations
    
    def toDataFrame(self, tweets):
        '''
          Converir  documentos a un DataFrame
        Parameters
        ----------
        tweets : List
            Lista de documentos

        Returns
        -------
        data : pandas
            DataFrame de documentos

        '''
        data = pd.DataFrame(columns= ['Created_at','user_id','screen_name','tweetText','reply_status_id',
                 'reply_to_screen_named','lang','retweeted','place','reply_user_id','hashtags'])
        for tweet in tweets:
            data['Created_at'] = [tweet.created_at for tweet in tweets]
            data['user_id'] = [tweet.user.id for tweet in tweets]
            data['screen_name'] =  [tweet.user._json['screen_name'] for tweet in tweets]
            data['tweetText'] = [tweet.full_text for tweet in tweets]
            data['reply_status_id'] =  [tweet.in_reply_to_status_id for tweet in tweets]
            data['reply_to_screen_named'] =  [tweet.in_reply_to_screen_name for tweet in tweets]
            data['lang'] =  [tweet.lang for tweet in tweets]
            data['retweeted'] =  [tweet.retweeted for tweet in tweets]
            tweets_place= []
            tweets_reply_user_id = []
            hashtags = []
            
            for tweet in tweets:
                if tweet.place:
                   tweets_place.append(tweet.place.full_name)
                else:
                   tweets_place.append('null')
                if tweet.in_reply_to_user_id is not None:
                    tweets_reply_user_id.append(tweet.in_reply_to_user_id )
                else:
                    tweets_reply_user_id.append(0)
                hashtags.append([h['text'] for h in tweet.entities['hashtags']])
                
            data['place'] = [i for i in tweets_place]
            data['reply_user_id'] = [i for i in tweets_reply_user_id]
            data['hashtags'] = [i for i in hashtags]

        return data
    
        
    def searchTweets(self, keyword, results):
        '''
        Búsqueda de documentos en API Rest en Twitter

        Parameters
        ----------
        keyword : List
            Lista de palabras claves (Hashtags) a buscar
        results : List
            Lista de documentos encontrados en Twitter

        Returns
        -------
        None.

        '''
        date_since = "2018-12-01"
        cursor = tweepy.Cursor(api.search_tweets, keyword + "-filter:retweets", lang="es", since_id=date_since, tweet_mode= "extended", count=50000).pages(900)
        for page in cursor: # Remove the limit to 100
            for item in page:
                if item not in results:
                    results.append(item)      
                    
    def numSampling(self, N):
        '''
        Obtener el tamaño de muestreo

        Parameters
        ----------
        N : int
            tamaño de población (cantidad de documentos).

        Returns
        -------
        int
            tamaño de muestreo.

        '''
        z = 1.644854
        p = 0.6
        e = 0.1  #modificar
        denom =  np.power(z,2) * p * (1-p)/ np.power(e,2)
        num = 1 + (  (np.power(z,2) * p * (1-p)) / ( np.power(e,2) * N ) )
        sampling = denom/num
        return int(sampling)

    def samplingTweets(self, data):
        '''
        Selecciona elementos de muestreo 

        Parameters
        ----------
        data : pandas
            DataFrame de documentos.

        Returns
        -------
        selected : List
            Documentos seleccionados en el muestreo.

        '''
        num = self.numSampling(len(data))
        selected = random.sample(data, k=num)
        return selected
        
    def removeTweet(self, select, res):
        '''
        Remueve Teewts de una lista

        Parameters
        ----------
        select : str
            documento a eliminar
        res : List
            Lista de documentos de la muestra

        Returns
        -------
        None.

        '''
        res.remove(select);
    
    def manualSelection(self, selected,results):
        '''
        Permite seleccionar manualmente los documentos relevantes en el muestro. 
        Si no son relevantes, se eliminan del corpus

        Parameters
        ----------
        selected : List
            Lista de documentos en la muestra.
        results : List
            Lista de documentos descargados.

        Returns
        -------
        res : TYPE
            DESCRIPTION.

        '''
        res = results.copy()
        for select in selected:
            print("\n" + select.full_text)
            op = input("El tweet es relevante? \n 1. SI \n 0. No \n")
            if op == '0':
                self.removeTweet(select,res)
        return res
            
    def getHashtags(self, results):
        '''
        Obtención de hashtags de un conjunto de documentos

        Parameters
        ----------
        results : List
            Lista de documentos descargados.

        Returns
        -------
        hashtags : List
            Lista de hashtags encontrados en docuementos.

        '''
        hashtags = [] 
        for res in results:
            hashtags.append([h['text'] for h in res.entities['hashtags']])
        return hashtags
    
   
    def expandKeywords(self, keywords):
        '''
        Agregar elementos a la lista inicial de palabras clave

        Parameters
        ----------
        keywords : List
            Lista de Hashtags.

        Returns
        -------
        keywords : List
            Lista extendida de Hashtags.
        '''
        
        keywords = [keyword for keyword in keywords if len(keyword)>0] 
        words = []
        for k in keywords:
            if len(k)>1:
                for i in range (len(k)):
                    if k[i] not in self.keywords:
                        words.append(k[i])
            else:
                
                if k[0] not in self.keywords:
                    words.append(k[0])     
        count = collections.Counter(words)
        keywords = [key for key, _ in count.most_common(10)]
        return keywords
        
  
    def saveData(self, data, keyword):
        '''
        Guardar un DataFrame en un archivo .csv
        Su estructura es: palabraClave.csv

        Parameters
        ----------
        data : pandas
            DataFrame de documentos.
        keyword : List
            Hastags o palabras clave con las que se buscaron los docuementos.

        Returns
        -------
        None.

        '''
        data = select.toDataFrame(data)
        data.to_csv("../data/"+keyword+".csv", encoding= 'utf-8', index=True)
        
    def resultsxKey(self, data, keywords):
        '''
        Selecciona los documentos pertenecientes a las palabras clave
        y los guarda

        Parameters
        ----------
        data : List
            Documentos del corpus.
        keywords : List
            Hastags o palabras clave con las que se buscaron los docuementos.

        Returns
        -------
        None.

        '''
        for keyword in keywords:
                res = [tweet for tweet in self.results if keyword in tweet.full_text]
                self.saveData(res,keyword)
                print("guardado ", keyword)

    def collectionData(self):
        '''
        Recopilación de documentos de Twitter

        Returns
        -------
        None.

        '''
        keywords = self.keywords 
        for i in range(self.iterations):
            self.results = []
            for keyword in keywords:
                #print("Keyword a buscar ", keyword) 
                self.searchTweets(keyword, self.results)
                #print("Keyword buscada ", keyword)    
            selected = self.samplingTweets(self.results) #retorna los tweets seleccionados
            final = self.manualSelection(selected,self.results)
            
            #separar los resultados por keywords
            self.resultsxKey(final, keywords)
            #print("Ya se han guardado exitosamente")
            #expandir nuevas palabras a buscar
            if(i<self.iterations-1):
                keywords = self.expandKeywords(self.getHashtags(final))
                for k in keywords:
                    self.keywords.append(k)


api = Authentication()
api = api.getAuth()
select = SelectData(4) #4 -> número de iteraciones que realizará

select.collectionData()

