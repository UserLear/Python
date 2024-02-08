let numeroSecreto = 0;
let intentos = 0;
let listaNumerosSorteados = [];
let numeroMaximo = 10;
let maximoIntentos = 4;

function asignarTextoElemento1(elemento,texto) {
    let elementoHTML = document.querySelector(elemento);
    elementoHTML.innerHTML = texto;
    return;
}

function verificarIntento() {
    let numeroDeUsuario = parseInt(document.getElementById('valorUsuario').value);
    if (numeroDeUsuario === numeroSecreto) {
        asignarTextoElemento1("p", `Acertaste el numero en ${intentos} ${intentos === 1 ? 'vez' : 'veces'}`)
        document.getElementById('reiniciar').removeAttribute('disabled');
    }else if (intentos > maximoIntentos) {
        asignarTextoElemento1('p', `Llegaste al maximo de ${intentos} intentos`);
        document.getElementById('reiniciar').removeAttribute('disabled');
    } else {
        if(numeroDeUsuario > numeroSecreto) {
            asignarTextoElemento1("p",'El numero secreto es menor.')
        } else {
            asignarTextoElemento1("p","El numero secreto es mayor.")
        }
        intentos++;
        limpiarCaja();
    }
    
    return;
}

function condicionesIniciales() {
    asignarTextoElemento1("h1", "Juego del numero secreto");
    asignarTextoElemento1('p', `Indica un numero del 1 al ${numeroMaximo}`);
    numeroSecreto = generarNumeroSecreto();
    intentos = 1;
}

function reiniciarJuego() {
    //limpiar caja
    limpiarCaja()
    //indicar mensaje de intervalo de numeros
    //generar numero aleatorio
    //inicializar numero de intentos
    condicionesIniciales();
    //deshabilitar el boton de nuevo juego
    document.querySelector("#reiniciar").setAttribute("disabled", "true");    
}
condicionesIniciales()

function limpiarCaja() {
    //let valorCaja = document.querySelector('#valorUsuario');
    //valorCaja.value = '';
    document.querySelector('#valorUsuario').value = "";
}

function generarNumeroSecreto() {
    let numeroGenerado = Math.floor(Math.random()*numeroMaximo+1);
    console.log(numeroGenerado);
    console.log(listaNumerosSorteados);
    //si ya sortemos todos los numeros
    if (listaNumerosSorteados.length == numeroMaximo) {
        asignarTextoElemento1("p", "Ya se sortearon todos los numeros posibles");
    }else {
        //si el numero generado esta en la lista hace algo si no hace otra cosa
        if (listaNumerosSorteados.includes(numeroGenerado)) {
            return generarNumeroSecreto();
        }else {
            listaNumerosSorteados.push(numeroGenerado);
            return numeroGenerado;  
        }
}
}



