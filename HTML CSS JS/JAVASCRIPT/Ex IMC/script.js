var nome = prompt('Digite seu nome: ')
var altura = Number(prompt('Digite sua altura em centímetros: '))
var peso = Number(prompt('Digite seu peso em quilogramas: '))

altura = altura / 100

var imc = peso / (altura ** 2)
imc = imc.toFixed(1)

if (imc < 16) {
    var classificacao = "Baixo peso muito grave"
    alert(`${nome} possui índice de massa corporal igual a ${imc}, sendo classificado como: ${classificacao}`)
} else if (imc < 16.99) {
    var classificacao = "Baixo peso grave"
    alert(`${nome} possui índice de massa corporal igual a ${imc}, sendo classificado como: ${classificacao}`)
} else if (imc < 18.49) {
    var classificacao = "Baixo peso"
    alert(`${nome} possui índice de massa corporal igual a ${imc}, sendo classificado como: ${classificacao}`)
} else if (imc < 24.99) {
    var classificacao = "Peso normal"
    alert(`${nome} possui índice de massa corporal igual a ${imc}, sendo classificado como: ${classificacao}`)
} else if (imc < 29.99) {
    var classificacao = "Sobrepeso"
    alert(`${nome} possui índice de massa corporal igual a ${imc}, sendo classificado como: ${classificacao}`)
} else if (imc < 34.99) {
    var classificacao = "Obesidade grau 1"
    alert(`${nome} possui índice de massa corporal igual a ${imc}, sendo classificado como: ${classificacao}`)
} else if (imc < 39.99) {
    var classificacao = "Obesidade grau 2"
    alert(`${nome} possui índice de massa corporal igual a ${imc}, sendo classificado como: ${classificacao}`)
} else {
    var classificacao = "Obesidade grau 3"
    alert(`${nome} possui índice de massa corporal igual a ${imc}, sendo classificado como: ${classificacao}`)
}