/*3. Crea un sistema de puntuación para un juego. Si la puntuación es 
mayor o igual a 100, muestra "¡Felicidades, has ganado!". En caso 
contrario, muestra "Intenta nuevamente para ganar.". */

nombre = prompt("Cual es tu nombre: ")

numero = prompt(`Hola ${nombre} introduce un numero: `)

if (numero >= 100) {
    alert("Felicidades has ganado.")
} else {
    alert("El numero que ingresastes es cero.")
}

