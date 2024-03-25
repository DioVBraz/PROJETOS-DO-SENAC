function toggle1() {
    let toggle1 = document.getElementById("toggle1")
    toggle1.style.display = "none"
    let toggle2 = document.getElementById("toggle2")
    toggle2.style.display = "block"
    let img = document.getElementById("lampada")
    img.src = "img/lampadaAcessa.png"
}

function toggle2() {
    let toggle1 = document.getElementById("toggle1")
    toggle1.style.display = "block"
    let toggle2 = document.getElementById("toggle2")
    toggle2.style.display = "none"
    let img = document.getElementById("lampada")
    img.src = "img/lampadaApagada.png"
}