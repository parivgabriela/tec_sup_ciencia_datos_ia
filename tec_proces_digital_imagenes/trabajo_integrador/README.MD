# TÉCNICAS DE PROCES. DIGITAL DE IMÁGENES

## Procesamiento Digital de Imágenes - Proyecto Integrador

Este repositorio contiene un proyecto integrador desarrollado para la materia de Procesamiento Digital de Imágenes del IFTS 24. Consiste en una serie de ejercicios prácticos que exploran conceptos fundamentales del procesamiento de imágenes utilizando Python.
Contenido del Proyecto
El notebook incluye tres ejercicios principales:

### 1. Espacios de Color

Análisis de canales BGR/RGB
Separación de canales de color
Conversión entre espacios de color
Análisis de información por canal

### 2. Muestreo y Cuantización

Aplicación de muestreo espacial con diferentes factores (2, 4 y 8)
Cálculo de reducción de datos para cada caso
Aplicación de cuantización con diferentes niveles (32, 64, 128, 256)
Análisis visual de degradación de imagen
Generación de histogramas

### 3. Segmentación por Color

Segmentación basada en umbrales RGB
Histogramas de imagen en escala de grises
Detección de objetos por color
Cálculo de coordenadas para rectángulos delimitadores
Dibujo de bordes en objetos segmentados
Aplicación de operaciones morfológicas para refinar la segmentación

## Librerías Utilizadas

OpenCV (cv2): Principal librería para procesamiento de imágenes
NumPy: Manipulación eficiente de arrays y operaciones matemáticas
Matplotlib: Visualización de imágenes y generación de gráficos
Funciones personalizadas para facilitar el procesamiento y análisis

## Técnicas Aplicadas

Desenfoque Gaussiano
Operaciones morfológicas (apertura y cierre)
Detección de contornos
Histogramas de color
Transformaciones de color
Segmentación mediante máscaras

## Requisitos
Para ejecutar este notebook necesitarás:

pip install opencv-python numpy matplotlib

Imágenes Utilizadas
El proyecto utiliza varias imágenes de prueba, incluyendo:

Una imagen de un parque con flores para el análisis de espacios de color
Una imagen de astronautas en escala de grises para muestreo y cuantización
Una imagen de especias coloridas para segmentación por color

Autor
Gabriela Pari Vaca - IFTS 24

Proyecto desarrollado como trabajo integrador para la materia de Técnicas de Procesamiento Digital de Imágenes del Instituto de Formación Técnica Superior N°24.