function triangulo() {
    var base = Number(window.prompt("Digite o valor da base: "))
    var altura = Number(window.prompt("Digite o valor da altura: "))
    var area = (base * altura) / 2
    var res = document.getElementById("res")
    res.innerText = "Área do triângulo: " + area
}

function quadrado() {
    var base = Number(window.prompt("Digite o valor da base: "))
    var altura = Number(window.prompt("Digite o valor da altura: "))
    var area = base * altura
    var res = document.getElementById("res")
    res.innerText = "Área do quadrado: " + area
}

function circunferencia() {
    var raio = Number(window.prompt("Digite o valor do raio: "))
    var area = Math.PI * (raio ** 2)
    area = area.toFixed(2)
    var res = document.getElementById("res")
    res.innerText = "Área da circunferência: " + area
}


