//variables
let numeroSecreto = 6;
let numeroUsuario = prompt("Me indicas un numero entre 1 y 10 por favor: ");

console.log(numeroUsuario);

/*Este codigo 
realiza una comparacion*/
if(numeroUsuario == numeroSecreto){
    //devuelve el mensaje alert si a condicion se cumple
    console.log("Acertaste el numero")
    alert("Acertaste el numero")
} else {
    console.log(`Lo siento, el numero secreto era: ${numeroSecreto} y elegiste el numero: ${numeroUsuario}.`)
    alert("Lo siento, el numero secreto era: "+ numeroSecreto + " y elegiste el numero:"+ numeroUsuario)
    //devuelve el mensaje si la condicion no se cumple
}




