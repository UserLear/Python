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