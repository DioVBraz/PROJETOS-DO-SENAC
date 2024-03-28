//step 1: get DOM
let proximo = document.getElementById('proximo');
let voltar = document.getElementById('voltar');

let container = document.querySelector('.container');
let Jogos = container.querySelector('.container .jogos-lista');
let Cards = document.querySelector('.container .cards');
let CardsItem = Cards.querySelectorAll('.item');
let tempoTransicao = document.querySelector('.container .tempo-transicao');

Cards.appendChild(CardsItem[0]);
let TempoCarregamento = 3000;
let TempoTransicao = 7000;

proximo.onclick = function(){
    showSlider('proximo');    
}

voltar.onclick = function(){
    showSlider('voltar');    
}
let TempoLimite;
let TempoProximoCard = setTimeout(() => {
    proximo.click();
}, TempoTransicao)
function showSlider(tipo){
    let  ItensControles = Jogos.querySelectorAll('.container .jogos-lista .item');
    let CardsItem = document.querySelectorAll('.container .cards .item');
    
    if(tipo === 'proximo'){
        Jogos.appendChild(ItensControles[0]);
        Cards.appendChild(CardsItem[0]);
        container.classjogos.add('proximo');
    }else{
        Jogos.prepend(ItensControles[ItensControles.length - 1]);
        Cards.prepend(CardsItem[CardsItem.length - 1]);
        container.classjogos.add('voltar');
    }
    clearTimeout(TempoLimite);
    TempoLimite = setTimeout(() => {
        container.classjogos.remove('proximo');
        container.classjogos.remove('voltar');
    }, TempoCarregamento);

    clearTimeout(TempoProximoCard);
    TempoProximoCard = setTimeout(() => {
        proximo.click();
    }, TempoTransicao)
}