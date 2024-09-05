# Proyecto Final ML  
## Defunciones Euskadi ML  

### Link de la base de datos  
[Base de datos](https://www.eustat.eus/bankupx/pxweb/es/DB/-/PX_010303_cmnp_edef18.px/table/tableViewLayout2/)  

### Conjunto de datos  
La base de datos tiene múltiples dimensiones (mes, año, tramo de edad, sexo, grandes grupos CIE-10), lo que permite realizar un análisis detallado y segmentado de las defunciones. Los datos están organizados por período temporal, específicamente por mes y año, lo que permite realizar un análisis de series temporales o análisis estacionales para identificar patrones de mortalidad a lo largo del tiempo.  
Debido a la estructura temporal de los datos (meses y años), se puede realizar un análisis de series temporales para observar tendencias, picos estacionales, o cambios drásticos en mortalidad en ciertos períodos (como durante la pandemia de COVID-19).  

### Variables principales  

#### 1. Mes  
- **Descripción**: Representa el mes en el que ocurrió la defunción.  
- **Tipo de dato**: Originalmente en formato de texto (ej: "Enero"), pero se ha transformado a formato numérico (ej: 1 para Enero, 2 para Febrero, etc.).  
- **Rango de valores**: 1 a 12.  

#### 2. Año  
- **Descripción**: El año en el que ocurrió la defunción.  
- **Tipo de dato**: Numérico.  
- **Rango de valores**: Originalmente el formato está por cada año del 2010 - 2023, pero se ha transformado a rangos por cada 5 años (ej: rango1, para los años del 2010 al 2014, rango2, para los años del 2015 al 2019, etc.).  

#### 3. Tramo de Edad Cumplida  
- **Descripción**: Representa el rango de edad de las personas fallecidas.  
- **Tipo de dato**: Originalmente está en rango numérico.  
- **Rango de valores**:  
  - 0 años  
  - 1-9 años  
  - 10-19 años  
  - 20-29 años  
  - Y así sucesivamente en intervalos de 10 años hasta llegar a los >= 90 años.  

#### 4. Sexo  
- **Descripción**: Sexo biológico de la persona fallecida.  
- **Tipo de dato**: Categórico, representado como:  
  - 0: Hombre  
  - 1: Mujer  

#### 5. Grandes Grupos CIE-10  
- **Descripción**: Código de la Clasificación Internacional de Enfermedades (CIE-10) que clasifica la causa de defunción en diferentes grupos. Las enfermedades se agrupan según un sistema estándar internacional.  
- **Tipo de dato**: Categórico.  
- **Categorías**:  
  1. I. Ciertas enfermedades infecciosas y parasitarias (A00 - B99)  
  2. II. Tumores [neoplasias] (C00 - D48)  
  3. III. Enferm. sangre y órganos hematop., ciertos trast. inmunidad (D50-D89)  
  4. IV. Enfermedades endocrinas, nutricionales y metabólicas (E00 - E90)  
  5. V. Trastornos mentales y del comportamiento (F00 - F99)  
  6. VI. Enfermedades del sistema nervioso (G00 - G99)  
  7. VII. Enfermedades del ojo y sus anexos (H00 - H59)  
  8. VIII. Enfermedades del oído y de la apófisis mastoides (H60 - H95)  
  9. IX. Enfermedades del sistema circulatorio (I00 - I99)  
  10. X. Enfermedades del sistema respiratorio (J00 - J99)  
  11. XI. Enfermedades del sistema digestivo (K00 - K93)  
  12. XII. Enfermedades de la piel y del tejido subcutáneo (L00 - L99)  
  13. XIII. Enfermedades sistema osteomuscular y tejido conjuntivo (M00 - M99)  
  14. XIV. Enfermedades del sistema genitourinario (N00 - N99)  
  15. XV. Embarazo, parto y puerperio (O00 - O99)  
  16. XVI. Ciertas afecciones originadas en el período perinatal (P00 - P96)  
  17. XVII. Malformaciones congén., deformidades y anomalías cromos. (Q00 - Q99)  
  18. XVIII. Síntomas, signos y hallazgos anormales clínicos y labor. (R00 - R99)  
  19. XX. Causas externas de mortalidad (V01 - Y89)  
  20. Covid-19 Confirmado  
  21. Covid-19 Probable  

#### 6. Número de Defunciones  
- **Descripción**: El número de defunciones que ocurrieron en un determinado mes, año, grupo de edad, sexo y causa (según la CIE-10).  
- **Tipo de dato**: Numérico (entero).