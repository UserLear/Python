


function asignarTextoElemento1(elemento,texto) {
    let elementoHTML = document.querySelector(elemento);
    elementoHTML.innerHTML = texto;
    return;
}

function verificarIntento() {
    let numeroDeUsuario = parseInt(document.getElementById('valorUsuario').value);
    if (numeroDeUsuario === numeroSecreto) {
        asignarTextoElemento1("p", "Acertaste el numero")
    } else {
        if(numeroDeUsuario > numeroSecreto) {
            asignarTextoElemento1("p","El numero secreto es menor.")
        } else {
            asignarTextoElemento1("p","El numero secreto es mayor.")
        }
    }
    return
}

function generarNumeroSecreto() {
    return Math.floor(Math.random()*10+1);
}

asignarTextoElemento1("h1", "Juego del numero secreto")
asignarTextoElemento1('p', 'Indica un numero del 1 al 10')

let numeroSecreto = generarNumeroSecreto();