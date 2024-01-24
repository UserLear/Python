//DESAFIOS: INTERACTUANDO CON HTML: 08
/*1. Descarga otro proyecto haciendo clic en este enlace y ábrelo en 
Visual Studio Code.*/
/*2. Cambia el contenido de la etiqueta h1 con document.querySelector
y asigna el siguiente texto: "Hora del Desafío". */
let cambioEtiqueta = document.querySelector("h1");
cambioEtiqueta.innerHTML = "Hora del desafio"

/*3. Crea una función que muestre en la consola el mensaje "El botón 
fue clicado" siempre que se presione el botón "Console".*/
//<button onclic1k="clicker();" class="container__boton">Consola</button>
function clicker() {
    alert("El boton fue clicado")
    console.log("El boton fue presionado")
}

/*4. Crea una función que se ejecute cuando se haga clic en el botón 
"prompt", preguntando el nombre de una ciudad de Brasil. Luego, muestra
una alerta con el mensaje concatenando la respuesta con el texto: 
"Estuve en {ciudad} y me acordé de ti". */
//<bu1tton onclick="ciudad();" class="container__boton">Prompt</bu1tton>
function ciudad() {
    let ciudadBrazil = prompt("Mensiona una ciudad de Brazil: ");
    alert(`Estube en ${ciudadBrazil} y me acorde de ti.`)
}

/*5. Crea una función que muestre una alerta con el mensaje: "Yo amo 
JS" siempre que se presione el botón "Alerta". */
//<button onclick="amoJS();" class="container__boton">Alerta</button>
function amoJS() {
    alert("Yo amo JS")
}

/*6. Al hacer clic en el botón "suma", pide 2 números y muestra el 
resultado de la suma en una alerta. */
//<button onclick="suma();" class="container__boton">Suma</button>
function suma() {
    numero1 = parseInt(prompt("Introduce primer numero: "));
    numero2 = parseInt(prompt("Introduce segundo numero: "));
    alert(`El resultado de la suma es ${numero1+numero2}`)
}

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

//DESAFIO: FUNCIONES: 09
/*1. Crear una función que muestre "¡Hola, mundo!" en la consola.*/
function saludo() {
    console.log("Hola Mundo!")
}

/*2. Crear una función que reciba un nombre como parámetro y 
muestre "¡Hola, [nombre]!" en la consola. */
function saludo(nombre) {
    console.log("Hola "+ nombre)
}

/*3. Crear una función que reciba un número como parámetro y 
devuelva el doble de ese número. */
function doble(numero) {
    let doble = numero * 2;
    return doble
}

/*4. Crear una función que reciba tres números como 
parámetros y devuelva su promedio. */
function promedio(n1, n2, n3) {
    let promedio = (n1+n2+n3)/3;
    return promedio
}

/*5. Crear una función que reciba dos números como 
parámetros y devuelva el mayor de ellos */
function numeroMayor(n1,n2) {
    if (n1 > n2) {
        return(n1)
    } else {
        return(n2)
    }
}

/*6. Crear una función que reciba un número como parámetro
y devuelva el resultado de multiplicar ese número por sí mismo */
function numero(n1) {
    let numero = n1 * n1
    return numero
}

