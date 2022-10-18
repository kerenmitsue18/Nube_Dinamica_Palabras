# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
Tercera BIENAL estudiantil de ciencias y tecnología
Autor: Keren Mitsue Ramírez Vergara
Asesor: Dr. Asdrúbal López Chau
Descripción:
    
    Clase principal para genenar la nube dinámica de palabras

Created on Wed Jul  6 23:04:43 2022
@author: KerenMitsue
"""



from datetime import timedelta
import pandas as pd
from WCDinamic2 import WCDinamic2

df = pd.read_csv("../data/amlo.csv")
df = df.sort_values(by="Created_at")


wdt = WCDinamic2()
wideWindow = timedelta(days=4)
step = timedelta(hours=72)
wdt.WCTime(df,wideWindow,step)
