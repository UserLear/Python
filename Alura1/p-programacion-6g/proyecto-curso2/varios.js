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

//ejercicio a mejorar
function calcularDobleTriple(numero) {
    const doble = numero * 2;
    const triple = numero * 3;
  
    return `El doble de ${numero} es ${doble} y el triple es ${triple}.`;
  }
  
  const numero = 5;
  convertir = parseInt(numero)
  const resultado = calcularDobleTriple(convertir);
  console.log(resultado);

//forma 1
function calcularDobleTriple1(numero) {
    return numero * 2 + " es el doble y " + numero * 3 + " es el triple."
}

const numero1 = 5;
convertir = parseInt(numero1)
const resultado1 = calcularDobleTriple1(convertir);
console.log(resultado1);

//forma 2 opcion correcta
function calcularDoble(numero) {
    return numero * 2; 
}
function calcularTriple(numero) {
    return numero * 3; 
}

const numero2 = 5;
convertir = parseInt(numero2)
const doble = calcularDoble(convertir);
const triple = calcularTriple(convertir);
console.log(`El doble de ${numero2} es ${doble} y el triple es ${triple}`);

//forma 3
function calcularDobleTriple(numero) {
    const resultado = {};
    resultado.doble = numero * 2;
    resultado.triple = numero * 3;
    return resultado;
  }
  
  const numero3 = 5;
  const resultado2 = calcularDobleTriple(numero3);
  
  console.log(`El doble de ${numero} es ${resultado2.doble} y el triple es ${resultado2.triple}.`);

//DESAFIO: REINICIANDO JUEGO: 09
/*1. Crea una función que calcule el índice de masa 
corporal (IMC) de una persona a partir de su altura en 
metros y peso en kilogramos, que se recibirán como 
parámetros.*/
function indiceMasaCorporal (peso, altura) {
    let iMc = peso / (altura**2);

    return iMc;
}
console.log(indiceMasaCorporal(180, 1.78));

/*2.  Crea una función que calcule el valor del factorial 
de un número pasado como parámetro.*/
function factorial(numero) {
    let valor = parseInt(numero);
    let factorial = 1;
    while (true) {
        if (valor > 0) {
            factorial *= valor;
            valor--;
        } else {
            break;
        }
    }
    return factorial;
}
let valor1 = factorial(6);
console.log(valor1);

/*3. Crea una función que convierta un valor en dólares, pasado 
como parámetro, y devuelva el valor equivalente en reales(moneda
brasileña,si deseas puedes hacerlo con el valor del dólar en 
tu país). Para esto, considera la cotización del dólar igual a 
R$4,80 */
function conversion(divisa,lempiras) {
    let conversion = lempiras / divisa;
    return conversion;
}
function tipoCambio(divisa,lempiras) {
    if (divisa == "$") {
        let dolar = 24.84;
        return conversion(dolar,lempiras);
    } else if (divisa == "€") {
        let euro = 26.85;
        return conversion(euro,lempiras);
    } else if (divisa == "¥") {
        let yen = 0.17;
        return conversion(yen,lempiras);
    } else {
        return "moneda no especificada";
    }
}

let lempiras = 50000;
console.log(`El cambio de ${lempiras} lempiras a dolares es ${tipoCambio("$",lempiras)}`);
console.log(`El cambio de ${lempiras} lempiras a euros es ${tipoCambio("€",lempiras)}`);
console.log(`El cambio de ${lempiras} lempiras a dolares es ${tipoCambio("¥",lempiras)}`);
console.log(`El cambio de ${lempiras} lempiras a otra es ${tipoCambio("%",lempiras)}`);

/*4. Crea una función que muestre en pantalla el área y el perímetro 
de una sala rectangular, utilizando la altura y la anchura que se 
proporcionarán como parámetros. */
function areaPerimetro(altura,anchura) {
    let area = altura * anchura;
    let perimetro = (2*altura) + (2*anchura);
    return [area,perimetro];
}

let [a, b] = areaPerimetro(3,7);
console.log(`El area del rectangulo es ${a} y su perimetro es ${b}`);

/*5. Crea una función que muestre en pantalla el área y el perímetro 
de una sala circular, utilizando su radio que se proporcionará como 
parámetro. Considera Pi = 3,14. */
function areaPerimetro(radio) {
    let area = 3.14*(radio**2);
    let perimetro = 3.14*(2*radio);
    return [area,perimetro];
}

let radio = 5;
let [c,d] = areaPerimetro(radio);
console.log(`El area de un circulo con radio ${radio} es ${c} y su perimetro es ${d}.`)

/*6. Crea una función que muestre en pantalla la tabla de multiplicar
 de un número dado como parámetro. */
function tablaMultiplicar(numero,secuencia) {
    let tabla = `${numero} x ${secuencia} = ${numero*secuencia}`;
    return tabla;
}
let numero = 1;
while (numero < 11) {
    console.log(tablaMultiplicar(3,numero))
    numero++;
}
/*DESAFIOS: LISTAS: 09*/
/*1. Crea una lista vacía llamada "listaGenerica".*/
let listaGenerica = [];

/*2. Crea una lista de lenguajes de programación llamada 
"lenguagesDeProgramacion con los siguientes elementos: 
'JavaScript', 'C', 'C++', 'Kotlin' y 'Python'. */
let lenguajesDeProgramacion = ['JavaScript', 'C', 'C++', 'Kotlin', 'Python'];

/*3. Agrega a la lista "lenguagesDeProgramacion los siguientes 
elementos: 'Java', 'Ruby' y 'GoLang'.  */
let lenguajesDeProgramacion1 = ['JavaScript', 'C', 'C++', 'Kotlin', 'Python'];
lenguajesDeProgramacion1.push('Java', 'Ruby', 'GoLang')

/*4. Crea una función que muestre en la consola todos los 
elementos de la lista "lenguagesDeProgramacion. */
let lenguajesDeProgramacion2  = ['JavaScript', 'C', 'C++', 'Kotlin', 'Python'];
for (let i = 0; i < lenguajesDeProgramacion2.length; i++) {
    console.log(lenguajesDeProgramacion2[i]);
}
/*4. Crea una función que muestre en la consola todos los 
elementos de la lista "lenguagesDeProgramacion. */
let lenguajesDeProgramacion7  = ['JavaScript', 'C', 'C++', 'Kotlin', 'Python'];
for (let i = 0; i < lenguajesDeProgramacion7.length; i++) {
    console.log(lenguajesDeProgramacion7[i]);
}
/*5. Crea una función que muestre en la consola todos 
los elementos de la lista "lenguagesDeProgramacion en 
orden inverso.*/
let lenguajesDeProgramacion3  = ['JavaScript', 'C', 'C++', 'Kotlin', 'Python'];
function lenguajes(lista){
    for (let i = 0; i < lista.length; i++) {
        console.log(lista[i]);
    }
}
lenguajes(lenguajesDeProgramacion3);

/*6. Crea una función que calcule el promedio de los elementos en una 
lista de números.*/
let numeros = [12, 18, 20, 27, 32];
function promedio(lista) {
    let suma = 0;
    let largoLista = lista.length;
    for (let i = 0; i < lista.length; i++) {
        suma += lista[i];
    }
    let calculoPromedio = suma / largoLista;
    return calculoPromedio
    
}
console.log(promedio(numeros));

/*7. Crea una función que muestre en la consola el número más grande y 
el número más pequeño en una lista.*/
let conjunto = [7, 5, 12, 24, 17];
var maximo = conjunto.reduce(function (a,b){
    return Math.max(a,b);
}, -Infinity)
console.log(maximo); //24

let conjunto2 = [1,2,3,4];
function maxMin (lista) {
    let distancia = lista.length;
    let extemoSuperior = lista[distancia-1];
    let extremoInferior = lista[0];
    return [extemoSuperior,extremoInferior]
}
let [x,y] = maxMin(conjunto2);
console.log(x,y); //4 1

/*8. Crea una función que devuelva la suma de todos los elementos en 
una lista. */
let listaSuma = [2, 4, 6, 8];
function sumar(lista) {
    let acumulado = 0;
    for (let i = 0; i < lista.length; i++) {
        acumulado += lista[i];
    }
    return acumulado
}
let suma = sumar(listaSuma);
console.log(suma);

/*9. Crea una función que devuelva la posición en la lista donde se 
encuentra un elemento pasado como parámetro, o -1 si no existe en la 
lista*/
let varios = ['uno','dos','tres','cuatro'];
function indice(valor) {
    let posicion = varios.indexOf(valor);
    return posicion;
}
console.log(indice("tres"))
console.log(indice("cinco"))

/*10. Crea una función que reciba dos listas de números del mismo tamaño
y devuelva una nueva lista con la suma de los elementos uno a uno. */
let lista1 = [2,4,6,8];
let lista2 = [3,5,7,9];
function crearLista (lista1,lista2) {
    let lista3 = [];
    for (let i = 0; i < lista1.length; i++) {
        lista3.push(lista1[i]+lista2[i]); 
    }
    return lista3
}
console.log(crearLista(lista1,lista2));

/*11. Crea una función que reciba una lista de números y devuelva una 
nueva lista con el cuadrado de cada número.*/
let listaNormal = [1,2,3,4,5];
function cuadrado (lista) {
    let doble = [];
    for (let i = 0; i <= lista1.length; i++) {
        doble.push(lista[i]**2); 
    }
    return doble;
}
console.log(cuadrado(listaNormal));

