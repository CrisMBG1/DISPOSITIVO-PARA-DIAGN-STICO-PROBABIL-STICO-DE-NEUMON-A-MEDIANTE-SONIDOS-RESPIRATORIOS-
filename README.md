# DISPOSITIVO PARA DIAGNÓSTICO PROBABILÍSTICO DE NEUMONÍA MEDIANTE SONIDOS RESPIRATORIOS EN UNA RED NEURONAL CONVOLUCIONAL Y CORRELACIONANDO CON ELECTROCARDIOGRAFÍA

![Modelo3DPCB](https://user-images.githubusercontent.com/88993846/132110988-ce82f52d-6e39-4506-a7a3-1a7495d972b0.png)

## Resumen
Se explica y detalla el diseño de un dispositivo para el diagnóstico probabilístico de neumonía mediante sonidos respiratorios que se evalúan en una red neuronal convolucional (CNN) y correlacionando la técnica de electrocardiografía en esta patología, se realiza la adquisición del sonido mediante un micrófono  para posteriormente realizar el muestreo de la señal, se hace de igual forma pero con una frecuencia de muestreo diferente a el sensor AD8232, para con un software realizar el filtrado y análisis. \\
El audio se evalúa en la CNN que observe patrones comunes en su espectrograma y coeficientes cepstrales en las frecuencias de Mel, comparando con un dataset de audios de personas con patologías respiratorias, determinar si hay patrones comunes en esta, el sensor de electrocardiografía  permite observar las magnitudes de las ondas e intervalos para saber si se encuentran en los valores normales y correlacionando estas, saber si esta forma de diagnóstico es fiable o no. 

## Introducción

\IEEEPARstart{L}{a} neumonía es una infección causada por virus, hongos, y bacterias, produciendo una inflamación del tejido pulmonar, en donde estos sacos se llenan de fluido, con síntomas como tos con flema o pus, fiebre, escalofríos y dificultad para respirar. Existen factores de riesgo que aumentan las probabilidades de contraer neumonía como enfermedades respiratorias crónicas, fumar cigarrillos, demencia, lesiones cerebrales, problemas del sistema inmunológico, padecer enfermedades graves entre otras, y se puede contraer al estar en ambientes hospitalarios o extrahospitalario, los grupos de riesgo se encuentran bebés y niños pequeños, personas mayores a 65 años, y personas con problemas de salud o sistemas inmunitarios debilitados, “La neumonía adquirida en la comunidad (NAC) continúa siendo una de las principales causas de mortalidad en Colombia, pues es responsable de 13 de cada 100.000 muertes“\cite{Neumonia1}.
Los tiempos y costos para el diagnóstico de neumonía pueden ser elevados y pueden tomar muchos días que son vitales para el tratamiento, en Colombia “los costos directos totales asociados con neumonía fue de Col \(\$\) 12’178.949, Col \(\$\) 7’533.187 para meningitis y Col \(\$\) 9’242.806 para bacteriemia. El costo por adulto de la atención ambulatoria de la neumonía adquirida en la comunidad se estimó en Col \(\$\)106.174. Para casos especiales se incrementó a Col \(\$\) 164.695” \cite{Neumonia2}.



## Definición del problema

La persona que se recupere de la neumonía, en el transcurso del tiempo está propenso a producir consecuencias derivadas a esta, las secuelas después de una neumonía con frecuencia no cursan solas, sino que derivan en otras enfermedades alarmantes. La persona afectada, su familia o la persona a cargo deben estar atentas a las sintomatologías de la persona tras la enfermedad detectando alguna que alerten de ellas. Entre estas se encuentran derrame pleural paraneumónico que es la acumulación de líquido en el espacio pleural, empiema donde en las enfermedades asociadas al empiema son: fístula broncopleural, absceso pulmonar, sepsis respiratoria y anemia \cite{Neumonia3}.\\
Con base a lo mencionado anteriormente en la problemática, se quiere realizar un diagnóstico rápido de neumonía mediante la clasificación de sonido respiratorios mediante una red neuronal convolucional y correlacionando otras sintomatologías mediante electrocardiografia para comprobar la viabilidad de esta forma de diagnóstico.


# Solución propuesta 

Dispositivo que realice la adquisición de sonidos respiratorios mediante un microfono y electrocardiografía \cite{Articulo1,Articulo2,Articulo3}, en donde mediante una red neuronal alimentada con un dataset de sonidos respiratorios de personas con neumonía y sin neumonía, diagnosticar si la persona posee neumonía mediante un valor probabilístico.
La idea de este artículo es mostrar el desarrollo de un dispositivo de bajo impacto ambiental, un desarrollo tecnológico relevante y social ya que aborda un problema que actualmente está presente debido a las enfermedades respiratorias como las que se están viviendo actualmente por la pandemia covid-19.


# Prototipo de la solución
El desarrollo de este dispositivo consiste en 2 etapas como se ve en la Figura \ref{fig:EtapasDia}, la etapa uno consiste en la adquisición de la señal de audio y de electrocardiografía, en donde la señal del micrófono es inicialmente amplificada para luego ser leída y convertida por un ADC (conversor análogo digital), y la señal cardiaca mediante el módulo AD8232 \cite{AD8232} se adquiere de igual forma pero un canal ADC diferente. 
Este muestreo de las señales lo realiza un microcontrolador STM32f103C8T6\cite{STM32F103x8}, en donde la frecuencia de muestreo de la señal de audio es \(F_{m}= 10KHz\) y para la señal de electrocardiografía \(F_{m}=200Hz\) recomendada para este tipo de señales. 

La etapa dos consiste en la transmisión de estas señales mediante el circuito ft232rl \cite{FT232R} para ser luego procesadas por la interfaz de usuario en donde se encuentra una red neuronal convolucional que realiza el diagnóstico de esta. 


![DaigramaBloques](https://user-images.githubusercontent.com/88993846/132111254-949ba416-f6f1-43c1-9124-23f74aaffba8.JPG)
Figura 1. Etapas del dispositivo probabilístico de neumonía.


### Caracterización de los sonidos respiratorios

Se identifica el rango de frecuencias de los sonidos respiratorios (respiración y tos) mediante un dataset \cite{Dataset} y mediante su transformada de fourier discreta (DFT) . 
Mediante una muestra de sonidos respiratorios en las que se encuentran el cual se obtuvo el espectro de frecuencias mediante el software MATLAB® Figura \ref{fig:Espectro}. el rango de frecuencias de los sonidos respiratorios las personas los cuales se encuentran 0-7.6KHz.


![Espectro](https://user-images.githubusercontent.com/88993846/132111271-b53265e2-b6d6-4d3f-9ff7-aaa462d0c977.png)
Figura 2. Espectro de frecuencias de sonidos respiratorios de una niña de 6 años (Azul) y bebe (Naranja).


### Caracterización de la señal electrocardiográfica

La señal de electrocardiografía tiene diferentes características que permiten analizar el comportamiento eléctrico, está compuesta por la línea isoeléctrica (punto de ausencia de la actividad eléctrica), Ondas (deflexiones o variación de la señal) compuesta por las ondas P, complejo QRS y onda T, segmentos que es la línea entre dos ondas como el segmento PR y ST e intervalos conjunto de una o más ondas por un segmento como el PR y QT como se observa en la Figura \ref{fig:ondas},  

![OndasCora](https://user-images.githubusercontent.com/88993846/132111293-654ea07c-17bb-4004-b547-6f4987e7aca6.png)
Figura 3. Ondas e intervalos de la señal ECG \cite{Ondas}.

La señal ECG tiene un espectro frecuencial que va desde los 0 Hz a los 100 Hz, este rango de frecuencias es el que se tendrá en cuenta para la filtración de la señal de diferentes ruidos eléctricos y mecánicos.

Para la adquisición de las señales electrocardiográficas se usó la ubicación de los electrodos de superficie según  el triángulo de Einthoven Figura \ref{fig:Triangulo} lograr medir las tres derivaciones .

![TrianguloEin](https://user-images.githubusercontent.com/88993846/132111301-586e17cc-3463-487d-87b7-4040cb7f1037.png)

Figura 4. Triangulo de Einthoven para la ubicación de los electrodos de superficie \cite{Triangulo}.

### Etapa de adquisición de señal de audio y de electrocardiografía 


El circuito de la Figura \ref{fig:Audio}, realiza la amplificación de la señal de audio para ser muestreada por el ADC del microcontrolador, el cual tiene una ganancia de 50 y lo fija en niveles de 0 a 5 V. 


![Amplificador](https://user-images.githubusercontent.com/88993846/132111307-166185f6-b302-449d-9900-89536b22dba0.png)
Figura 5. Amplificador para señal de audio.

Para monitorear la actividad eléctrica del corazón se usó el sensor de ritmo cardiaco AD8232 de la Figura \ref{fig:ModElectro}, este es un bloque de señales para ECG, extrayendo los biopotenciales, amplificando y filtrando las señales en condiciones de ruidos eléctricos o mecánicos. 
Estos potenciales se miden mediante electrodos que cuanto más cerca del corazón están los electrodos, mejor será la medición. Los cables están codificados por colores para ayudar a identificar la colocación adecuada. 



![EsquemaElectro](https://user-images.githubusercontent.com/88993846/132111310-55511648-5bcd-4119-81a5-ce1297c09354.png)
Figura 6. Módulo electrocardiografía \cite{AD8232}.


El AD8232 \cite{AD8232} está compuesto en su entrada por un filtro RIF y dos amplificadores acoplados (GM1 y GM2) Figura \ref{fig:EsquematicoAD}, el amplificador corriente continua (HPA) y un integrador formado por C1 y un amplificador óptico.\\ El amplificador de transconductancia, GM1, Estos amplificadores toman la señal de los electrodos y generan una corriente proporcional a la tensión presente en sus entradas.\\
Para posteriormente proporcionar esta señal a un amplificador de instrumentación C1 con una ganancia de 100 y enviarla por OUT para ser leída. Adicionalmente está compuesto por comparadores y filtros con el fin de que la señal sea lo más precisa posible para la lectura de las ondas e intervalos de la ECG. 

![ElectroBloques](https://user-images.githubusercontent.com/88993846/132111319-9558a408-3658-408f-8175-7894c5afbbeb.png)

Figura 7. Diagrama esquemático del AD8232.

La Figura \ref{fig:Comunicacion}, es un circuito integrado que realiza la conversión entre USB a datos seriales asíncronos, permite la transmisión de datos de audio y electrocardiografía para ser leídos y procesados. 

![Serial](https://user-images.githubusercontent.com/88993846/132111322-330bb2e3-fbd9-4b34-a9f2-7ee5393c787f.png)


Figura 8. Circuito de comunicación.

Las fuentes de alimentación son 5V  y 3.3V de la Figura \ref{fig:Reguladores}, se implementaron debido a los requerimientos de los anteriores circuitos, para esto se usarán 2 reguladores de voltaje por la baja potencia de los circuitos, en donde los datasheets\cite{L78,LD39015} proveen la aplicación típica para estos valores. 



![Regulador5](https://user-images.githubusercontent.com/88993846/132111324-53613e31-df47-4bea-96ad-d4cbfa5c0de0.png)
![Regulador3](https://user-images.githubusercontent.com/88993846/132111326-190dde85-4a7b-4724-bd0d-5096adc59dba.png)

Figura 9. Reguladores de voltaje.


El microcontrolador que se usó fue el STM32f103C8T6, para la lectura de los datos de audio y electrocardiografía, también este microcontrolador permite la ejecución de tareas de forma simultánea mediante el sistema operativo RTOS, en donde de forma simultánea se realizó la lectura mediante dos entradas ADC. 

## Etapa filtrado

En la Figura \ref{fig:SeñalFiltrada} se puede observar en la parte superior la señal de electrocardiografía con ruidos e interferencias, para esto se diseñó un filtro digital tipo pasa bajos en la frecuencia de corte de 40 Hz en -3dB y eliminado el desplazamiento con el fin de reconocer las ondas e intervalos de la señal electrocardiográfica como se ve en la parte inferior. 


![2021-05-18 (1)](https://user-images.githubusercontent.com/88993846/132111328-5d019817-26d8-4051-805c-ab07eaa0339e.png)

Figura 10. Señal ECG derivación 3 sin filtrar (Arriba) y señal ECG con filtro pasa bajos y fijada en 0mV (Abajo)

## Procesamiento de la señal respiratoria
### Selección de algoritmo de deep learning

El algoritmo desarrollado para la clasificación de sonidos más utilizada y con mayor fiabilidad actualmente se encuentra la red neuronal convolucional, que con ayuda de la transformada de fourier que transforma la señal del dominio en el tiempo al dominio frecuencial, espectrograma que es una representación visual del espectro de frecuencias de una señal en intervalos de tiempo y MFCC (Coeﬁcientes Cepstrales en las Frecuencias de Mel) esta muestra de manera gráfica los cambios en la intensidad que nos servirá para extraer características de ese sonido, todas estas herramientas se usarán para obtener la clasificación de la patología.

### Red neuronal convolucional (CNN)

La CNN será alimentada mediante un dataset de sonidos respiratorios que está dividida en sonidos de Asma, Bronquiectasia, Bronquiolitis, COPD (enfermedad pulmonar obstructiva crónica), LRTI (Infección del tracto respiratorio inferior), Neumonía y URTI (Infección del tracto respiratorio superior), este dataset entrenará la red neuronal para lograr obtener el modelo de clasificación, las capas de esta red obtendrán características de manera jerarquizada, de manera que la salida de la red entregará un diagnóstico probabilístico de concordancia para neumonía y las otras patologías.\\ 
En una red neuronal convolucional, las neuronas sencillas de un perceptrón son reemplazadas por procesadores en matriz que realizan una operación sobre los datos de imagen 2D que pasan por ellas como se ve en la Figura \ref{fig:CNN}, en lugar de un único valor numérico con se encuentra en \eqref{eq:RedNeuro}.



\begin{equation}
Y_{i}=g(b_{j}+\sum K_{ji}\oplus Y_{j})
\label{eq:RedNeuro}
\end{equation}

![CNN](https://user-images.githubusercontent.com/88993846/132111334-47d0864a-8e66-47fd-8027-403b9e95fa2b.png)

Figura 11. Arquitectura para red de sonido.


### Preprocesamiento y dataset

Antes de realizar la red neuronal se preparó el dataset \cite{Dataset} con sonidos respiratorios nombrados anteriormente,en este dataset se encuentran datos de 126 pacientes, contiene tanto sonidos respiratorios limpios como grabaciones ruidosas que simulan condiciones de la vida real, un archivo texto el cual muestra el número del paciente, la locación del pecho en donde fue grabada y el modo de adquisición (single channel o multichannel).\\
Estos sonidos se procesan en Pycharm 2020.2.3 con python 3.7.9 se segmentan cada 10 segundos para ampliar el número de audios del dataset, luego se realizó la transformación MFCC para generar un archivo .JSON que contiene los datos en una matriz con las MFCC de estos audios, este archivo alimentara la CNN.

### Desarrollo de la red neuronal

Para la elaboración de la CNN se usaron las librerías de tensorflow keras, numpy, sklearn y matplotlib; La entrada de la red neuronal es el archivo .JSON explicado anteriormente que contiene la información de todos los MFCC, la capa interna con 512, 256 y 64 unidades respectivamente con función de activación relu, para finalmente una capa de salida con 10 unidades que son los tipos de audios que se quieren clasificar Asma, Bronquiectasia, Bronquiolitis, COPD (enfermedad pulmonar obstructiva crónica), LRTI (Infección del tracto respiratorio inferior), Neumonía y URTI (Infección del tracto respiratorio superior). 
En este artículo se implementó el modelo CNN con la arquitectura Figura \ref{fig:ArquitecturaCNN}. con los parámetros de la Tabla \ref{tab:Constantes}.


\begin{table}[H]
\centering
\caption{Parámetros para el modelo CNN - clasificación de los sonidos respiratorios.}
\label{tab:Constantes}
\scalebox{1.1}{
\begin{tabular}{c c}
\hline\hline
\textbf{Parámetros} & \textbf{Valor} 
\\ \hline
Batch size  & 32\\
Droput Rate & 0.3\\
Learning rate & 0.001\\
Epochs & 100 \\
\hline
\hline
\end{tabular}}
\end{table}

![BloquesRed](https://user-images.githubusercontent.com/88993846/132111338-e3817214-038c-4c1d-a159-1c368976db0d.png)

Figura 12. Arquitectura de la CNN.

## Resultados
### Interfaz gráfica de usuario

Se desarrolló una interfaz simple mediante el software python usando la librería Tkinter, con el propósito de grabar el sonido y la electrocardiografía en tiempo real Figura \ref{fig:Interfaz}.  


![InterfazUsuario](https://user-images.githubusercontent.com/88993846/132111340-28a52556-40af-4ba9-a0e8-3f4eada6170a.JPG)

Figura 13. Interfaz de usuario (Elaborado en Pycharm con Python 3.7.9).


Inicialmente se desarrolló la PCB de la Figura \ref{fig:Modelo3D} en Altium Designer® y su tamaño fue adecuado a un modelo 3D elaborado en SolidWorks®, pero debido a su tamaño y su elevados costos de fabricación se elaboró la PCB de la Figura \ref{fig:PCB}.

![Modelo3DPCB](https://user-images.githubusercontent.com/88993846/132111343-7fb4daf9-3dc4-44f4-b787-2ca6c446db47.png)

Figura 14. Prototipo 3D en Altium Designer®.

![PCBFisica](https://user-images.githubusercontent.com/88993846/132111347-c93902d4-becf-4609-b4db-b2b3af7847bd.jpg)


Figura 15. PCB del proyecto.



Esta permite hacer la amplificación muestreo de la señal de audio, muestreo de la señal de electrocardiografía y transmisión dados los circuitos esquemáticos.

Se logró que la CNN tuviera una precisión del 85.48 \(\%\) Figura \ref{fig:RespuestaCCN}, con los los audios de prueba en donde está aumentó debido a que se usó las técnicas de dropout y regularizers para minimizar el overfitting con los parámetros Tabla \ref{tab:Constantes}, esta red neuronal es solo diagnóstico probabilístico y no debe ser tomado como un diagnóstico final para esta enfermedad. 

![ResultadoCCN](https://user-images.githubusercontent.com/88993846/132111350-50fd45c4-9d87-4bac-855f-659362f12d1c.png)

Figura 16. Respuesta de la red neuronal a entrenamiento precisión del modelo (Arriba) y error del modelo (Abajo).

La interfaz gráfica logró una comunicación a tiempo real con la señal de audio y electrocardiografía con la red neuronal desarrollada. 
Se logró la identificación de las ondas RQT para para determinar variaciones en los rangos normales en personas con neumonía. 

## Conclusiones

Dados los resultados se logró obtener un diagnóstico probabilístico de varias patologías respiratorias y no únicamente neumonía en donde estas son asma, bronquiectasia, bronquiolitis, COPD (enfermedad pulmonar obstructiva crónica), LRTI (Infección del tracto respiratorio inferior), Neumonía y URTI (Infección del tracto respiratorio superior) con la precisión dada en los resultados.\\
El sensor de electrocardiografía implementado se logró correlacionar con la sintomatología de esta patología, debido a la relación que tiene las ondas e intervalos de las señales electrocardiográficas cuando estas no están sobre los valores normales, así aumentando la probabilidad del diagnóstico, este desarrollo podría ser utilizado como complemento para un diagnóstico clínico de enfermedades respiratorias.

