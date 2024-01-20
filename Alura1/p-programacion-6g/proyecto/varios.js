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

/*3. Crea un sistema de puntuación para un juego. Si la puntuación es 
mayor o igual a 100, muestra "¡Felicidades, has ganado!". En caso 
contrario, muestra "Intenta nuevamente para ganar.". */
nombre = prompt("Cual es tu nombre: ")

numero = prompt(`Hola ${nombre} introduce un numero: `)

if (numero >= 100) {
    alert("Felicidades has ganado.")
} else {
    alert("Intenta nuevamente para ganar")
}

/*4. Crea un mensaje que informe al usuario sobre el saldo de su 
cuenta, utilizando un template string para incluir el valor del 
saldo */
nombre = prompt("Cual es tu nombre: ")
alert(`Hola ${nombre} este programa te informa que saldo tienes en cuenta`)

let salario = 12000;

alert(`${nombre} al parecer tienes ${salario} disponible para gastar.`)

/*5. Pide al usuario que ingrese su nombre mediante un prompt. 
Luego, muestra una alerta de bienvenida usando ese nombre.*/
alert("Hola usuario ingresa por favor tu nombre");
nombre = prompt("Dinos tu nombre: ");
alert(`Valla te estabamos esperando ${nombre}.`);

//DESAFIOS: LOOPS Y TENTATIVAS: 07
/*1. Crea un contador que comience en 1 y vaya hasta 10 usando un 
bucle 'while'. Muestra cada número. */
nombre = prompt("Cual es tu nombre: ");
alert(`Hola ${nombre} este programa es un contador de numeros`)

numero = 0;
while (numero <=10) {
    alert("Ahora el numero vale: " + numero)
    numero ++
}

/*2. Crea un contador que comience en 10 y vaya hasta 0 usando un 
bucle 'while'. Muestra cada número. */
nombre = prompt("Cual es tu nombre: ");
alert(`Hola ${nombre} este programa es un contador de numeros`)

numero = 10;
while (numero > 0) {
    alert("Ahora el numero vale: " + numero)
    numero --
}

/*3. Crea un programa de cuenta regresiva. Pide un número y cuenta 
desde 0 hasta ese número utilizando un bucle 'while' en la consola 
del navegador. */
nombre = prompt("Cual es tu nombre: ");
alert(`Hola ${nombre} este programa es un contador de numeros`)

ingresaNumero = prompt("Ingresa un numero: ");
numeroInicio = 0;

while (numeroInicio < ingresaNumero) {
    console.log(`Empieza en: ${numeroInicio}`);
    numeroInicio++;
}
console.log(`¡Y es asi como comienza este espectaculo, Bienvenidos! al ${numeroInicio} `);

/*4. Crea un programa de cuenta progresiva. Pide un número y cuenta 
desde ese numero hasta 0 número utilizando un bucle 'while' en la consola 
del navegador. */
nombre = prompt("Cual es tu nombre: ");
alert(`Hola ${nombre} este programa es un contador de numeros`);

ingresaNumero = prompt("Ingresa un numero: ");

while (ingresaNumero > 0) {
    console.log(`Empieza en: ${ingresaNumero}`);
    ingresaNumero--;
}
console.log(`¡Y es asi como comienza este espectaculo, Bienvenidos!.`);

//DESAFIOS: BUENAS PRACTICAS DE PROGRAMACION: 09
/*1. Crea un programa que utilice console.log para mostrar un 
mensaje de bienvenida.*/
console.log("Un gusto saludarte");

/*2. Crea una variable llamada "nombre" y asígnale tu nombre. Luego, 
utiliza console.log para mostrar el mensaje "¡Hola, [tu nombre]!" en 
la consola del navegador.  */
nombre = "Moises";
console.log(`Un gusto saludarte ${nombre}`);

/*3. Crea una variable llamada "nombre" y asígnale tu nombre. Luego, 
utiliza alert para mostrar el mensaje "¡Hola, [tu nombre]!".*/
nombre = "Moises";
console.log(`Un gusto saludarte ${nombre}`);
alert(`Hola ${nombre}`)

/*4. Utiliza prompt y haz la siguiente pregunta: ¿Cuál es el lenguaje 
de programación que más te gusta?. Luego, almacena la respuesta en una
 variable y muestra la respuesta en la consola del navegador.*/
lenguaje = prompt("Cual es tu lenguaje de programacion favorito: ")
console.log(lenguaje)

/*5. Crea una variable llamada "valor1" y otra llamada "valor2", 
asignándoles valores numéricos de tu elección. Luego, realiza la suma 
de estos dos valores y almacena el resultado en una tercera variable 
llamada "resultado". Utiliza console.log para mostrar el mensaje "La 
suma de [valor1] y [valor2] es igual a [resultado]." en la consola.*/
valor1 = 4;
valor2 = 7;
resultado = valor1 + valor2;
console.log(`La suma de ${valor1} y ${valor2} es igual a ${resultado}`);

/*6. Crea una variable llamada "valor1" y otra llamada "valor2", 
asignándoles valores numéricos de tu elección. Luego, realiza la resta
de estos dos valores y almacena el resultado en una tercera variable 
llamada "resultado". Utiliza console.log para mostrar el mensaje "La 
diferencia entre [valor1] y [valor2] es igual a [resultado]." en la 
consola.*/
valor1 = 4;
valor2 = 7;
resultado = valor1 - valor2;
console.log(`La diferencia de ${valor1} y ${valor2} es igual a ${resultado}`);

/*7. Pide al usuario que ingrese su edad con prompt. Con base en la 
edad ingresada, utiliza un if para verificar si la persona es mayor o 
menor de edad y muestra un mensaje apropiado en la consola.*/
edad = prompt("Ingresa tu edad: ");
if (edad >= 18) {
    console.log("¡Ingreso permitido!");
} else {
    console.log("!Ingreso denegado¡");
}

/*8. Crea una variable "numero" y solicita un valor con prompt. Luego, 
verifica si es positivo, negativo o cero utilizando un if-else y muestra el 
mensaje correspondiente. */
numero = prompt("Ingresa cualquier numero real: ");
if (numero == 0) {
    console.log("El numero que ingresaste fue el 0")
} else if (numero >0) {
    console.log("El numero que ingresaste es mayor que 0")
} else {
    console.log("el numero que ingresaste es menor que 0")
}

/*9. Utiliza un bucle while para mostrar los números del 1 al 10 en la consola.*/
numero = 1;
while (numero < 11) {
    console.log("El numero es "+ numero);
    numero++;
}

/*10. Crea una variable "nota" y asígnale un valor numérico. Utiliza 
un if-else para determinar si la nota es mayor o igual a 7 y muestra 
"Aprobado" o "Reprobado" en la consola. */
nota = 7;
if (numero >= 7) {
    console.log("Aprobado")
} else {
    console.log("Reprobado")
}

/*11. Utiliza Math.random para generar cualquier número aleatorio y
muestra ese número en la consola. */
numeroAleatorio = Math.random();
console.log(numeroAleatorio);

/*12. Utiliza Math.random para generar un número entero entre 1 y 
10 y muestra ese número en la consola.*/
numeroAleatorio = Math.floor(Math.random()*10+1);
console.log(numeroAleatorio);

/*13. Utiliza Math.random para generar un número entero entre 1 y
1000 y muestra ese número en la consola. */
numeroAleatorio = Math.floor(Math.random()*1000+1);
console.log(numeroAleatorio);






