
//variables
let numeroSecreto = 6;
let numeroUsuario;
let intentos = 1;
//let palabraVeces = "vez";
let maximosIntentos = 4;

while (numeroUsuario != numeroSecreto){
    numeroUsuario = prompt("Me indicas un numero entre 1 y 10 por favor: ");
    console.log(numeroUsuario);

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
