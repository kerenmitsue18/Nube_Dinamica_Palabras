# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Inteligencia Artificial
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Asesor: Dr. Asdrúbal López Chau
Descripción: 

Created on Tue Jun 28 21:08:09 2022

@author: KerenMitsue
"""
from CloudWords import CloudWords
from AnalysisSenticNet import SenticNetClass
from TextClean import TextClean
from datetime import timedelta, datetime
from collections import Counter

class WCDinamic:
    
    def __init__(self):
        self.wc = CloudWords()
        self.tc = TextClean()
        self.frecuency = None
        self.polarity = []
        self.sn = SenticNetClass()
        self.tweets = []

    def WCTime(self, df, wideWindow = timedelta(days=1) , step =timedelta(hours=12) ):
        if wideWindow < step:
            print('No se puede realizar la nube dinámica de palabras')
        else:
            dates = list(df['Created_at'])
            maxDate = self.maxDate(dates)
            minDate = self.minDate(dates)
            
            firstDate = minDate
            nextDate = firstDate + wideWindow
            tempfirst = firstDate
            templast = nextDate
            
            while firstDate < maxDate:
                
                #verificar la primera iteracion 
                if firstDate == minDate:
                    self.tweets = self.selectTweets(df, firstDate, nextDate)
                    data = self.tokenizar(self.tweets)
                    self.polarity = self.calculatePolarity(data)
                    data = [ d for d in data.split() if d in list(self.polarity.keys())  ]
                    self.frecuency = self.calculateFrecuency(data)
                    
                else:
                    #removetweets 
                    temptweets = self.selectTweets(df, tempfirst, firstDate)
                    tempdata = self.tokenizar(temptweets)
                    self.updatePolarity(tempdata, True) 
                    data = [ d for d in tempdata.split() if d not in list(self.polarity.keys())  ]
                    self.updateFrecuency(data, True)
                    self.updateTweets(temptweets, True)
                    
                    #add tweets
                    tempdate = nextDate - templast
                    temptweets = self.selectTweets(df, templast,templast + (nextDate-templast))
                    tempdata = self.tokenizar(temptweets)
                    self.updatePolarity(tempdata, False) 
                    data = [ d for d in tempdata.split() if d in list(self.polarity.keys())  ]
                    self.updateFrecuency(data, False)
                    self.updateTweets(temptweets, False)  
                
                #All wordcloud
                period = "Del "+  str(firstDate)  + " al " + str(nextDate)
                wordcloud = self.wc.wordCloud(self.frecuency, 'all')
                self.wc.graphWordCloud(wordcloud,period)     
                    
                print("Polarity :\n", self.polarity)
                print("frecuency : \n ", self.frecuency )
                period = "Del "+  str(firstDate)  + " al " + str(nextDate)                
                               
                #Negative wordcloud
                frecNegative = self.getWords('negative')
                wordcloud = self.wc.wordCloud(frecNegative, 'negative')
                self.wc.graphWordCloud(wordcloud,period) 
                
                #Positive wordcloud
                frecPositive = self.getWords('positive')
                wordcloud = self.wc.wordCloud(frecPositive, 'positive')
                self.wc.graphWordCloud(wordcloud,period) 
                
                #Neutral wordcloud
                frecNeutral = self.getWords('neutral')
                wordcloud = self.wc.wordCloud(frecPositive, 'neutral')
                self.wc.graphWordCloud(wordcloud,period) 
                
                
                
                tempfirst = firstDate
                templast = nextDate
                firstDate +=step
                nextDate += wideWindow    

    def minDate(self, dates):
        return datetime.fromisoformat(dates[0]).replace(tzinfo=None)
    
    def maxDate(self, dates):
        return datetime.fromisoformat(dates[-1]).replace(tzinfo=None)
    
    
    def selectTweets(self, df, firstDate, secondDate):
         dfTweets =  df.loc[(df['Created_at'] >= str(firstDate))
                              & (df['Created_at'] < str(secondDate))]
         return list(dfTweets['tweetText'] )
    
    def tokenizar(self, tweets):
        data = ''
        for tweet in tweets:
            tweet = self.tc.clean(tweet)
            data += " ".join(tweet)+ " "
        return data   

    def updateTweets(self, temptweets, remove=True):
        if remove:
            self.removeTweets(temptweets)
        else:
            self.addTweets(temptweets)
            
    def updateFrecuency(self, words, remove = True):
        tempfrecuency = self.calculateFrecuency(words)
        if remove:
            self.removeFrecuency(tempfrecuency)
        else:
            self.addFrecuency(tempfrecuency)
    
    def updatePolarity(self, tempdata, remove= True):
        tempolarity = self.calculatePolarity(tempdata)   
        if remove:
            self.removePolarity(tempolarity)
        else: 
            self.addPolarity(tempolarity)
            
           
    def removeTweets(self, temptweets):
        if len(temptweets)>0:
            for tweet in temptweets:
                try: 
                    self.tweets.remove(tweet)
                except:
                    pass
    
    def removeFrecuency(self,frecuency):       
        frecuency = { word:value for (word,value) in frecuency.items() if value>0}
        self.frecuency.subtract(frecuency)
        self.frecuency = Counter({ word:number for (word, number) in self.frecuency.items() if number>0 and word in self.polarity  })
        
    def removePolarity(self, polarity):
        for key in polarity.keys():
            try:
                del self.polarity[key]
            except:
                pass
                    
    def addTweets(self, temptweets):
        if len(temptweets)>0:
            for tweet in temptweets:
                self.tweets.append(tweet)
                
    def addFrecuency(self, frecuency):
        self.frecuency.update(frecuency)
    
    def addPolarity(self, polarity):
        self.polarity.update(polarity)
        
    def calculateFrecuency(self, words): #words is a list
        return  Counter(words)

    def calculatePolarity(self, words):
        dicPolarity = self.sn.getPolarity(words)
        newPolarity = { word:polarity for (word,polarity) in dicPolarity.items() if polarity !='null'}
        return newPolarity
    
    def getMoodTags(self, words):
        return self.sn.getMoods(words)

    def getWords(self, typePolarity= 'neutral'):
        dic_words = {word:polarity for (word, polarity) in self.polarity.items() if polarity== typePolarity }
        key_words = list(dic_words.keys())
        return { word:number for (word, number) in self.frecuency.items() if word in key_words }
    


        