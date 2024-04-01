const menu = document.querySelector('.menu-br');
const NavMenu = document.querySelector('.cabeçalho-br');

menu.addEventListener('click', () => {
    menu.classList.toggle('ativo');
    NavMenu.classList.toggle('ativo');
})