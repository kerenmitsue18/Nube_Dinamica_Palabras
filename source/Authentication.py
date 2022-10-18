# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
Tercera BIENAL estudiantil de ciencias y tecnología
Autor: Keren Mitsue Ramírez Vergara
Asesor: Dr. Asdrúbal López Chau
Descripción:
    
    Clase para autenticar la sesión en la API Rest de Twitter

Created on Sat Jul 16 19:39:21 2022

@author: KerenMitsue
"""

import tweepy


class Authentication:
    
    def getAuth(self):
        '''
        Obtener la conexión con API Rest de Twitter

        Returns
        -------
        Objeto API
            Objeto para utilizar el API Rest.

        '''
        #cadenas de autenticacion 
        consumer_key = "cIdb0l9E6Gi5gSoKrSRdHjUao"
        consumer_secret = "RVBl6rIyklTrrrn1UfNB0poPeWCIbcTSkPDgw6QT9dkTe2Wuk0"
        access_token = "1519391083427508224-knxEk64zGQmMIZnTruCHz9duqIWMP1"
        access_token_secret = "7AT1NNC3oR6EbFCCbgpW3F4YzopxK2eslLnEnZ45sBlr2"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
    
        return tweepy.API(auth, wait_on_rate_limit=True)



            