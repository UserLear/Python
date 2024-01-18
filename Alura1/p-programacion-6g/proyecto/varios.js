"01 iniciando javascript"
alert('Hola Mundo');

//DESAFIOS 
alert("¡Bienvenida y bienvenido a nuestro sitio web!");
nombre = "luna";
edad = 25;
numeroDeVentas = 50;
saldoDisponible = 1000;
alert("¡Error! Completa todos los campos");
mensajeDeError = "¡Error! Completa todos los campos";
alert(mensajeDeError);
nombre = prompt("Por favor ingresa tu nombre: ");
edad = prompt("Por favor ingresa tu edad: ")
if (edad >= 18){
    alert("¡Puedes obtener tu licencia de conducir!")
}

if (numeroUsuario == numeroSecreto) {
    //Acertamos, fue verdadera la condición
    alert(`Acertaste, el número es: ${numeroUsuario}`);
} else {
    //La condición no se cumplió
    alert('Lo siento, no acertaste el número');
}
 //calcula un descuento en relacion a millas recorridas
let porcentajeDescuento = 0;
cantidadMillas = prompt("Ingresa las millas recorridas: ")

if (cantidadMillas > 30000) {
    porcentajeDescuento = 20;
    console.log("Tu porcentaje de descuento es:" + porcentajeDescuento);
} else if (cantidadMillas > 5000) {
    porcentajeDescuento = 10;
    console.log("Tu porcentaje de descuento es:" + porcentajeDescuento);
} else {
    porcentajeDescuento = 0;
    console.log("Tu porcentaje de descuento es:" + porcentajeDescuento);
}

//DESAFIOS:CONDICIONALES Y CONCATENACION: 09
/*1. regunta al usuario qué día de la semana es. Si la respuesta es 
"Sábado" o "Domingo", muestra "¡Buen fin de semana!". De lo contrario, 
muestra "¡Buena semana!*/
nombre = prompt("Cual es tu nombre: ")

alert(`Hola ${nombre} que dia de la semana es hoy?.`)
dia = prompt("Introduce el dia: ")

if (dia == "sabado") {
    console.log("¡Buen fin de semana!")
    alert("¡Buen fin de semana!")
} else if (dia == "domingo") {
    console.log("¡Buen fin de semana!")
    alert("¡Buen fin de semana!")
} else {
    console.log("¡Buena semana!")
    alert("¡Buena semana!")
}

/*2. Verifica si un número ingresado por el usuario es positivo o 
negativo. Muestra una alerta informativa.*/ 
nombre = prompt("Cual es tu nombre: ")

numero = prompt(`Hola ${nombre} introduce un numero: `)

if (numero < 0) {
    alert("El numero que ingresastes es menor que cero.")
} else if (numero > 0) {
    alert("El numero que ingresastes es mayor que cero.")
} else {
    alert("El numero que ingresastes es cero.")
}

