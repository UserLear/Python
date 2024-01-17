alert('Hola Mundo');
let numeroSecreto = 6;
let numeroUsuario = prompt("Me indicas un numero por favor: ");
console.log(numeroUsuario);

if(numeroUsuario == numeroSecreto){
    alert("Acertaste el numero")
}

if (numeroUsuario == numeroSecreto) {
    //Acertamos, fue verdadera la condición
    alert(`Acertaste, el número es: ${numeroUsuario}`);
} else {
    //La condición no se cumplió
    alert('Lo siento, no acertaste el número');
}

"desafios"
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
