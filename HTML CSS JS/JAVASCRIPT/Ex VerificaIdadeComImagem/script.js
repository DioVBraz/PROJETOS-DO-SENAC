function verificar () {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            genero = "homem"
            if (idade >= 0 && idade < 10) {
                img.setAttribute('src', 'imagens/meninoBebe.png')
            } else if (idade < 21) {
                img.setAttribute('src', 'imagens/homemJovem.png')
            } else if (idade < 50) {
                img.setAttribute('src', 'imagens/homemAdulto.png')
            } else if (idade < 120) {
                img.setAttribute('src', 'imagens/homemVelho.png')
            } else{
                window.alert("[ERRO] Verifique os dados e tente novamente!")
            }
        } else {
            genero = "mulher"
            if (idade >= 0 && idade < 10) {
                img.setAttribute('src', 'imagens/meninaBebe.png')
            } else if (idade < 21) {
                img.setAttribute('src', 'imagens/mulherJovem.png')
            } else if (idade < 50) {
                img.setAttribute('src', 'imagens/mulherAdulta.png')
            } else if (idade < 120) {
                img.setAttribute('src', 'imagens/mulherVelha.png')
            } else{
                window.alert("[ERRO] Verifique os dados e tente novamente!")
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos`
        res.appendChild(img)
    }
}