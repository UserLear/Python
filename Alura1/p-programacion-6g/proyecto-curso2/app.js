//CONEXION CON HTML

/*definimos la funcion para introducirla al html y actue sobre el boton
intentar*/
function intentoDeUsuario() {
    alert('click desde el boton')
}
function asignarTextoElemento1(elemento,texto) {
    let elementoHTML = document.querySelector(elemento);
    elementoHTML.innerHTML = texto;
}
asignarTextoElemento1("h1", "Juego del numero secreto")
asignarTextoElemento1('p', 'Indica un numero del 1 al 10')

//variables
let eligeSecreto = prompt("Elige el numero maximo ")
let numeroSecreto = Math.floor(Math.random()*parseInt(eligeSecreto)+1);
let numeroUsuario;
let intentos = 1;
//let palabraVeces = "vez";
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