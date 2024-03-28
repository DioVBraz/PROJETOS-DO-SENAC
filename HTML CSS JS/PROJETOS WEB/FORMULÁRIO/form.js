const proximoBotao = document.querySelector('.btn-proximo');
const voltarBotao = document.querySelector('.btn-voltar');
const etapas = document.querySelectorAll('.etapas');
const formularios = document.querySelectorAll('.formularios');
let ativo = 1;

proximoBotao.addEventListener('click', () => {
    ativo++;
    if (ativo > etapas.length) {
        ativo = etapas.length;
    }
    updateProgress();
});

voltarBotao.addEventListener('click', () => {
    ativo--;
    if (ativo < 1) {
        ativo = 1;
    }
    updateProgress();
});

const updateProgress = () => {
    console.log('etapas.length =>' + etapas.length);
    console.log('ativo =>' + ativo);

    etapas.forEach((step, i) => {
        if (i === (ativo - 1)) {
            step.classList.add('ativo');
            formularios[i].classList.add('ativo');
            console.log('i =>' + i);
        } else {
            step.classList.remove('ativo');
            formularios[i].classList.remove('ativo');
        }
    });

    if (ativo === 1) {
        voltarBotao.disabled = true;
    } else if (ativo === etapas.length) {
        proximoBotao.disabled = true;
    } else {
        voltarBotao.disabled = false;
        proximoBotao.disabled = false;
    }
};
