var num1 = Number(window.prompt("Digite um numero: "))
var oper = window.prompt("Digite uma operação (soma ou subtração): ")
var num2 = Number(window.prompt("Digite um numero: "))

oper = oper.toLowerCase()
operacao(num1,num2,oper)

function operacao(n1, n2, op) {
    if (op === "soma") {
        soma(n1, n2)
    } else if (op === "subtração") {
        subtracao(n1, n2)
    } else {
        window.alert("Operação inválida")
    }
}

function soma(n1, n2) {
    var resultado = n1 + n2
    document.write("O resultado da soma é: " + resultado)
}

function subtracao(n1, n2) {
    var resultado = n1 - n2
    document.write("O resultado da subtração é: " + resultado)
}