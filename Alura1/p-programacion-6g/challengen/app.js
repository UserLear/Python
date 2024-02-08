//codificador y decodificador
/*Requisitos visuales
1. area de escritura de la parabra a codificar
2. boton que ejecuta la codificacion y borra el cuadro de texto
3. al codificar el resultado se envia a otra seccion dentro de la pantalla 
donde esta ya codificado.
4. boton de descodificacion que devuelve el texto cofificado en la pantalla
secundaria a la pantalla de inicio ya descodificado.
5. boton de copiar texto encriptado para pegarlo y desencriptar y borrar el cuadro de texto
*/

/*Requisitos de codigo
1. */












let numeroSecreto = 0;
let intentos = 0;

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
    asignarTextoElemento1('p', 'Indica un numero del 1 al 10');
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
    //document.querySelector("#reiniciar").setAttribute("disabled", "true");

    
}
condicionesIniciales()

function limpiarCaja() {
    //let valorCaja = document.querySelector('#valorUsuario');
    //valorCaja.value = '';
    document.querySelector('#valorUsuario').value = "";
}

function generarNumeroSecreto() {
    return Math.floor(Math.random()*10+1);
}



