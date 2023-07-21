# Nube_Dinamica_Palabras
Implementación de una nube dinámica de palabras, aplicada a un contexto político mexicano.
## Resumen
Una de las primeras etapas en el proceso de análisis de sentimientos, consiste en un estudio exploratorio de los documentos. La nube de palabras es una de las herramientas más usadas para la visualización resumida de estos datos. Una de las principales desventajas de las nubes de palabras comunes, es que no permitern visualizar los cambios en la polaridad de las opiniones durante el tiempo; tampoco  consideran teorías emocionales para una mejor compresión del fenómeno a estudiar. En este artículo se propone una modificaciíon gráfica de la dinámica de la evolución de la frecuencia y polaridad de palabras en documentos. Como caso de estudiop, se aplicó al contexto político mexicano actual. 

> Keywords: Análisis de sentimientos, SenticNet , nube de palabras.

## Objetivo general 
Diseñar e implementar una Nube Dinámica de Palabras para ser usada como una herramienta para la visualización de la evolución de la frecuencia de uso de palabras, y sus polaridades emocionales respecto al tiempo, mediante el modelo sentimental del marco de trabajo SenticNet.

#### Objetivos específicos
- Definir formalmente el concepto de Nube Dinámica de Palabras, en el que se consideran la frecuencia de las palabras, la temporalidad de los documentos que las contienen y su polaridad emocional.
- Presentar una metodología para la búsqueda y recolección sistemática de documentos en la plataforma de Twitter.
- Aplicar la metodología del objetivo anterior para recolectar documentos recientes relacionados con el contexto político mexicano.

## Métodología aplicada
Se utilizó el API Rest que proporciona Twitter cuando se genera una cuenta como desarrollador, para permitir el acceso al núcleo de datos y acceder a los tweets recientes. Así mismo, se utilizó la biblioteca Tweepy que contiene
la interfaz Cursor para iterar a través de distintos tipos de objetos (usualmente representados como objetos JSON).

Para el desarrollo del artículo, se utilizó SenticNet, con el objetivo de inferir la polaridad de las opiniones. SenticNet consta de un extractor de conceptos y de una biblioteca con hasta 14,000 conceptos clasificados según su positividad o negatividad, el resultado es un número flotante entre -1 y +1 (donde -1 es negatividad extrema y +1 es positividad extrema). 

A continuación se muestra un resumen gráfico de la metodología empleada. 

<img src="https://raw.githubusercontent.com/kerenmitsue18/Nube_Dinamica_Palabras/main/Metodolog%C3%ADa.png" alt="Metodología palicada" width="350px">

## Artículo de CIM 2022
El trabajo "**Nube dinámica de palabras basada en SenticNet para contexto
político mexicano "** fue publicado en la revista periódica del "COLOQUIO DE INVESTIGACIÓN MULTIDISCIPLINARIA" Volumen 10. Núm. 1, Octubre 2022. ISSN: 2007 8102
Link de la revista: http://depi.orizaba.tecnm.mx/Journals/Journal_CIM_2022.pdf

![Artículo CIM 2022](https://github.com/kerenmitsue18/Nube_Dinamica_Palabras/blob/main/Journal_CIM_2022%20Articulo%20Cloud.pdf)
> Elaborado por: Keren Mitsue Ramírez Vergara
