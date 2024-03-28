let listaProdutos = document.querySelector('.lista-produtos');
let listaCarrinho = document.querySelector('.lista-carrinho');
let carrinhoIcon = document.querySelector('.carrinho-icon');
let carinhoNumero = document.querySelector('.carrinho-icon span');
let html = document.querySelector('body');
let fecharCard = document.querySelector('.fechar');
let produtos = [];
let carrinho = [];


carrinhoIcon.addEventListener('click', () => {
    html.classList.toggle('mostrarCarrinho');
})
fecharCard.addEventListener('click', () => {
    html.classList.toggle('mostrarCarrinho');
})

    const removerDadosHTML = () => {

        if(produtos.length > 0) 
        {
            produtos.forEach(produto => {
                let novoProduto = document.createElement('div');
                novoProduto.dataset.id = produto.id;
                novoProduto.classList.add('item');
                novoProduto.innerHTML = 
                `<img src="${produto.imagem}" alt="">
                <h2>${produto.nome}</h2>
                <div class="preco">R$ ${produto.preco}</div>
                <button class="adicionarCarrinho">Adicionar no carrinho</button>`;
                listaProdutos.appendChild(novoProduto);
            });
        }
    }
    listaProdutos.addEventListener('click', (event) => {
        let posicaoClick = event.target;
        if(posicaoClick.classList.contains('adicionarCarrinho')){
            let id_produto = posicaoClick.parentElement.dataset.id;
            adicionarProduto(id_produto);
        }
    })
const adicionarProduto = (produto_id) => {
    let posicaoProdutoCarrinho = carrinho.findIndex((valor) => valor.produto_id == produto_id);
    if(carrinho.length <= 0){
        carrinho = [{
            produto_id: produto_id,
            quantidade: 1
        }];
    }else if(posicaoProdutoCarrinho < 0){
        carrinho.push({
            produto_id: produto_id,
            quantidade: 1
        });
    }else{
        carrinho[posicaoProdutoCarrinho].quantidade = carrinho[posicaoProdutoCarrinho].quantidade + 1;
    }
    adicionarCarrinho();
    adicionarProdutoQuantidade();
}
const adicionarProdutoQuantidade = () => {
    localStorage.setItem('carrinho', JSON.stringify(carrinho));
}
const adicionarCarrinho = () => {
    listaCarrinho.innerHTML = '';
    let totalquantidade = 0;
    if(carrinho.length > 0){
        carrinho.forEach(item => {
            totalquantidade = totalquantidade +  item.quantidade;
            let novoItem = document.createElement('div');
            novoItem.classList.add('item');
            novoItem.dataset.id = item.produto_id;

            let posicaoProduto = produtos.findIndex((valor) => valor.id == item.produto_id);
            let info = produtos[posicaoProduto];
            listaCarrinho.appendChild(novoItem);
            novoItem.innerHTML = `
            <div class="imagem">
                    <img src="${info.imagem}">
                </div>
                <div class="nome">
                ${info.nome}
                </div>
                <div class="totalPreco">R$${info.preco * item.quantidade}</div>
                <div class="quantidade">
                    <span class="menos"><</span>
                    <span>${item.quantidade}</span>
                    <span class="mais">></span>
                </div>
            `;
        })
    }
    carinhoNumero.innerText = totalquantidade;
}

listaCarrinho.addEventListener('click', (event) => {
    let posicaoClick = event.target;
    if(posicaoClick.classList.contains('menos') || posicaoClick.classList.contains('mais')){
        let produto_id = posicaoClick.parentElement.parentElement.dataset.id;
        let tipo = 'menos';
        if(posicaoClick.classList.contains('mais')){
            tipo = 'mais';
        }
        quantidadeCarrinho(produto_id, tipo);
    }
})
const quantidadeCarrinho = (produto_id, tipo) => {
    let posicaoItemCarrinho = carrinho.findIndex((valor) => valor.produto_id == produto_id);
    if(posicaoItemCarrinho >= 0){
        let info = carrinho[posicaoItemCarrinho];
        switch (tipo) {
            case 'mais':
                carrinho[posicaoItemCarrinho].quantidade = carrinho[posicaoItemCarrinho].quantidade + 1;
                break;
        
            default:
                let alterarQuantidade = carrinho[posicaoItemCarrinho].quantidade - 1;
                if (alterarQuantidade > 0) {
                    carrinho[posicaoItemCarrinho].quantidade = alterarQuantidade;
                }else{
                    carrinho.splice(posicaoItemCarrinho, 1);
                }
                break;
        }
    }
    adicionarCarrinho();
    adicionarProdutoQuantidade();
}

const initCatalogo = () => {
    fetch('produtos.json')
    .then(resposta => resposta.json())
    .then(dados => {
        produtos = dados;
        removerDadosHTML();

        if(localStorage.getItem('carrinho')){
            carrinho = JSON.parse(localStorage.getItem('carrinho'));
            adicionarCarrinho();
        }
    })
}
initCatalogo();