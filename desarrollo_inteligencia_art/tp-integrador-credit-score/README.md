# Desarrollo de Sistemas Inteligentes - Trabajo Práctico Grupo 8
## Descripción General

Este repositorio contiene el trabajo práctico desarrollado por el Grupo 8 para la materia "Desarrollo de Sistemas Inteligentes". El proyecto se enfoca en el análisis de un conjunto de datos de perfiles crediticios para préstamos de vehículos de dos ruedas en India, con el objetivo de identificar grupos de personas propensas a riesgos crediticios y predecir sus puntajes.

### Conjunto de Datos
El dataset fue obtenido de Kaggle y contiene registros de perfiles de solicitudes de préstamos en India. Incluye características como:
- Datos demográficos (edad, género)
- Datos financieros (ingresos, puntajes de crédito)
- Historial crediticio
- Detalles de préstamos solicitados
- Información de empleo
- Ubicación geográfica

## Hipótesis Planteadas

- Hipótesis 1: Las personas con antigüedad crediticia tienen trabajos más estables, lo que se refleja en una tasa de 'LTV ratio' con menor riesgo.
- Hipótesis 2: Investigación sobre qué rango etario tiene mejor puntuación de perfil, y si esto depende de sus ingresos o del número de préstamos activos.

## Metodología
El proyecto sigue estos pasos metodológicos:

- Análisis Exploratorio de Datos (EDA)
- Análisis univariado con histogramas y diagramas de cajas
- Identificación y tratamiento de valores atípicos
- Análisis bivariado con gráficos de dispersión


## Preprocesamiento de Datos

- Eliminación de duplicados
- Categorización de variables numéricas
- Codificación de variables categóricas
- Normalización de datos


## Modelado

Regresión Lineal
Árboles de decisión (DecisionTreeClassifier y DecisionTreeRegressor)
Random Forest



## Resultados Principales

Las personas asalariadas tienden a tener mejores puntajes crediticios y de perfil.
Las personas con trabajos autónomos muestran mayor antigüedad en su historial crediticio.
Se encontró una correlación positiva entre ingresos y puntuación crediticia.
El modelo Random Forest mostró el mejor desempeño para la predicción, con un MSE de 0.174.

## Conclusiones

El perfil de empleo es un factor significativo que puede predecirse y que impacta en la calificación crediticia.
Las personas asalariadas tienen mayor proporción de historial crediticio, aunque esto no necesariamente se refleja en un menor riesgo LTV.
Un mayor ingreso correlaciona con una mejor puntuación crediticia, y los perfiles con mejor puntuación tienden a tener más préstamos activos.

## Herramientas Utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Yellowbrick

Grupo 8
Este trabajo fue desarrollado por el Grupo 8 como parte de la evaluación para la materia Desarrollo de Sistemas Inteligentes.