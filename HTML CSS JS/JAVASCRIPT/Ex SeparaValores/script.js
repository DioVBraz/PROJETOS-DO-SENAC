function distribuirCaracter() {
    
    var caracter = document.getElementById("entrada").value

    document.getElementById("entrada").value = ""

    if (isNaN(caracter)) {
        document.getElementById("apenasLetras").value = caracter
    } else {
        document.getElementById("apenasNumeros").value = caracter
    }

}