const inp = document.getElementById("inp")

function inpfocus() {
    inp.style.backgroundColor = 'yellow'
}

function inpblur() {
    if (inp.value.length == 0) {
        inp.style.backgroundColor = 'white'
    } else if (inp.value.length < 3) {
        inp.style.backgroundColor = 'red'
    } else {
        inp.style.backgroundColor = 'green'
    }
}