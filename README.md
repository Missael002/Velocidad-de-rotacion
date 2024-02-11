# Velocidad-de-rotacion
El código calcula la velocidad de rotación de la Tierra en función de la latitud introducida por el usuario.

Para calcular la velocidad de rotación de la Tierra en un punto específico, se utiliza la fórmula que relaciona 
la velocidad angular de rotación de la Tierra (ω) con la latitud del punto y el radio de la Tierra.

V= ω × R × cos(latitud)

-V = es la velocidad de rotación en metros por segundo (m/s),
-ω = es la velocidad angular de rotación de la Tierra en radianes por segundo,
-R = es el radio promedio de la Tierra en metros,
-latitud = latitud es la latitud del punto en radianes

 En este caso simplificamos la formula de la siguiente manera:
 ω = es aproximadamente 7.2921159×10^−5 que simplificado seria 0.0000729 radianes por segundo.
 R = equivale a "6371000" que es el radio promedio de la Tierra en metros.

La formula simplificada quedaria de la siguiente manera:
V= 0.0000729 x 6371000 x cos(latitud)
  
porteriormente multiplicamos V x 3.6 lo que nos daria el resultado en Km/h

3.6 = hay 3600 segundos en una hora y 1000 metros en un kilómetro "3600/1000"
