var menuIcon = document.querySelector('.menu-icon');
var ul = document.querySelector('.ul');

menuIcon.addEventListener('click', ()=>{

    if (ul.classList.contains('ativo')){
        ul.classList.remove('ativo');
        document.querySelector('.menu-icon img').src = 'Imagens/menu.png';
    }else{
        ul.classList.add('ativo');
        document.querySelector('.menu-icon img').src = 'Imagens/close.png';
    }

})