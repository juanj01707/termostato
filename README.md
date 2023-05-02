# **Termostato**
este código permite al usuario ingresar casos de prueba con límites y valores, y calcula el número mínimo de operaciones necesarias para transformar la temperatura a en la temperatura b, utilizando a x x. luego de que se ingresan todos los casos de prueba imprime los resultados de todas

## **-Estos son los pasos que sigue el algoritmo**

1. Se le pide al usuario que ingrese el número de casos de prueba.
2. Se valida que el número de casos de prueba esté dentro de un rango válido.
3. Se solicita al usuario ingresar los datos para cada caso de prueba (valores de l, r, x, a y b).
4. Para cada caso de prueba:
    - a. Se verifica si el valor de b está dentro del rango (l, r). Si no lo está, se agrega -1 a la lista de resultados.
    - b. Si b está dentro del rango, se calcula la cantidad mínima de operaciones necesarias para transformar el valor a en b. Esto se hace verificando si la diferencia entre a y l es divisible exactamente por x. Si es así,          se divide la diferencia entre a y b por x para obtener el número de operaciones necesarias.
    - c. Si la diferencia entre a y l no es divisible exactamente por x, se agrega -1 a la lista de resultados.
5. Se muestran los resultados obtenidos para cada caso de prueba.

## **--Tiempo de codificacion**
el tiempo que inverti en relizar el codigo fue de  horas de las cuales:

3 horas fueron de ententer el problema
5 horas para conseguir que el codigo funcionara
1 hora para la documentacion
