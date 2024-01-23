//CONEXION CON HTML

/*definimos la funcion para introducirla al html y actue sobre el boton
intentar*/
function verificarIntento() {
    let numeroDeUsuario = document.getElementById("valorUsuario").value;
    console.log(numeroDeUsuario)
}
//modificar varios elementos en html utilizando una funcion
function asignarTextoElemento1(elemento,texto) {
    let elementoHTML = document.querySelector(elemento);
    elementoHTML.innerHTML = texto;
    return;
}
asignarTextoElemento1("h1", "Juego del numero secreto")
asignarTextoElemento1('p', 'Indica un numero del 1 al 10')

//crear una funcion para generar un numero pseudo aleatorio
let eligeSecreto = prompt("Elige el numero maximo ")
function generarNumeroSecreto(numero) {
    return numeroSecreto = Math.floor(Math.random()*parseInt(numero)+1);   
}

let numeroSecreto;
numeroSecreto = generarNumeroSecreto(eligeSecreto);
console.log(numeroSecreto)
//variables
let numeroUsuario;
let intentos = 1;
let maximosIntentos = 4;

while (numeroUsuario != numeroSecreto){
    numeroUsuario = parseInt(prompt(`Me indicas un numero entre 1 y ${eligeSecreto} por favor: `));
    console.log(typeof(numeroUsuario));

    /*Este codigo 
    realiza una comparacion*/
    if(numeroUsuario == numeroSecreto){
        //devuelve el mensaje alert si a condicion se cumple
        console.log("Acertaste el numero")
        alert(`Acertaste, el numero es: ${numeroSecreto}. Lo hiciste en ${intentos} ${intentos == 1 ? "vez" : "veces"}.`)
    } else {
        if (numeroUsuario > numeroSecreto) {
            alert("El numero secreto es menor.")
        } else {
            alert("El numero secreto es mayor")
        }
        //intentos = intentos + 1;
        //intentos += 1;
        intentos++;
        //palabraVeces = "veces";

    //codigo que rompe el bucle al generarse una condicion
    if (intentos > maximosIntentos ) {
        alert(`Llegaste al numero al numero maximo de ${maximosIntentos} intentos.`)
        break;
    }
    }
}