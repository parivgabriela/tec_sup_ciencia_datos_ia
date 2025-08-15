# Técnicas de Procesamiento del Habla

**Carrera:** Técnico Superior en Ciencia de Datos e Inteligencia Artificial  
**Año:** Segundo Año. Materia cursada en 2024
**Materia:** Técnicas de Procesamiento del Habla  

---

## 📖 Descripción

Este repositorio contiene las prácticas desarrolladas durante el curso de **Técnicas de Procesamiento del Habla**, donde exploramos conceptos fundamentales del procesamiento de lenguaje natural (NLP) desde los fundamentos básicos hasta técnicas avanzadas de análisis y generación de texto.

La materia abarca desde conceptos básicos como tokenización y limpieza de texto, hasta modelos estadísticos para predicción y generación de texto, culminando con el uso de librerías especializadas para análisis avanzado de textos en español.

---

## 📂 Contenido del Repositorio

### [📁 Práctica 1](./practica_1/)
**Introducción a NLP: Fundamentos del Procesamiento de Texto**

Introducción a los conceptos básicos del procesamiento de lenguaje natural. Se abordan técnicas fundamentales como tokenización, manejo de stopwords y filtrado de texto. Incluye ejemplos prácticos de preprocesamiento y limpieza de datos textuales para preparar el terreno hacia análisis más complejos.

---

### [📁 Práctica 2](./practica_2/)
**Normalización Textual: Lemmatización y Stemmatización**

Aplicación de técnicas avanzadas de normalización textual utilizando un dataset de noticias categorizadas. Se implementan algoritmos de lemmatización y stemmatización para reducir las palabras a sus formas canónicas, mejorando la eficiencia del procesamiento y análisis posterior de los textos.

---

### [📁 Práctica 3](./practica_3/)
**Clasificación de Autores con Modelos de Markov**

Desarrollo de un sistema de predicción y clasificación de textos utilizando obras de Pablo Neruda y Mario Benedetti. Se implementa un modelo de Markov de primer orden que aprende patrones de escritura de cada autor, creando un diccionario de palabras y calculando probabilidades. Incluye una clase `Classifier` personalizada para predecir la autoría de textos nuevos.

---

### [📁 Práctica 4](./practica_4/)
**Generación Automática de Texto Estilo Neruda**

Construcción de un generador automático de texto inspirado en el estilo de Pablo Neruda. Utiliza modelos de Markov para crear un sistema de predicción basado en probabilidades que genera frases aleatorias manteniendo la coherencia estilística del poeta. Implementa técnicas de generación de texto mediante cadenas de Markov.

---

### [📁 Práctica 5](./practica_5/)
**Análisis Avanzado con spaCy: Procesamiento Multilingüe**

Introducción y uso avanzado de la librería spaCy para procesamiento de textos en español e inglés. Se utilizan los modelos `es_core_news_sm`, `es_core_news_lg` y `en_core_web_md` para análisis morfológico, sintáctico y semántico. Se exploran funcionalidades como reconocimiento de entidades (`.ents`), análisis de sentencias (`.sents`), detección de puntuación (`.is_punct`), stopwords (`.is_stop`) y lemmatización (`.lemma_`).

---

## 🛠️ Tecnologías y Herramientas

- **Python** - Lenguaje principal de desarrollo
- **NLTK** - Procesamiento de lenguaje natural básico
- **spaCy** - Análisis avanzado de texto multilingüe
- **Modelos de Markov** - Predicción y generación de texto
- **Pandas/NumPy** - Manipulación y análisis de datos

---

## 📋 Prerrequisitos

```bash
pip install nltk spacy pandas numpy
python -m spacy download es_core_news_sm
python -m spacy download es_core_news_lg
python -m spacy download en_core_web_md
```

---

## 🎯 Objetivos de Aprendizaje

- Comprender los fundamentos del procesamiento de lenguaje natural
- Aplicar técnicas de preprocesamiento y normalización de texto
- Implementar modelos estadísticos para predicción textual
- Desarrollar sistemas de clasificación y generación automática
- Utilizar herramientas profesionales para análisis textual multilingüe

---

## 📧 Contacto

**Materia:** Técnicas de Procesamiento del Habla  
**Nivel:** Segundo Año - Tec. Superior en Ciencia de Datos e IA