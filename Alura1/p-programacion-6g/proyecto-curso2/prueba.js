//DESAFIOS
/*1. Crea una función que calcule el índice de masa 
corporal (IMC) de una persona a partir de su altura en 
metros y peso en kilogramos, que se recibirán como 
parámetros.*/
function indiceMasaCorporal (peso, altura) {
    let iMc = peso / (altura**2)
    return iMc
}
console.log(indiceMasaCorporal(180, 1.78))

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
            break
        }
    }
    return factorial
}
let valor1 = factorial(10)
console.log(valor1)

